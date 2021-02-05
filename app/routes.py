from flask import render_template,redirect,url_for,request
from services.dbservice import * #Peso=1

#//Loading Routes
#from routese.AdminStringRoutes import *
#from routese.IndexActionRoutes import *
from auto.AutoActionRoutes import *
from auto.AutoAdminRoutes import *

#//Loading Auto Routes



from main import app
dbg = Maindb() #Peso=2


#//rutas tienen que estar vinculadas a un metodo
@app.route('/home')
def home():
    return "<h1> Esta es la pagina home </h1>"

@app.route('/')
def index():
    valueG1 = "Alfa Version"
    dbg = Maindb()
    getdb = dbg.readall()
    return render_template('index.html',
                            getdb=getdb,valueG=valueG1
                            )

@app.route('/admin')
def admin():
    dbg = Maindb()
    getdb = dbg.readall()
    return render_template('admin.html',
                            getdb=getdb,
                            )

dbg.desco()