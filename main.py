#Volumento app.py

from flask import Flask, render_template
#from services.serialservice import *
from services.dbservice import *
from services.stringservice import *

constructorstring = 0
dbg = Maindb()
app = Flask(__name__)

from .routes import *


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