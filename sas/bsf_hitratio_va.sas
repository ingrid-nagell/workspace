/***********************************************************************************/
/*************************                                *************************/
/*************************        	     Privat		          *************************/
/*************************       Boligselgerforsikring    *************************/
/*************************                                *************************/
/***********************************************************************************/

/* 
Beskrivelse: Hit Ratio Rapport Boligselgerforsikring

Type: Rapportering.
Status: Under arbeid.
Av: I.N. /Applied Analytics.

Sist oppdatert: 01.08.2022
Opprettet: 01.11.2021
*/

/*TO DO
- Mellomlagre på SAS?
*/

/**************************/
/*        LIBRARIES       */
/**************************/
libname GZA       meta library = '(GZA) Raadata';
libname INFO      meta library = '(INFO) Informasjonslag';
libname tu_du     meta library = '(TU_DU) Digital Analyse'      metaout=data;
libname G70       meta library = '(G70) Prediksjonsmodellering';


/*********************************/
/*     MACROVARIABLER - DATO     */
/*********************************/
%let startdato 	= %sysevalf('01JAN22'd); 
%let sluttdato  = %sysevalf(%sysfunc(today())-1); 

%let starttime  = %sysevalf('01JAN2022:00:00'dt);

/************************/
/*       KLADDER        */
/************************/
/* Henter alle NYE kladder. 
På DEKN-NIVÅ, da hver risiko består av 1 dekning
*/
proc sql;
	create table kladd as
	select distinct	
		  a.FA99903 as dato_forekomst  	/*Dato for når tilbudet ble opprettet*/
		, a.FA99904 as tid_forekomst   /*Tidspunkt for når tilbudet ble opprettet*/
		, (DHMS(a.FA99903,0,0,a.FA99904)) FORMAT=DATETIME21.2 as datetime_forekomst /*Dato og tidspunkt for når tilbudet ble opprettet*/
		, a.FPS7101 as niva_forsikring_forekomst /*Nivå for forsikringsforekomst*/
		, a.FACCC02 as fors_nr /*Forsikringsnummer*/
		, b.FACCC03 as risiko_nr /*Risikonummer*/
		, a.FPS7102 as deknings_nr /*Dekningsnummer*/
		, b.FA06601 as grunn_dek_nr /*Grunndekningsnummer*/
		, b.FA08001 as produkt_dek_nr /*Produktdekningsnummer*/
		, a.FIN0101 as appid_forekomst_kladd /* Forteller hvilken applikasjon kladden ble opprettet */
		, a.FPS7103 as appid_forekomst_prod /* Forteller hvilken applikasjon avtalen ble opprettet */
		, b.FA99905 as opprettet_av_forekomst /*G-ident, sjekk om dette er selger 1 feltet i S2000*/
		, b.FAYYY16 as selger_1_forekomst /*selgerinformasjon*/
		, b.FAYYY18 as selger_2_forekomst /*selgerinformasjon*/
		, b.FAYYY38 as selger_3_forekomst /*selger forhandlerkanal*/
		, b.FA01305 as premie
		, (case when (b.FA06601 in('40005','40020','10034','10015')) 
				then 'J'
			else 'N'
			end) as teknisk_egenskap
		, 1 as flagg_kladd 
		, "kladd" as type_forekomst 
	from gza.gza1250_frader as a
	inner join gza.gza0013_frader as b
	on a.FPS7102= b.FACCC04 /*Joiner på dekningsnummer*/
	where a.FA99903 >= &startdato. 	
		and a.FA99903 <= &sluttdato.
		and a.FPS7101 = 'DEK'
		and b.FA99903 >= &startdato.
		and b.FA99903 <= &sluttdato.
		and b.FA99910 = 'N'
		and b.FA08001 = '16775'
		/*and a.FPS7102 ne '191199518'*/
	group by b.FACCC04 /*Grupperer på dekningsnummer i gza.gza0013*/
	having b.FA99901 = min(b.FA99901) and DHMS(b.FA99903,0,0,b.FA99904)=min(DHMS(b.FA99903,0,0,b.FA99904)) /*Vi skal ha løpenummer = minste løpenummer og dato = minste dato fra gza.gza0013*/
	order by a.FA99903;
quit;


