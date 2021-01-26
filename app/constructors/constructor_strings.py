from services.dbservice import *
from main import constructorstring
dbg = Maindb()

C1ON="stringon"
C1OFF="stringoff"
C2ON=""
C2OFF=""
C3ON=""
C3OFF=""
C4ON=""
C4OFF=""
C5ON=""
C5OFF=""
C6ON=""
C6OFF=""
C7ON=""
C7OFF=""
C8ON=""
C8OFF=""
C9ON=""
C9OFF=""
C10ON=""
C10OFF=""

#SI QUIERO HACER UN BUCLE NECESITO
#SABER PARSEAR DE STR A VAR
# O HACER TODO EL DOC CON PYTHON
if constructorstring == 1:
    dbg.updatestrings('c1',C1ON,C1OFF)
    dbg.updatestrings('c2',C2ON,C2OFF)
    dbg.updatestrings('c3',C3ON,C3OFF)
    dbg.updatestrings('c4',C4ON,C4OFF)
    dbg.updatestrings('c5',C5ON,C5OFF)
    dbg.updatestrings('c6',C6ON,C6OFF)
    dbg.updatestrings('c7',C7ON,C7OFF)
    dbg.updatestrings('c8',C8ON,C8OFF)
    dbg.updatestrings('c9',C9ON,C9OFF)
    dbg.updatestrings('c10',C10ON,C10OFF)
