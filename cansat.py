# importing panda library 
import csv
import matplotlib
import pandas as pd 
import matplotlib.pyplot as plt
import math 
#! /usr/bin/python3
from time import strftime


templst = []
hdtylst = []


def txt_to_csv():
# readinag given csv file 
# and creating dataframe 
    inp = pd.read_csv(inpu) 
# storing this dataframe in a csv file 
    inp.to_csv(output,  
                    index = None)
    return print("Exito al hacer la tarea")


def graph_calculatedheight_gpsheight():
    P0 = 1013.25 
    M = 0.029
    g = 9.81
    R = 8.314
    T = 288.15
    h = []

# Define la columna específica que deseas convertir a float (0-indexada)
    columna_a_convertir = 2  # Por ejemplo, convierte la segunda columna
    columna_gps = 7
# Lista para almacenar los valores convertidos a float
    archivo = input("Introduzca el archivo de Datos: ")
# Abre el archivo CSV en modo de lectura
    with open(archivo, newline='') as csvfile:
        # Crea un lector CSV
        csvreader = csv.reader(csvfile)
        df = pd.read_csv(archivo, delimiter=",", decimal=".")
        h_gps = df.iloc[0:999999,7]    
    # Itera sobre cada fila en el archivo CSV
        for fila in csvreader:
        # Obtiene el valor de la columna específica y hace la 
            media = []
            valor = float(fila[columna_a_convertir])*10
            P = valor
            Formula = -1 * ((R*T)/(M*g)*math.log((P/P0)))
            h.append(Formula) 

#Generamos una grafica lineal para una recta en X
#plt.plot(y, label='Counter')
    plt.plot(h_gps, label= "Altura GPS")
    #plt.plot(media,label="Altura sacada con las medias entre las dos")
    plt.plot(h, label="Altura Calculada")
#Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title("Comparación de Alturas")
    plt.legend()
    plt.savefig('Alturas comparadas.png')
    plt.show()


def graphs():   

    archivo = input("Introduzca la ruta del archivo: ")
    df = pd.read_csv(archivo, delimiter=",", decimal=".")
    altitude = df.iloc[0:9999,7]
    temperature = df.iloc[0:9999,1]
    pressure = df.iloc[0:9999, 2]
    humidity = df.iloc[0:9999, 3]
#Generamos una grafica lineal para una recta en X
#plt.plot(y, label='Counter')
    plt.plot(temperature, label="Temperature")
    plt.plot(altitude, label="Altitude")
    plt.plot(pressure, label="Pressure")
    plt.plot(humidity, label="Humidity")
#Agregamos las etiquetas y añadimos una leyenda.
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title("Simple Plot")
    plt.legend()
    plt.savefig('grafica_lineal.png')
    plt.show()
    return print("Graficas hechas correctamente")