/**************************/
/*        SALGSDATA       */
/**************************/
proc sql;
	create table prod as
	select distinct	
		  b.FA99903 as dato_forekomst  
		, b.FA99904 as tid_forekomst  
		, (DHMS(b.FA99903,0,0,b.FA99904)) FORMAT=DATETIME21.2 as datetime_forekomst /*Dato og tidspunkt for når tilbudet ble opprettet*/
		, (DHMS(a.FA99903,0,0,a.FA99904)) FORMAT=DATETIME21.2 as datetime_kladd /*Dato og tidspunkt for når tilbudet ble opprettet*/
		, a.FPS7101 as niva_forsikring_forekomst /*Nivå for forsikringsforekomst*/
		, a.FACCC02 as fors_nr /*Forsikringsnummer*/
		, b.FACCC03 as risiko_nr /*Risikonummer*/
		, a.FPS7102 as deknings_nr /*Dekningsnummer*/
		, b.FA06601 as grunn_dek_nr /*Grunndekningsnummer*/
		, b.FA08001 as produkt_dek_nr /*Produktdekningsnummer*/
		, a.FIN0101 as appid_forekomst_kladd /* Forteller hvilken applikasjon kladden ble opprettet */
		, a.FPS7103 as appid_forekomst_prod /* Forteller hvilken applikasjon avtalen ble opprettet */
		, b.FA99905 as opprettet_av_forekomst /*G-ident, sjekk om dette er selger 1 feltet i S2000*/
		, b.FAYYY16 as selger_1_forekomst /*selgerinformasjon*/
		, b.FAYYY18 as selger_2_forekomst /*selgerinformasjon*/
		, b.FAYYY38 as selger_3_forekomst /*selger forhandlerkanal*/
		, b.FA01305 as premie
		, (case when (b.FA06601 in('40005','40020','10034','10015')) 
				then 'J'
			else 'N'
			end) as teknisk_egenskap
		, 1 as flagg_salg /* Denne flagger ut salgene med nummer 1 */
		, "salg" as type_forekomst /* Forteller type forekomst*/
	from gza.gza1250 as a
	inner join gza.gza0013 as b
	on a.FPS7102= b.FACCC04 /*Joiner på dekningsnummer*/
	where a.FA99903 >= &startdato. 	
		and a.FA99903 <= &sluttdato.
		and a.FPS7101 = 'DEK'			
		and b.FA99903 >= &startdato.
		and b.FA99903 <= &sluttdato. 
		and b.FA99910 = 'N'
		and b.FA08001 = '16775'
	group by b.FACCC04 /*Grupperer på dekningsnummer i gza.gza0013*/
	having b.FA99901 = min(b.FA99901) 
		and DHMS(b.FA99903,0,0,b.FA99904) = min(DHMS(b.FA99903,0,0,b.FA99904)) /*Vi skal ha løpenummer = minste løpenummer og dato = minste dato fra gza.gza0013*/
	;
quit;

/************************/
/*   SKRIV TIL TU_DU    */
/************************/



/************************/
/*  SAMMENSTILLE DATA   */
/************************/
data s2000_data; 
	set kladd prod;
	/*Excel-variabler*/
	excel_aar = year(dato_forekomst);
	excel_maned =strip(put(dato_forekomst, monname.));
	excel_aar_mnd_02 = input(put(dato_forekomst, yymmn6.), 6.);
run;

proc sql;
	create table join_flagg_salg as
	select 
		a.*
		, b.flagg_salg as flagg_prod
		, b.premie as salg_premie
		, b.dato_forekomst as salg_dato
	from s2000_data as a
	left join prod as b
		on a.deknings_nr = b.deknings_nr and a.type_forekomst = 'kladd' 
	order by a.deknings_nr
	;
quit;

proc sort data=join_flagg_salg out=s2000_sorted;
by dato_forekomst;
quit;


/**************************/
/*     PRODUKTSTRUKTUR    */
/**************************/
proc sql; 
	create table produktstruktur as
	select distinct 
	  a.FA08001 as produkt_dek_nr
	, a.FA08002 as produkt_dek_navn
	, a.FA07901 as produkt_ris_nr
	, b.FA07902 as produkt_ris_navn
	from gza.gza0080 as a
	left join gza.gza0079 as b
		on a.FA07901=b.FA07901
	where a.FA08001 = '16775'
	group by a.FA08001 
	having a.FA99901 = max(a.FA99901)and b.FA99901 = max(b.FA99901)
	;
quit; 

