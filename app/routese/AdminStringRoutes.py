from flask import render_template,redirect,url_for,request
from services.dbservice import * #Peso=1


from main import app
dbg = Maindb() #Peso=2


@app.route('/changestringsC1', methods = ["POST"])
def changestringsC1():
    if request.method == 'POST':
        reqstringon = request.form['stringon'] 
        reqstringoff = request.form['stringoff'] 
        dbg = Maindb()
        dbg.updatestrings('c1',str(reqstringon),str(reqstringoff))

    return (redirect(url_for('admin')))



dbg.desco()