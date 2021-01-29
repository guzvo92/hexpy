import os #para crear el salto de linea


#############################    funciones file makers  ########################################
#para una estructura de 50 registros

def creandocircuitos(num,uri):

    file = open(uri, "w") #limpiando archivo
    file.write("" + os.linesep)
    file.close()  #limpiando archivo

    contentimports = "from django.db import models"
    contentimports2 = "from django.utils.timezone import now"
    contentline0 = "class Dbchar"
    contentline1 = "(models.Model):"
    contentline2 = "name = models.CharField(max_length=50)"
    contentline3 = "vocation= models.CharField(max_length=50)"
    contentline4 = "level= models.CharField(max_length=50)"
    contentline5 = "lastlog= models.CharField(max_length=50)"
    contentline6 = "created_at= models.DateTimeField(auto_now_add=True)"

    file = open(uri, "a")
    file.write("" +  contentimports + "" + os.linesep)
    file.write("" +  contentimports2 + "" + os.linesep)
    file.write("\n")

    for x in range(num):

        file.write("" +  contentline0 + "" + str(x))
        file.write("" +  contentline1 + "" + os.linesep)
        file.write("" + "\t"+  contentline2 + "" + os.linesep)
        file.write("" + "\t"+ contentline3 + "" + os.linesep)
        file.write("" + "\t"+ contentline4 + "" + os.linesep)
        file.write("" + "\t"+ contentline5 + "" + os.linesep)
        file.write("" + "\t"+ contentline6 + "" + os.linesep)
        file.write("\n")

    file.close()


def CreaActionRutesFile(num,uri):

    file = open(uri, "w") #crea archivo
    file.close()  #limpiando archivo

    import0 = "#//[This is an Autofile by GMAN]"
    import1 = "from flask import render_template,redirect,url_for,request"
    import2 = "from services.dbservice import * #Peso=1"
    import3 = "from main import app"
    p0 = "dbg = Maindb() #Peso=2"
   
    
    file = open(uri, "a") #append
    
    file.write("" +  import0 + "" + os.linesep)
    file.write("" +  import1 + "" + '\n')
    file.write("" +  import2 + "" + '\n')
    file.write("" +  import3 + "" + os.linesep)
    file.write("" +  p0 + "" + os.linesep)
    file.write("\n")

    for x in range(num):

        #ON_FUNCTION
        file.write("@app.route('/c" + str(x+1) + "on')"+'\n')
        file.write("def c"+ str(x+1) + "on():"+ '\n')
        file.write("    DBG = Maindb()"+ '\n')
        file.write("    DBG.updateval('c" +str(x+1)+ "','1')"+ '\n')
        file.write("    GETDBG = DBG.readall()"+ '\n')
        file.write("    string = GETDBG["+ str(x) +"]"+ "[7] #//i"+str(x)+"C7" '\n')
        file.write("    print('[HEX] '+ str(string))" + '\n')
        file.write("    return render_template('index.html',getdb=GETDBG)")

        file.write( os.linesep)

        #OFF_FUNCTION
        file.write("@app.route('/c" + str(x+1) + "off')"+'\n')
        file.write("def c"+ str(x+1) + "off():"+ '\n')
        file.write("    DBG = Maindb()"+ '\n')
        file.write("    DBG.updateval('c" +str(x+1)+ "','0')"+ '\n')
        file.write("    GETDBG = DBG.readall()"+ '\n')
        file.write("    string = GETDBG["+ str(x) +"]"+ "[8] #//i"+str(x)+"C7" '\n')
        file.write("    print('[HEX] '+ str(string))" + '\n')
        file.write("    return render_template('index.html',getdb=GETDBG)" + '\n')
        
        file.write("\n")

    file.write("dbg.desco()")

    file.close()