proc sql; 
	create table join_produktstruktur as 
	select distinct
		a.*
		,b.produkt_dek_navn
		,b.produkt_ris_nr
		,b.produkt_ris_navn
	from s2000_sorted as a
	left join produktstruktur as b
		on a.produkt_dek_nr = b.produkt_dek_nr	
	;
quit; 



/************************/
/*        MEGLER        */
/************************/
/*Henter partref som hører til forsikringen*/
proc sql;
	create table partref_data as 
	select distinct
		FACCC02 as fors_nr 
		, FAYYY02 as partref
	from gza.gza0011_frader
	where FA99903 >= &startdato. 	
		and FA99903 <= &sluttdato.
	;
quit;


proc sql; 
	create table partid_data as 
	select distinct 
	  PART_IDENT as part_id
	, OFF_IDENT as org_nr
	, OFF_IDENT_FORRIGE
	, KORT_NAVN as part_navn
	, PART_REF as partref
	, PERS_ORG_KODE as part_type
	from info.d_part_sh_siste
	;
quit;

proc sql; 
	create table org_id_data as 
	select distinct 
	  OFF_ORG_NR
	, OFF_ORG_0_NR
	, ORG_0_NAVN
	, OFF_ORG_NR_FORELDR
	, ORG_NAVN_FORELDR
	from info.d_kons_str_sh_siste
	where OFF_ORG_NR ne ''
	;
quit;
 

proc sql;
	create table gk_join as
	select 
	a.*
	, b.partref
	, c.part_id
	, c.org_nr
	, c.off_ident_forrige
	, c.part_navn
	, c.part_type
	, d.OFF_ORG_0_NR
	, d.ORG_0_NAVN
	, d.OFF_ORG_NR_FORELDR
	, d.ORG_NAVN_FORELDR
	from join_produktstruktur as a
	left join partref_data as b
		on a.fors_nr = b.fors_nr
	/*Left join med where -> joiner inn info kun der tab c er org.*/
	inner join partid_data (where=(part_type = 'O'))  as c
		on b.partref = c.partref
	left join org_id_data as d
		on c.org_nr = d.off_org_nr
	;
quit;


/*Lager en part_navn_dec til bruk i lagring av filer på eget området*/
proc sql;
	create table partnavn_decoded as
	select *
	, tranwrd(prxchange('s/ as$//', -1, strip(compress(tranwrd(tranwrd(tranwrd(lowcase(tranwrd(part_navn,"&", "og")), 'ø', 'o'),'æ','ae'), 'å', 'aa'), '','p'))),' ', '-') as part_navn_dec LENGTH=15
	from gk_join;
quit;

/*
proc freq data=partnavn_decoded;
table part_navn_dec;
run;
*/

/** OVERSIKT ALLE PARTER I DF
proc sql;
	create table oversikt_part as
	select distinct
	part_navn
	, partref
	, selger_2_forekomst
	, part_type
	, part_id
	, org_nr
	, OFF_IDENT_FORRIGE
	, OFF_ORG_0_NR
	, ORG_0_NAVN
	, OFF_ORG_NR_FORELDR
	, ORG_NAVN_FORELDR
	from gk_join
	order by part_type desc, part_navn
	;
quit;
**/


/**************************/
/*     KJØPER OG SELGER   */
/**************************/ 
/*

GIR DUPLIKATER, TATT UTT ENN SÅ LENGE

*/

/*Kun på rader type 'prod'
proc sql;
	create table selger_frader as
	select distinct
	  a.FA00601 as rollekode
	, a.FACCC02 as fors_nr
	, a.FAYYY02 as selger_partref
	, b.part_id as selger_part_id
	, b.part_navn as selger_part_navn
	, b.part_type as selger_part_type
	from gza.gza0333_frader as a
	left join partid_data as b
		on a.FAYYY02 = b.partref
	where a.FA00601 = 'SE'
	;
quit;
*/

