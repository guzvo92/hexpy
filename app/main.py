#Volumento main.py

constructorstring = 0 #Peso=0
constructortable = 1 #Peso=0

from flask import Flask

app = Flask(__name__) #peso1

from routes import * #peso2


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
    #app.run(debug=True)
    app.run(debug=True,host =str(mip),port=2500)