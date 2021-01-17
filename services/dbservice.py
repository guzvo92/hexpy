import sqlite3

class Maindb:

    def __init__(self):
        #self son para propiedades de la clase (variables)
        self.conexion = sqlite3.connect('volumento.db')
        self.cursor = self.conexion.cursor() #Ejecutar consultas
        #el cursor me genera objetos

    def desco(self):
        self.conexion.close()

    def creartabla(self,tabla):
        v1="CREATE TABLE IF NOT EXISTS "
        v2= tabla
        v3= "( id INTEGER PRIMARY KEY AUTOINCREMENT,"
        v4 ="titulo varchar(255),"
        v5 ="estado int(255),"
        v6 ="urlon varchar(255),"
        v7 ="urloff varchar(255),"
        v8 ="valon varchar(255),"
        v9 ="valoff varchar(255)"
        v10 = " )"
        value = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10
        #print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def insertnewdata(self,tabla,circuito,status):
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
        v15 = "')"
        value = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13+v14+v15
        print (value)
        self.cursor.execute(value)
        self.conexion.commit()

    def updateval(self,circuito,valor):
        a1 = "UPDATE circuitos "
        b1 = "SET estado = "
        b2 = valor
        b3 = " "
        c1 = "WHERE titulo= '"
        c2 = circuito +"';"
        value = a1+b1+b2+b3+c1+c2
        #print (value)
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


'''
programadb = Maindb()
programadb.creartabla("circuitos")

programadb.insertnewdata('circuitos','c1','0')
programadb.insertnewdata('circuitos','c2','0')
programadb.insertnewdata('circuitos','c3','0')
programadb.insertnewdata('circuitos','c4','0')
programadb.insertnewdata('circuitos','c5','0')
programadb.insertnewdata('circuitos','c6','0')
programadb.insertnewdata('circuitos','c7','0')
programadb.insertnewdata('circuitos','c8','0')
programadb.insertnewdata('circuitos','c9','0')
programadb.insertnewdata('circuitos','c10','0')

#programadb.deleteval(1)
#programadb.updateval("c5","1")
programadb.desco()
'''