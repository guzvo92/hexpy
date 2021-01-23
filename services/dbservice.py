import sqlite3

class Maindb:

    def __init__(self):
        #self son para propiedades de la clase (variables)
        self.conexion = sqlite3.connect('volumento.db')
        self.cursor = self.conexion.cursor() #Ejecutar consultas
        #el cursor me genera objetos

    def desco(self):
        self.conexion.close()

    def borrartabla(self,tabla):
        v1="DROP TABLE "
        v2= tabla
        v3= " "
        value = v1+v2+v3
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def creartabla(self,tabla):
        v1="CREATE TABLE IF NOT EXISTS "
        v2= tabla
        v3= "( id INTEGER PRIMARY KEY AUTOINCREMENT,"
        v4 ="titulo varchar(255),"
        v5 ="estado int(255),"
        v6 ="urlon varchar(255),"
        v7 ="urloff varchar(255),"
        v8 ="valon varchar(255),"
        v9 ="valoff varchar(255),"
        v10 ="stringon varchar(255),"
        v11 ="stringoff varchar(255)"
        v12 = " )"
        value = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def insertnewdata(self,tabla,circuito,status,stringon,stringoff):
        v1 = "INSERT INTO "
        v2 = tabla
        v3 = " VALUES (null, '"
        v4 = circuito
        v5 = "','"
        v6 = status
        v7 = "','"
        v8 = "/"+str(circuito)+"on"
        v9 = "','"
        v10= "/"+str(circuito)+"off"
        v11 = "','"
        v12 = str(circuito)+" On"
        v13 = "','"
        v14= str(circuito)+" Off"
        v15 = "','"
        v16= str(stringon)
        v17 = "','"
        v18= str(stringoff)
        v19 = "')"
        value = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15+v16+v17+v18+v19
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    #editar a parametros opcionales PENDIENTE
    def updatevalfull(self,circuito,valor,stringon,stringoff):
        a1 = "UPDATE circuitos "
        a2 = "SET estado = "
        a3 = valor
        a4 = ","
        a5 = "stringon = '"
        a6 = stringon
        a7 = "'"
        a8 = ","
        a9 = "stringoff = '"
        a10 = stringoff
        a11 = "' WHERE titulo= '"
        a12 = str(circuito) + "';"
        value = a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12
        value2 = a1+a2+a3+a11+a12
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def updateval(self,circuito,valor):
        a1 = "UPDATE circuitos "
        a2 = "SET estado = "
        a3 = valor
        a4 = " WHERE titulo= '"
        a5 = str(circuito) + "';"
        value = a1+a2+a3+a4+a5
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def updatestrings(self,circuito,stringon,stringoff):
        a1 = "UPDATE circuitos "
        a2 = "SET stringon = '"
        a3 = stringon
        a4 = "'"
        a5 = ","
        a6 = "stringoff = '"
        a7 = stringoff
        a8 = "' WHERE titulo= '"
        a9 = str(circuito) + "';"
        value = a1+a2+a3+a4+a5+a6+a7+a8+a9
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def deleteval(self,id):
        v1 = "DELETE FROM circuitos WHERE id="
        v2 = str(id) + " "
        value= v1+v2
        #print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def readall(self):
        self.cursor.execute("SELECT * FROM circuitos")
        self.circuitos = self.cursor.fetchall()
        #print(self.circuitos)
        self.conexion.commit()
        return self.circuitos

dbg = Maindb()

from main import constructortable

if constructortable == 1:
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