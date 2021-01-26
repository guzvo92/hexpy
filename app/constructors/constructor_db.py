from main import constructordb
from services.dbservice import *

if constructordb == 1:

    dbg = Maindb() #Peso=2

    dbg.borrartabla('circuitos')
    dbg.creartabla('circuitos')
    dbg.insertnewdata('circuitos','c1','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c2','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c3','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c4','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c5','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c6','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c7','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c8','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c9','0','stringonG','stringoffG')
    dbg.insertnewdata('circuitos','c10','0','stringonG','stringoffG')

    dbg.desco()
