
#Volumento app.py

from flask import Flask
#from SerServices import *
from db import *


dbg = Maindb()
dbg.updateval("c5","0")

app = Flask(__name__)

#//rutas tienen que estar vinculadas a un metodo
@app.route('/home')
def home():
    return "<h1> Esta es la pagina home </h1>"

#//parametros en las rutas
@app.route('/informaciones/<string:nombre>/<apellidos>/<int:edad>')
def informaciones(nombre,apellidos):
    return f"""
    <h1> Esta es la pagina home {nombre} </h1>
    <p> {nombre} <p/>
    """

#//parametros opcionales
@app.route('/informacion/')
@app.route('/informacion/<string:nombre>/')
@app.route('/informacion/<string:nombre>/<apellidos>')
def informacion(nombre= None, apellidos= None):

    texto = ""
    if nombre != None:
        texto = f"<p> {nombre} <p/>"
    if nombre != None and apellidos != None:
        texto = f"<p> {nombre} {apellidos} <p/>"

    return f"""
    <h1> Esta es la pagina home </h1>
    {texto}
    """

from flask import redirect,url_for
#// redireccion
@app.route('/contacto/')
@app.route('/contacto/<redireccion>/')
#//si le paso cualquier parametro me redirecciona
def contacto(redireccion= None):
    if redireccion is not None:
        return (redirect(url_for('informacion2')))
    return "Pagina de contacto sin redireccion"


from flask import render_template
#// usando render templates con variables renderhtml
@app.route('/template/')
def template():
    htmlG= f"<h3> Esto es un html </h3>"
    return render_template('template.html', valueG = htmlG)


@app.route('/')
def index():
    edad = 101
    personas = ['gus','jorge','paco']
    return render_template('index.html',
                            edad=edad,
                            personas=personas)


@app.route('/c1on')
def c1on():
    print("comando enviado")
    #escritura(ON35)
    return "c1 encendido"


@app.route('/c1off')
def c1off():
    valfun= sayhellon()
    valsaludo="helloworld"
    valsaludo2="helloworld2"
    #sayhellon()
    return render_template('on.html',
                            value=valsaludo,
                            value2=valsaludo2)


#tiene que ir al final de las rutas NOTA!
#//si corro archivo llamado "main" -> palabra reservada
#//que se ejecute en modo debug
if __name__ == '__main__':
    app.run(debug=True)
