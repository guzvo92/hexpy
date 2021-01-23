from main import app
from services.dbservice import * #Peso=1
from services.stringservice import *
#from services.serialservice import *


dbg = Maindb() #Peso=2


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