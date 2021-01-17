
#Volumento app.py

from flask import Flask, render_template
from services.serialservice import *
from services.dbservice import *
dbg = Maindb()


dbg.updateval("c5","1")
dbg.updateval("c1","1")

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
    return render_template('index.html',
                            getdb=getdb,
                            )

@app.route('/c1off')
def c1off():
    dbg = Maindb()
    dbg.updateval("c1","0")
    getdb = dbg.readall()
    return render_template('index.html',
                            getdb=getdb,
                            )


dbg.desco()

#tiene que ir al final de las rutas NOTA!
#//si corro archivo llamado "main" -> palabra reservada
#//que se ejecute en modo debug
if __name__ == '__main__':
    app.run(debug=True)
