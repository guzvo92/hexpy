#Volumento app.py

from flask import Flask, render_template
#from services.serialservice import *
from services.dbservice import *
from services.stringservice import *

constructorstring = 0


###################### dbservice.py

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
        v9 ="valoff varchar(255),"
        v10 ="stringon varchar(255),"
        v11 ="stringoff varchar(255)"
        v12 = " )"
        value = v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12
        #print (value)
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


################# main.py

dbg = Maindb()

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


app = Flask(__name__)

#//rutas tienen que estar vinculadas a un metodo
@app.route('/home')
def home():
    return "<h1> Esta es la pagina home </h1>"

@app.route('/')
def index():
    dbg = Maindb()
    getdb = dbg.readall()
    return render_template('index.html',
                            getdb=getdb,
                            )

@app.route('/c1on')
def c1on():
    dbg = Maindb()
    dbg.updateval("c1","1")
    getdb = dbg.readall()

    url = getdb[0][7]
    print("[Hex] "+ str(url))
    return render_template('index.html',
                            getdb=getdb,
                            )

@app.route('/c1off')
def c1off():
    dbg = Maindb()
    dbg.updateval("c1","0")
    getdb = dbg.readall()

    url = getdb[0][8]
    print("[Hex] "+ str(url))
    return render_template('index.html',
                            getdb=getdb,
                            )


dbg.desco()


import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

mip = get_ip()

#tiene que ir al final de las rutas NOTA!
#//si corro archivo llamado "main" -> palabra reservada
#//que se ejecute en modo debug
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=True,host =str(mip),port=2500)