/* UNDERSØK NÅR VI HAR FAKTISKE VERDIER */
/*
proc sql;
	create table selger_prod as
	select distinct
	  a.FA00601 as rollekode
	, a.FACCC02 as fors_nr
	, a.FAYYY02 as selger_partref
	, b.part_id as selger_part_id
	, b.part_navn as selger_part_navn
	, b.part_type as selger_part_type
	, b.kommune_nr as selger_kommune_nr
	from gza.gza0333_frader as a
	left join partid_data as b
		on a.FAYYY02 = b.partref
	where FA00601 = 'SE'
	;
quit;
*/
/*
proc sql;
	create table kjoper_prod as
	select distinct
	 a.FA00601 as rollekode
	, a.FACCC02 as fors_nr
	, a.FAYYY02 as kjoper_partref
	, b.part_id as kjoper_part_id
	, b.part_navn as kjoper_part_navn
	, b.part_type as kjoper_part_type
	from gza.gza0333 as a
	left join partid_data as b
		on a.FAYYY02 = b.partref
	where FA00601 = 'KJ'
	;
quit;


proc sql;
	create table se_kj_join as
	select 
	a.*
	, b.selger_partref
	, b.selger_part_id
	, b.selger_part_navn
	, b.selger_part_type
	, c.kjoper_partref
	, c.kjoper_part_id
	, c.kjoper_part_navn
	, c.kjoper_part_type
	from partnavn_decoded as a
	left join selger_frader as b
		on a.fors_nr = b.fors_nr
		and a.type_forekomst = 'kladd'
	left join kjoper_prod as c
		on a.fors_nr = c.fors_nr
		and a.type_forekomst = 'salg'
	;
quit;
*/

/*SJEKK OM ANTALL UNIKE DEKNINGSNR = UNIKE FORSIKRINGSNR*/

/*************************/
/*  BOLIGSELGERFORSIKRING  */
/*************************/
/*Her joines BSF data inn, burde den egentlig legges på som egne rader?
Kan fikse senere evt*/
proc sql;
	create table bsf_data_01 as
	select a.*
		, b.FA99903 as bsf_dato
		, b.FA99904 as bsf_tid
		, b.FA99905 as bsf_gident
		, b.FA99906 as bsf_annulasjon
		, b.FA99908 as bsf_gjelder_fra
		, b.FA99909 as bsf_gjelder_til
		, b.FA99910 as bsf_kode_oppr
		, b.FA99912 as bsf_kode_ann
		, b.FACCC01 as bsf_kildesys
		, b.FACCC02 as bsf_forsnr
		, b.FACCC03 as bsf_risiko_nr
		, b.FRI4808 as bsf_oppdragsid
		, b.FPS3520 as bsf_kode_eierform
		, b.FRI4804 as bsf_egenerklaring_signert
		, (case when '31DEC2021'd < b.FRI4804 < '31DEC9999'd then 'J'
			end) as bsf_flagg_signert 
		, b.FRI4805 as bsf_prisantydning
		, b.FRI4806 as bsf_salgssum
		, (case when b.FRI4806 > 0 then 'J'
			end) as bsf_flagg_salgssum 
		, (case when b.FRI4806 > 0 then b.FRI4806 - b.FRI4805 
			end)	as bsf_avvik_salgssum
		, b.FRI4807 as bsf_overtakelsesdato
		, (case when '31DEC2021'd <  b.FRI4807 < '31DEC9999'd then 'J'
			end) as bsf_flagg_overtakelse
		, b.FRI4808 as bsf_dodsbo
		, b.FRI4809 as bsf_ikraftdato
		, b.FRI4810 as bsf_oppr_ikraft

		,(case when a.type_forekomst = 'salg' then premie end) as salgspremie
	
	from partnavn_decoded as a
	left join gza.gza1694_frader as b
		on a.risiko_nr = b.FACCC03
		and a.type_forekomst = 'kladd'
	group by b.FACCC03
	having b.IBMSNAP_LOGMARKER=min(b.IBMSNAP_LOGMARKER)
	order by risiko_nr, datetime_forekomst
	;
quit;

data bsf_data;
	set bsf_data_01;
	if type_forekomst = 'kladd' and bsf_flagg_signert = 'J'
		then int_kladd_signering = intck('day', dato_forekomst, bsf_egenerklaring_signert);
	if type_forekomst = 'kladd' and bsf_flagg_overtakelse = 'J'
		then int_kladd_overtagelse = intck('day', dato_forekomst, bsf_overtakelsesdato);
	if flagg_prod = 1 and bsf_flagg_overtakelse = 'J' and bsf_overtakelsesdato <= salg_dato then flagg_overtak_for_salg = 1;
	if flagg_prod = 1 and bsf_flagg_overtakelse = 'J' and bsf_overtakelsesdato > salg_dato then flagg_overtak_for_salg_storre = 1;
