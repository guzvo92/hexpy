#Volumento main.py

constructorstring = 0 #[peso0]
constructordb = 1 #[peso0]
production = 0 #[peso0]
items = 20#[peso0] Routesauto

from flask import Flask
app = Flask(__name__) #peso1

from services.makerservice import * #[peso2]
CreaActionRutesFile(items,"auto/AutoActionRoutes.py") #[peso3]
CreaConstructorCircuitos(items,"auto/AutoConstructorCirc.py") #[peso3]

from routes import * #[peso2] Archivo de rutas Maestro
from auto.AutoConstructorCirc import * #[peso2] 
from constructors.constructor_strings import * #[peso2] 
#from services.serialservice import * #[peso2] Archivo init serials


#Code ISOLATED
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
    if production == 1:
        app.run(debug=False,host =str(mip),port=2500)
    else:
        app.run(debug=True,port=2500)