def fireindex():
    hcom = [
	[1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9, 9, 10, 11, 12, 12, 13, 13, 14],
	[1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9, 10, 10, 11, 12, 13, 13, 13],
	[1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9,  9, 10, 11, 12, 12, 12, 13],
	[1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8,  9, 10, 10, 11, 12, 12, 13],
	[1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8,  9, 10, 10, 11, 12, 12, 13],
	[1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8,  9, 10, 10, 11, 12, 12, 12]
    ]
    ccor = [
	    [
		    [ [3, 1, 0, 0, 1, 3], [4, 2, 1, 1, 2, 4], [5, 4, 3, 3, 4, 5] ],
	    	[ [2, 1, 0, 0, 1, 4], [2, 0, 0, 1, 3, 5], [4, 4, 3, 4, 4, 5] ],
	    	[ [3, 1, 0, 0, 1, 3], [3, 1, 1, 1, 1, 3], [4, 4, 3, 3, 4, 5] ],
	    	[ [3, 1, 0, 0, 1, 3], [5, 3, 1, 0, 0, 2], [5, 4, 3, 3, 4, 4] ]
    	], # may, jun, jul
	    [
		    [ [4, 2, 1, 1, 2, 4], [4, 3, 3, 3, 3, 4], [5, 5, 4, 4, 5, 5] ],
	    	[ [4, 2, 1, 1, 2, 4], [3, 1, 1, 2, 4, 5], [5, 4, 4, 4, 5, 5] ],
	    	[ [4, 2, 1, 1, 2, 4], [4, 2, 1, 1, 2, 4], [5, 4, 4, 4, 4, 5] ],
	    	[ [4, 2, 1, 1, 2, 4], [5, 4, 2, 1, 1, 3], [5, 5, 4, 4, 4, 5] ]
    	], # feb, mar, apr, aug, sep, oct
	    [
		    [ [5, 4, 3, 3, 4, 5], [5, 5, 5, 5, 5, 5], [5, 5, 5, 5, 5, 5] ],
	    	[ [5, 4, 3, 3, 4, 5], [5, 4, 3, 2, 5, 5], [5, 5, 5, 5, 5, 5] ],
	    	[ [5, 4, 3, 2, 4, 5], [5, 3, 1, 1, 3, 5], [5, 5, 5, 5, 5, 5] ],
	    	[ [5, 4, 3, 3, 4, 5], [5, 5, 4, 2, 3, 5], [5, 5, 5, 5, 5, 5] ]
    	]  # nov, dec, jan
    ]

    dcom = {
	    'temp': { '<0':0, '<9':1, '<20':2, '<31':3, '<42':4, '>42':5 },
	    'hrel': {}
    } # Distribution of different variables inside of the fuel humidity table.

    dcor = {
	    'moth': { '01':2, '02':1, '03':1, '04':1, '05':0, '06':0,
		    	'07':0, '08':1, '09':1, '10':1, '11':2, '12':2 }, # %m
	    'ortn': { 'N':0, 'E':1, 'S':2, 'O':3, None:2 },
	    'exps': { 'E0':0, 'E1':1, 'SS':2 },
	    'hour': {  } # (hour-8)/2, # %H
    } # Distribution of different variables inside of the table corrector table.


    with open( input('\n--> file:   '), 'rt') as f:
        data = f.readlines()
    for i in data:
            i = i.split(',')
            templst.append(i[1])
            hdtylst.append(i[3])

    tm = 0
    for i in templst:
        tm += float(i)
    tm /= len(templst)
	
    hm = 0
    for i in hdtylst:
        hm += float(i)
    hm /= len(hdtylst)

    H = int( hm//5 )
    T = tm
    if T < 0: T = 0
    elif T < 9: T = 1
    elif T < 20: T = 2
    elif T < 31: T = 3
    elif T < 42: T = 4
    else: T = 5

    ortn = input('\n--> ortn :   ').upper()
    exps = input('\n--> exps :   ').upper()
    mnth = strftime('%m')
    hour = strftime('%H')

    m = dcor['moth'][mnth]
    o = dcor['ortn'][ortn]
    e = dcor['exps'][exps]
    h = int(( int(strftime('%H'))-8)/2)

    c = hcom[T][H] + ccor[m][o][e][h]

    return print( '\n\nEl índice de riesgo que presenta el combustible fino muerto es ' + str(c) + '\n\n' )
    




b = 1
while b == 1:
    a = input("Que quieres hacer: ")
    if (a ==  "txt_to_csv"): 
        inpu = (input("Introduzca la ruta del input: "))
        output = (input("Introduzca la ruta del output: "))
        txt_to_csv()
    elif (a == "exit"):
        break
    elif (a == "graph_height"):
        graph_calculatedheight_gpsheight()
    elif (a == "fireindex"):
         fireindex()
    elif (a == "help"):
        print("COMANDOS\n\ntxt_to_csv --> Converts a txt file into a csv file\ngraph_height --> Shows up a graph of the height calculated depending on the pressure anthe height detected by the GPS\nfireindex --> Calculates a general humidity index of the plants based on the hour, the slope and the humidity\nexit --> Exits the program\ngraphs --> Shows graphs of the temperatura, pressure, humidity and altitude\n")
    elif (a == "graphs"):
        graphs()
    else:
        print("Función Desconocida")