run;


/**************************/
/*      LAST TIL CAS      */
/**************************/

%loadCasTable(
	sourcelib=work, 
	sourcetablename=bsf_data, 
	castablename=TI_AA_BSF_hitratio, 
	caslib=ASR_WEBDATA, 
	save=true
	);



/**************************************************************************************/
/***********************/
/*    UTSENDELSE AV    */
/*      RAPPORTER      */
/***********************/

/* Opprett kun hvis dagen spørringen kjører er den 01 i måneden*/
%IF %sysfunc(today(),day.)=1 %THEN
%DO;


/***********************/
/*   RAPPORTDMACROER   */
/***********************/
/*Mottaker macro (nyttig hvis flere eposter)*/
%let avsender 	= "ingrid.nagell@gjensidige.no"; 
%let mottaker 	= "monika-sande.nore@gjensidige.no";
%let kopi 		= "ingrid.nagell@gjensidige.no";
/*%let mottaker 	= "ingrid.nagell@gjensidige.no";*/

/*Forrige måned som macro - lag denne med TODAY-func i steden, ikke max eller min*/
%let prev_month = %sysfunc(intnx(month,"&sysdate"d,-1),yymmn.);

/*Innværende måned som macro*/
%let curr_month = %sysfunc(intnx(month,"&sysdate"d,0),yymmn.);


/******************************/
/*   OPPSUMMERINGSRAPPORT     */
/******************************/
/****** TABELLER *****/
/*PR FORETAK PR MÅNED*/
proc sql; 
	create table bsf_summary as
	select distinct
	part_navn
	, org_nr
	, partref
	, selger_2_forekomst
	, excel_aar
	, excel_maned
	, excel_aar_mnd_02
	, sum(flagg_kladd) as antall_prisberegninger
	, sum(flagg_salg) as antall_salg
	, sum(salgspremie) as salgspremie
	from bsf_data
	where excel_aar_mnd_02 ne &curr_month.
	group by org_nr, selger_2_forekomst, excel_aar_mnd_02
	order by part_navn, selger_2_forekomst, excel_aar_mnd_02
	;
quit;

/*PR FORETAK SISTE MÅNED*/
proc sql;
	create table bsf_last_month as
	select *
	from bsf_summary
	where excel_aar_mnd_02 = &prev_month.
	;
quit;


/***** EXCEL *****/
/*Definer navn på workbook. Husk ".xlsx"*/
ods excel file="/mnt_g/GF_NO/TU/G020772/bsf/bsf_hit_ratio&prev_month..xlsx" ;

/*Infoside*/
ods excel options(
	sheet_name = "Om rapporten"
	);
proc odstext;
    p "Om rapporten:" / style=[color=black font_weight=bold];
	p "Månedlig rapportering for Boligselgerforsikring.";
	p "Denne rapporten inneholder informasjon om aktiviteten rundt BSF pr meglerforetak.";
	p " ";
	p "Nøkkelbegrep:";
	p "Forsikringer opprettet (kladder): Antall forsikringskladder opprettet av meglerkontorene i perioden.";
	p "Solgte forsikringer: Antall solgte forsikringer til kunder i perioden.";
	p "";
	p "Rapporten finnes også i utvidet format i SAS VA. For spørsmål angående rapporten, kontakt digital.analyse@gjensidige.no.";
run;

/*ReportSheet med datarapport*/
ods excel options(
	sheet_name = "Siste måned" 
	autofilter = "1-2"
	frozen_headers = "1"
	);
proc report data = bsf_last_month;
	define part_navn			/ display 'Meglerforetak';
	define org_nr				/ noprint;
	define partref				/ noprint;
	define selger_2_forekomst	/ display "Meglerkontor-ID";
	define excel_aar			/ display "År";
	define excel_maned			/ display "Måned";
	define excel_aar_mnd_02		/ noprint;
	define antall_prisberegninger / display "Forsikringer opprettet (kladder)" analysis;
	define antall_salg			/ display "Solgte forsikringer" analysis;
	define salgspremie			/ display "Premie" analysis '(NOK)';
	rbreak after / summarize;
	compute part_navn;
    	if missing(part_navn) then part_navn = 'TOTAL';
		if part_navn = 'TOTAL' then call define(_row_,"style","style={background=cxEEFFFF}");
	endcomp;
