Select 
IBMSNAP_LOGMARKER,
IBMSNAP_OPERATION,
FSD0003 as dato,
FSD0004 as tid,
FDE0101 as dekningsnr,
FSD0001 as lopenr,
FSD0002 as type_f,
FSD0005 as ident,
FDE0148 as selger2
from Kafka.STDE001 where FPD0501 = '16775' and dekningsnr = 'x'
order by FDE0101 desc, IBMSNAP_LOGMARKER, IBMSNAP_OPERATION

-- FA08001 = prod_dekning
