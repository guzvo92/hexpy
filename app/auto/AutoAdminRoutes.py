#//[This is an Autofile by GMAN]
from flask import render_template,redirect,url_for,request
from services.dbservice import * #Peso=1
from main import app
dbg = Maindb() #Peso=2
@app.route('/changestringsc1', methods = ['POST'])
def changestringsc1():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c1',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc2', methods = ['POST'])
def changestringsc2():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c2',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc3', methods = ['POST'])
def changestringsc3():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c3',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc4', methods = ['POST'])
def changestringsc4():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c4',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc5', methods = ['POST'])
def changestringsc5():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c5',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc6', methods = ['POST'])
def changestringsc6():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c6',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc7', methods = ['POST'])
def changestringsc7():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c7',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc8', methods = ['POST'])
def changestringsc8():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c8',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc9', methods = ['POST'])
def changestringsc9():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c9',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc10', methods = ['POST'])
def changestringsc10():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c10',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc11', methods = ['POST'])
def changestringsc11():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c11',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc12', methods = ['POST'])
def changestringsc12():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c12',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc13', methods = ['POST'])
def changestringsc13():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c13',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc14', methods = ['POST'])
def changestringsc14():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c14',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc15', methods = ['POST'])
def changestringsc15():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c15',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc16', methods = ['POST'])
def changestringsc16():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c16',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc17', methods = ['POST'])
def changestringsc17():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c17',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc18', methods = ['POST'])
def changestringsc18():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c18',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc19', methods = ['POST'])
def changestringsc19():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c19',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
@app.route('/changestringsc20', methods = ['POST'])
def changestringsc20():
    if request.method == 'POST':
        reqstringon = request.form['stringon']
        reqstringoff = request.form['stringoff']
        dbg = Maindb()
        dbg.updatestrings('c20',str(reqstringon),str(reqstringoff))
    return (redirect(url_for('admin')))
dbg.desco()