run;

/*ReportSheet med datarapport*/
ods excel options(
	sheet_name = "Alle data"
	embedded_titles = "on"
	autofilter = "1-4"
	frozen_headers = "1"
	);
proc report data = bsf_summary;
	define part_navn			/ display 'Meglerforetak';
	define org_nr				/ noprint;
	define partref				/ noprint;
	define selger_2_forekomst	/ display "Meglerkontor-ID";
	define excel_aar			/ display "År";
	define excel_maned			/ display "Måned";
	define excel_aar_mnd_02		/ noprint;
	define antall_prisberegninger / display "Forsikringer opprettet (kladder)" analysis;
	define antall_salg			/ display "Solgte forsikringer" analysis;
	define salgspremie			/ display "Premie" analysis '(NOK)';
	rbreak after / summarize;
	compute part_navn;
    	if missing(part_navn) then part_navn = 'TOTAL';
		if part_navn = 'TOTAL' then call define(_row_,"style","style={background=cxEEFFFF}");
	endcomp;
run;

/*Close ODS EXCEL*/
ods excel close;

/****** EPOST *******/
filename outbox email (&avsender.);

data _null_;
		file outbox
		to = (&mottaker.)
		cc = (&kopi.)
		from = (&avsender.)
		subject = ("UTKAST: BSF hit ratio-rapport totaloversikt")

		/*Valgfri: Legg ved excelfil fra G-området*/
		attach = ("/mnt_g/GF_NO/TU/G020772/bsf/bsf_hit_ratio&prev_month..xlsx" content_type="application/xlsx");
		
		/*Tekst i Epost*/
		put "Hei,";
		put " ";
		put "Vedlagt finner du Hit Ratio-rapporten for boligselgerforsikring.";
		put "Rapporten sendes ut den 1. i hver måned.";
		put "Rapporten oppdateres daglig i SAS VA.";
		put " ";
		put "Spørsmål angående rapporten kan rettes til";
		put &avsender.;
		put " ";
		put "Ingrid Nagell";
		put "Anvendt Analyse | Gjensidige Forsikring AS";

run;



/************************/
/*   PR MEGLERFORETAK   */
/************************/
/****** MACROER ******/

/*Samle Foss og CO i en rapport - finnes det overordnet id i nl-reg? som iv kan bruke istedenfor?*/



/*
Lage mapping over kategorier for meglerforetak i proc sql
Deretter filtereri macroen under på 
1) månedlig, 2) kvartal
*/

/*proc sql;*/
/*create table bsf_data_kat as*/
/*select *, */
/*	(case when substr(part_id,2) in &liste_orgnr. then '1' end) as megler_kat*/
/*from bsf_data*/
/*;*/
/*quit;*/

/** MANUELL LISTE **/
/*
%let liste_orgnr = (
			  '0814460002',	
			  '0926312537',
			  '123'
			);
*/

/*Liste over parter siste måned fra df*/
proc sql;
	select distinct org_nr into : liste_org
	separated by ' '
	from bsf_data
	where excel_aar_mnd_02 = &prev_month.
	;
quit;

/*
proc sql;
	create table sjekk as
	select distinct org_nr, part_navn_dec
	from bsf_data
	where excel_aar_mnd_02 = &prev_month.
	order by part_navn_dec
	;
quit; 
*/

/*Tom epost-attachment liste*/
%let attachment = ;

/****** LOOP OVER MEGLERKONTOR ******/
%MACRO getBSFdata;
%local i next_id next_name a;
%let i=1;

%DO %while (%scan(&liste_org., &i) ne );
   %let next_id = %scan(&liste_org., &i);

proc sql;
	create table bsf_&next_id. as
	select distinct
	part_navn
		, part_navn_dec
		, partref
		, selger_2_forekomst
		, excel_aar
		, excel_maned
		, sum(flagg_kladd) as antall_prisberegninger
		, sum(flagg_salg) as antall_salg
		, sum(salgspremie) as salgspremie
	from bsf_data
	where excel_aar_mnd_02 = &prev_month.
		and org_nr = "&next_id."
	group by org_nr, selger_2_forekomst, excel_aar_mnd_02
	;
quit;

proc sql;
  select 
    max(part_navn_dec) 
    into :part_navn_tit
  from bsf_&next_id.;
  ;
quit;


