Select TABSCHEMA , TABNAME , COLNAME , REMARKS 

from SYSCAT.COLUMNS

where TABSCHEMA='' and upper(REMARKS) like '%BEGUNSTIGET%'