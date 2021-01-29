#//[This is an Autofile by GMAN]
from flask import render_template,redirect,url_for,request
from services.dbservice import * #Peso=1
from main import app
dbg = Maindb() #Peso=2

@app.route('/c1on')
def c1on():
    DBG = Maindb()
    DBG.updateval('c1','1')
    GETDBG = DBG.readall()
    string = GETDBG[0][7] #//i0C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c1off')
def c1off():
    DBG = Maindb()
    DBG.updateval('c1','0')
    GETDBG = DBG.readall()
    string = GETDBG[0][8] #//i0C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c2on')
def c2on():
    DBG = Maindb()
    DBG.updateval('c2','1')
    GETDBG = DBG.readall()
    string = GETDBG[1][7] #//i1C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c2off')
def c2off():
    DBG = Maindb()
    DBG.updateval('c2','0')
    GETDBG = DBG.readall()
    string = GETDBG[1][8] #//i1C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c3on')
def c3on():
    DBG = Maindb()
    DBG.updateval('c3','1')
    GETDBG = DBG.readall()
    string = GETDBG[2][7] #//i2C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c3off')
def c3off():
    DBG = Maindb()
    DBG.updateval('c3','0')
    GETDBG = DBG.readall()
    string = GETDBG[2][8] #//i2C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c4on')
def c4on():
    DBG = Maindb()
    DBG.updateval('c4','1')
    GETDBG = DBG.readall()
    string = GETDBG[3][7] #//i3C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c4off')
def c4off():
    DBG = Maindb()
    DBG.updateval('c4','0')
    GETDBG = DBG.readall()
    string = GETDBG[3][8] #//i3C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c5on')
def c5on():
    DBG = Maindb()
    DBG.updateval('c5','1')
    GETDBG = DBG.readall()
    string = GETDBG[4][7] #//i4C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c5off')
def c5off():
    DBG = Maindb()
    DBG.updateval('c5','0')
    GETDBG = DBG.readall()
    string = GETDBG[4][8] #//i4C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c6on')
def c6on():
    DBG = Maindb()
    DBG.updateval('c6','1')
    GETDBG = DBG.readall()
    string = GETDBG[5][7] #//i5C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c6off')
def c6off():
    DBG = Maindb()
    DBG.updateval('c6','0')
    GETDBG = DBG.readall()
    string = GETDBG[5][8] #//i5C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c7on')
def c7on():
    DBG = Maindb()
    DBG.updateval('c7','1')
    GETDBG = DBG.readall()
    string = GETDBG[6][7] #//i6C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c7off')
def c7off():
    DBG = Maindb()
    DBG.updateval('c7','0')
    GETDBG = DBG.readall()
    string = GETDBG[6][8] #//i6C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c8on')
def c8on():
    DBG = Maindb()
    DBG.updateval('c8','1')
    GETDBG = DBG.readall()
    string = GETDBG[7][7] #//i7C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c8off')
def c8off():
    DBG = Maindb()
    DBG.updateval('c8','0')
    GETDBG = DBG.readall()
    string = GETDBG[7][8] #//i7C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c9on')
def c9on():
    DBG = Maindb()
    DBG.updateval('c9','1')
    GETDBG = DBG.readall()
    string = GETDBG[8][7] #//i8C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c9off')
def c9off():
    DBG = Maindb()
    DBG.updateval('c9','0')
    GETDBG = DBG.readall()
    string = GETDBG[8][8] #//i8C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

@app.route('/c10on')
def c10on():
    DBG = Maindb()
    DBG.updateval('c10','1')
    GETDBG = DBG.readall()
    string = GETDBG[9][7] #//i9C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)
@app.route('/c10off')
def c10off():
    DBG = Maindb()
    DBG.updateval('c10','0')
    GETDBG = DBG.readall()
    string = GETDBG[9][8] #//i9C7
    print('[HEX] '+ str(string))
    return render_template('index.html',getdb=GETDBG)

dbg.desco()