from flask import render_template,redirect,url_for,request
from services.dbservice import * #Peso=1


from main import app
dbg = Maindb() #Peso=2
   

@app.route('/c1on')
def c1on():
    dbg = Maindb()
    dbg.updateval("c1","1")
    getdb = dbg.readall()

    string = getdb[0][7] #dato0 col7
    print("[Hex] "+ str(string))
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