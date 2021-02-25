#//[This is an Autofile by GMAN]
from flask import render_template,redirect,url_for,request
from services.dbservice import * #Peso=1
from services.telnetservice import * #Peso=1
import time
from main import app
from main import constructorconexiontelnet
dbg = Maindb() #Peso=2
def conexiontelnet(argstring):
  if constructorconexiontelnet == 1:
      try:
          print('Conexion activa')
          test = lutronmaster('192.168.10.11','auvit','1234')
          test.conexion()
          test.send(argstring)
          test.endconexion()
      except:
          print('Error en la conexion')
  else: 
     print('Conexion desactivada') 
@app.route('/c1on')
def c1on():
    DBG = Maindb()
    DBG.updateval('c1','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[0][8] #//i0C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[0][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c1off')
def c1off():
    DBG = Maindb()
    DBG.updateval('c1','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[0][9] #//i0C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[0][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c2on')
def c2on():
    DBG = Maindb()
    DBG.updateval('c2','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[1][8] #//i1C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[1][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c2off')
def c2off():
    DBG = Maindb()
    DBG.updateval('c2','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[1][9] #//i1C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[1][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c3on')
def c3on():
    DBG = Maindb()
    DBG.updateval('c3','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[2][8] #//i2C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[2][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c3off')
def c3off():
    DBG = Maindb()
    DBG.updateval('c3','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[2][9] #//i2C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[2][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c4on')
def c4on():
    DBG = Maindb()
    DBG.updateval('c4','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[3][8] #//i3C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[3][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c4off')
def c4off():
    DBG = Maindb()
    DBG.updateval('c4','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[3][9] #//i3C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[3][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c5on')
def c5on():
    DBG = Maindb()
    DBG.updateval('c5','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[4][8] #//i4C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[4][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c5off')
def c5off():
    DBG = Maindb()
    DBG.updateval('c5','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[4][9] #//i4C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[4][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c6on')
def c6on():
    DBG = Maindb()
    DBG.updateval('c6','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[5][8] #//i5C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[5][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c6off')
def c6off():
    DBG = Maindb()
    DBG.updateval('c6','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[5][9] #//i5C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[5][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c7on')
def c7on():
    DBG = Maindb()
    DBG.updateval('c7','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[6][8] #//i6C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[6][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c7off')
def c7off():
    DBG = Maindb()
    DBG.updateval('c7','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[6][9] #//i6C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[6][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c8on')
def c8on():
    DBG = Maindb()
    DBG.updateval('c8','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[7][8] #//i7C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[7][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c8off')
def c8off():
    DBG = Maindb()
    DBG.updateval('c8','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[7][9] #//i7C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[7][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c9on')
def c9on():
    DBG = Maindb()
    DBG.updateval('c9','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[8][8] #//i8C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[8][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c9off')
def c9off():
    DBG = Maindb()
    DBG.updateval('c9','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[8][9] #//i8C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[8][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c10on')
def c10on():
    DBG = Maindb()
    DBG.updateval('c10','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[9][8] #//i9C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[9][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c10off')
def c10off():
    DBG = Maindb()
    DBG.updateval('c10','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[9][9] #//i9C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[9][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c11on')
def c11on():
    DBG = Maindb()
    DBG.updateval('c11','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[10][8] #//i10C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[10][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c11off')
def c11off():
    DBG = Maindb()
    DBG.updateval('c11','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[10][9] #//i10C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[10][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c12on')
def c12on():
    DBG = Maindb()
    DBG.updateval('c12','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[11][8] #//i11C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[11][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c12off')
def c12off():
    DBG = Maindb()
    DBG.updateval('c12','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[11][9] #//i11C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[11][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c13on')
def c13on():
    DBG = Maindb()
    DBG.updateval('c13','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[12][8] #//i12C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[12][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c13off')
def c13off():
    DBG = Maindb()
    DBG.updateval('c13','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[12][9] #//i12C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[12][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c14on')
def c14on():
    DBG = Maindb()
    DBG.updateval('c14','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[13][8] #//i13C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[13][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c14off')
def c14off():
    DBG = Maindb()
    DBG.updateval('c14','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[13][9] #//i13C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[13][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c15on')
def c15on():
    DBG = Maindb()
    DBG.updateval('c15','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[14][8] #//i14C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[14][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c15off')
def c15off():
    DBG = Maindb()
    DBG.updateval('c15','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[14][9] #//i14C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[14][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c16on')
def c16on():
    DBG = Maindb()
    DBG.updateval('c16','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[15][8] #//i15C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[15][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c16off')
def c16off():
    DBG = Maindb()
    DBG.updateval('c16','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[15][9] #//i15C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[15][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c17on')
def c17on():
    DBG = Maindb()
    DBG.updateval('c17','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[16][8] #//i16C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[16][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c17off')
def c17off():
    DBG = Maindb()
    DBG.updateval('c17','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[16][9] #//i16C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[16][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c18on')
def c18on():
    DBG = Maindb()
    DBG.updateval('c18','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[17][8] #//i17C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[17][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c18off')
def c18off():
    DBG = Maindb()
    DBG.updateval('c18','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[17][9] #//i17C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[17][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c19on')
def c19on():
    DBG = Maindb()
    DBG.updateval('c19','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[18][8] #//i18C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[18][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c19off')
def c19off():
    DBG = Maindb()
    DBG.updateval('c19','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[18][9] #//i18C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[18][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

@app.route('/c20on')
def c20on():
    DBG = Maindb()
    DBG.updateval('c20','1')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[19][8] #//i19C7
    print('[HEX] '+ str(string))
    stringon = GETDBG[19][8] #//i0C8
    conexiontelnet(stringon)
    return render_template('index.html',getdb=GETDBG)
@app.route('/c20off')
def c20off():
    DBG = Maindb()
    DBG.updateval('c20','0')
    GETDBG = DBG.readallcircuitos()
    string = GETDBG[19][9] #//i19C7
    print('[HEX] '+ str(string))
    stringoff = GETDBG[19][9] #//i0C8
    conexiontelnet(stringoff)
    return render_template('index.html',getdb=GETDBG)

dbg.desco()