/*** EXCEL ***/
/*Definer navn på workbook. Husk ".xlsx"*/
%let myfile = %sysfunc(compress("/mnt_g/GF_NO/TU/G020772/bsf/bsf_&part_navn_tit._&prev_month..xlsx"));
ods excel file = &myfile. ;

/*Infoside*/
ods excel options(
	sheet_name = "Om rapporten"
	);
proc odstext;
    p "Om rapporten:" / style=[color=black font_weight=bold];
	p "Månedlig rapportering for Boligselgerforsikring.";
	p "Denne rapporten inneholder infromasjon om aktiviteten rundt BSF pr meglerforetak, pr måned.";
	p " ";
	p "Nøkkelbegrep:";
	p "Forsikringer opprettet (kladder): Antall forsikringskladder opprettet av meglerkontorene i perioden.";
	p "Solgte forsikringer: Antall solgte forsikringer til kunder i perioden.";
	p "";
	p "Rapporten finnes også i utvidet format i SAS VA. For spørsmål angående rapporten, kontakt digital.analyse@gjensidige.no.";
run;

/*ReportSheet med datarapport*/
ods excel options(
	sheet_name = "Siste måned" 
	autofilter = "1"
	frozen_headers = "1"
	);
proc report data = bsf_&next_id.;
	define part_navn			/ display 'Meglerforetak';
	define partref				/ noprint;
	define part_navn_dec		/ noprint;
	define selger_2_forekomst	/ display "Meglerkontor-ID";
	define excel_aar			/ display "År";
	define excel_maned			/ display "Måned";
	define antall_prisberegninger / display "Antall risikoer opprettet" analysis;
	define antall_salg			/ display "Solgte forsikringer" analysis;
	define salgspremie			/ display "Premie" analysis '(NOK)';
	rbreak after / summarize;
	compute part_navn;
    	if missing(part_navn) then part_navn = 'TOTAL';
		if part_navn = 'TOTAL' then call define(_row_,"style","style={background=cxEEFFFF}");
	endcomp;
run;


/*Close ODS EXCEL*/
ods excel close;

%let a = %sysfunc(compress("/mnt_g/GF_NO/TU/G020772/bsf/bsf_&part_navn_tit._&prev_month..xlsx")) content_type="application/xlsx";
%let attachment = &attachment. &a.;

%let i = %eval(&i + 1);

%END;
%MEND;
%getBSFdata;


/*** EPOST ***/
filename outbox email (&avsender.);

data _null_;
		file outbox
		to = (&mottaker.)
		cc = (&kopi.)
		from = (&avsender.)
		subject = ("UTKAST: BSF hit ratio-rapport pr meglerforetak")

		/*Valgfri: Legg ved excelfil fra G-området*/
		attach = (&attachment.);
		
		/*Tekst i Epost*/
		put "Hei,";
		put " ";
		put "Vedlagt finner du Hit Ratio-rapporten for boligselgerforsikring pr meglerforetak.";
		put "Rapporten sendes ut den 1. i hver måned.";
		put "Rapporten oppdateres daglig i SAS VA.";
		put " ";
		put "Spørsmål angående rapporten kan rettes til";
		put &avsender.;
		put " ";
		put "Ingrid Nagell";
		put "Anvendt Analyse | Gjensidige Forsikring AS";

run;


/*SLETTER ALLE FILENE FRA MAPPEN*/

/*Liste med navn på filer: */
data have;
	rc=filename('xx',"/mnt_g/GF_NO/TU/G020772/bsf/");
	did=dopen('xx');
	do i=1 to dnum(did);
 	fname=dread(did,i);
 	output;
	end;
	rc=dclose(did);
run;

/*Lager macro som skal brukes til å slette filer*/
%macro dfile(fname=);
	data _null_;
	rc=filename('temp', "/mnt_g/GF_NO/TU/G020772/bsf/&fname");
	if rc=0 and fexist('temp') then rc=fdelete('temp');
	rc=filename('temp');
	put _all_;
	run;
%mend;

/*Sletter filer ved bruk av liste og macro*/
data _null_;
 set have;
 call execute(cats('%dfile(fname=',fname,')'));
run;

/*AVSLUTTER IF-THEN-DO STATEMENT*/
%END;


/************************************************************************************************/
/**************************/
/*   SLETTER WORK DATA    */
/**************************/
proc datasets library=WORK kill; run; quit;

