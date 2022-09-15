setwd("~/workspace/analyse_crm_nl_avgang")

userid <- credentials[["username"]]
passwd <- credentials[["password"]]
library(ggplot2)

connection <- odbc::dbConnect(odbc::odbc(), "IVHP01", UID = userid, PWD = passwd)

select <- "SELECT (LEVETID_SISTE_AAPN_DAGER - LEVETID_SISTE_OPPH_DAGER) AS LEVETID,
  LEVETID_ANN_AARSAK_NAVN_KUNDE as AVGANGSAARSAK,
  BEST_PRM_NL_INTERV_KODE as PREMIE,
  NAERING_GRP_NAVN_PRIM as BRANSJE,
  FYLKE_NR as FYLKE,
  REGN_DRIFT_INTK as INNTEKT,
  ANT_ANSATT,
  KUNDE_SCORE_INTERV_KODE as KUNDE_SCORE,
  ANT_RISIKO
  FROM G00V.G70_PART_NL
  WHERE SKF_KUNDE_FLAGG = 0
  AND LEVETID_SISTE_OPPH_DAGER < 91
  AND (LEVETID_SISTE_AAPN_DAGER - LEVETID_SISTE_OPPH_DAGER) < 30
  AND (LEVETID_SISTE_AAPN_DAGER - LEVETID_SISTE_OPPH_DAGER) > 0"

result <- odbc::dbSendQuery(connection, select)
data <- data.table::setDT(odbc::dbFetch(result))
odbc::dbClearResult(result)
odbc::dbDisconnect(connection)

#Viser de 6 f�rste linjene
head(data)