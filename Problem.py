from ast import Continue #importar continue(pasa al siguiente código) de la libreria ast

def delfecha(mensaje, fecha, veces): #crear una función
    mensaje = f.readline() #mensaje = 1r elemento de message.txt
    mensaje = mensaje.split("/" ,) #separamos las fechas por dia - mes - año segun "/"
    mensaje.pop(0) #eliminamios el 1r elemnto(dia)  (nos queda mes-año)
    mensaje = '/'.join(mensaje)#juntamos el mes y año a partir de una barra(/)
    #el proceso seria por ejemplo: "12/02/2021" --> "12" , "02", "2021" --> "02", "2021" --> "02/2021"
    try:
        mensaje = mensaje.split("\n") #lo utilizamos para quitar el salto de linea, lo ponemos en un try para que no nos de error en la ultima linea del .txt file
        mensaje.pop(-1)# eliminamos el \n que hemos separado que nos ha quedado como: ""
    except:
        Continue # no error mensaje en la ultima linea del .txt file
    try:
        ndx = fecha.index(mensaje) #busca en la lista fecha el mensaje, ndx = a la ubicación del mensaje
    except: #en caso de un error(significa que no ha encontrado mensaje en fecha se ejecutara except y ndx será igual a -1
        ndx = -1 
    if ndx == -1: #en caso de no encontrar ninguna coincidencia en las variables crea unas nuevas
        fecha.append(mensaje)
        veces.append(1)
    else:#en caso de que ndx no sea -1 significara que habra encontrado el mensaje de manera que le sumara a veces +1 de manera que habra salido 2 veces o mas
        veces[ndx] += 1


with open("incendios.txt") as mydoc: #abre el mensaje para contar cuantas lineas tiene en total
    totall = sum(1 for linea in mydoc)#miramos cuantas lineas tiene el .txt file
f = open ("incendios.txt","r")#Abre el doc
mensaje = f.readline() #le decimos de leer la primera línea y no hacer nada ya que la primera lína es: "ACQ_DATE"
fecha = [] #Definimos un par de listas para el resultado
veces = []
for n in range(totall - 1): #ejecuta la función delfecha todas las lineas excepto ACQ_DATE
    delfecha(mensaje, fecha, veces)
for n in range(len(fecha)):#imprime el resultado
    print(fecha[n][0] + ";",veces[n])
f.close()#Cerramos el .txt file
input("Presiona cualquier tecla para salir") #Haremos que te pida algo y hasta que no obtenga una respuesta no va a pasar a la siguiente linea, el final