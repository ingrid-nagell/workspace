select st.TABLE_SCHEM, st.TABLE_NAME, sc.NAME, sc.remarks, sc.COLTYPE, sc.NULLS, sc.COLTYPE, sc.LENGTH, sc.SCALE, sc.HIGH2KEY, sc.LOW2KEY, sc.TYPENAME, sc.NUMNULLS, sc.IDENTITY, sc.COLNO
from  SYSIBM.SYSCOLUMNS sc 
inner join  
(select TABLE_NAME, TABLE_SCHEM 
from SYSIBM.SQLTABLES
where TABLE_SCHEM = 'INFO') 
as st 
on sc.TBNAME = st.TABLE_NAME and sc.TBCREATOR = 'G00V'
order by st.TABLE_NAME, sc.COLNO
