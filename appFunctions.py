import os
import customtkinter as ctk 
import tkinter as tk
import mysql.connector
import os.path as path
from tkinter import messagebox
import pandas as pd
import csv
import math
import matplotlib.pyplot as plt
from time import strftime
import numpy as np
import os
import cv2
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def take_data_from_server(year, mnth, day):
    
    #Comparacion de datos ya descargados del servidor y creación del directorio en el caso de no existir

    ruta_archivo = str(os.path.dirname(__file__))
    ruta_archivo2 = ruta_archivo.replace("\\","/")
    ruta_archivo3 = ruta_archivo2.replace("c","C")

    selected_date = day + "_" + mnth + "_" + year
    path_file = ruta_archivo3 + "/data/datos" + selected_date + ".txt"
    path_file2 = ruta_archivo3 + "/data"


    if (os.path.exists(path_file2) == True):
        pass
    else:
        os.mkdir(ruta_archivo3 + "/data")

    # Conección a MySQL

    conexion = mysql.connector.connect(user='remoto', password="",
                                   host='IESEscorialSQL.ddns.me',
                                   database='data',
                                   port='3306')



    cursor = conexion.cursor()

    #Descarga de datos desde el servidor

    try:
        cursor.execute("SELECT * FROM rasajc_data" + selected_date + ";")
        list1 = cursor.fetchall()
        

        if path.exists(path_file):
            os.remove(path_file)
            with open(path_file , "x") as file:
                pass
            

        with open(path_file, "w") as file1:
            for x, y, z, a, b, c, d, e, f in list1:
                list2 = (str(x) + "," + str(y) + "," + str(z) + "," +  str(a) + "," +  str(b) + "," +  str(c) + "," +  str(d) + "," +  str(e) + "," +  str(f))
                file1.write(list2 + "\n")
    
        conexion.commit()
        conexion.close()
    except mysql.connector.errors.ProgrammingError:
        messagebox.showerror(title="Error during colecting data", message="Los datos para esa fecha no existe")
    except:
        messagebox.showerror(title="Error during colecting data", message="Un error ocurrió al descargar los datos")


def graphs(year, mnth, day, checkbox_temp, checkbox_alt, checkbox_prss, checkbox_hum, checkbox_calcalt, checkbox_calccd, checkbox_v): 
    
    ruta_archivo = str(os.path.dirname(__file__))
    ruta_archivo2 = ruta_archivo.replace("\\","/")
    ruta_archivo3 = ruta_archivo2.replace("c","C") 


    selected_date = day + "_" + mnth + "_" + year
    path_file = ruta_archivo3 + "/data/datos" + selected_date + ".txt"

    take_data_from_server(year, mnth, day)
    
    # Declaración de Constantes para las formulas 
    
    P0 = 101.325
    M = 0.029
    g = 9.81
    R = 8.314  
    h = []
    v = []
    cd = []
    hgps = []
    difh = 0
    p = []
    h__gps = []
    tmplist = []

    mCansat = 0.3
    
    df = pd.read_csv(path_file, delimiter=",", decimal=".")
    altitude = df.iloc[0:999999,7]
    humidity = df.iloc[0:999999, 3]
    counter = 0
    counter2 = 0 
    sum_v = 0
    sum_cd = 0
    sum_h = 0
    sumt_cd = 0 
    h_ant = 0
    v_h = 0

    """ Fila 0 --> Counter ; Fila 1 --> Temperatura (Cº) ; Fila 2 --> Presión (kPa) ;  
        Fila 3 --> Humedad (%) ; Fila 4 --> Luminosidad ; Fila 5 --> Latitud (º) ; 
        Fila 6 --> Longitud (º) ; Fila 7 --> Altura (m) ; Fila 8 --> Velocidad (km/h) ;
        Fila 9 --> Nº de Satelites
    """

    # Abrir archivo descargado desde el servidor para recolectar datos (Archivo con formato CSV)

    with open(path_file, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        df = pd.read_csv(path_file, delimiter=",", decimal=".")
        h_gps = df.iloc[0:999999,7]
        v_gps = df.iloc[0:999999,8]    
        for fila in csvreader: 
            P = float(fila[2])
            p.append(P)
            h_gps = float(fila[7])
            v_gps = float(fila[8])
            temperature = float(fila[1])+273.15
            # Filtro De La Velocidad del GPS y del CD para evitar errores

            if (v_gps >= 18.5):
                v_gps = v_gps * 0.277
                Cd = (2*mCansat*g)/((v_gps**2)*0.12*1.2)
            else:
                v_gps = 0
                Cd = 0

            # Calculamos la Temp. y la Altura Mediante la Fórmula Barométrica
 
            Formula_height = -1 * ((R*293.15*math.log(P/P0))/(M*g))
            

            vh = (h_ant - h_gps)/ 0.5

            h_ant = h_gps

            if (vh < 0):
                counter2 += 1
                vh = -1*vh
                v_h += vh
            else: 
                pass

            # Guardamos datos
            tmplist.append(temperature)
            hgps.append(h_gps)
            h__gps.append(h_gps)
            h.append(Formula_height) 
            cd.append(Cd)
            v.append(v_gps)
            counter += 1
            sum_h += h_gps
            sum_v += v_gps
            sum_cd += Cd
            difh += h_gps - Formula_height
        #Calculos del Desv. Tipica del CD, Velocidad y la Altura
        
        dif_vh = v_h / counter2
        difh_media = difh / counter
        media_cd = sum_cd / counter
        sumt_cd = sum((item - media_cd) ** 2 for item in cd)
        desv_cd = math.sqrt((1/counter)*sumt_cd)

        messagebox.showinfo(title="Cálculos Numéricos", message=f"Media Dif. h (GPS) - h (Calc.): {difh_media:.2f} m \nMedia Velocidad: {dif_vh:.2f} m/s \nDesv. Cd: {desv_cd:.2f}")


    # Graficamos


    if (checkbox_temp == "on"):
        plt.plot(tmplist, label="Temperature (k)")
    if (checkbox_alt == "on"):
        plt.plot(altitude, label="Altitude (m)")
    if (checkbox_prss == "on"):
        plt.plot(p, label="Pressure (HPa)")
    if (checkbox_hum == "on"):
        plt.plot(humidity, label="Humidity (%)")
    if (checkbox_calcalt == "on"):
        plt.plot(h, label="Calc. Altitude (m)")
    if (checkbox_calccd == "on"):
        plt.plot(cd, label="Coeficiente de Sustentación")
    if (checkbox_v == "on"):
        plt.plot(v, label="Speed (m/s)")
    

    plt.legend(loc = "upper right")

    plt.xlabel("Tiempo (s)")
    plt.ylabel('Eje Y')
    plt.title("Gráficas")
    plt.show()
    
    
def fireindex(year, mnth, day, orient, expos):
    
    #Declaracion de listas y directorios para guardar los datos

    templst = []
    hdtylst = []

    ruta_archivo = str(os.path.dirname(__file__))
    ruta_archivo2 = ruta_archivo.replace("\\","/")
    ruta_archivo3 = ruta_archivo2.replace("c","C")
    
    selected_date = day + "_" + mnth + "_" + year
    path_file = ruta_archivo3 + "/data/datos" + selected_date + ".txt"
    
    
    take_data_from_server(year, mnth, day)
    
    # Tabla de la humedad del combustible fino muerto del INIA

    hcom = [
	[1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9, 9, 10, 11, 12, 12, 13, 13, 14],
	[1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8, 9, 9, 10, 10, 11, 12, 13, 13, 13],
	[1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9,  9, 10, 11, 12, 12, 12, 13],
	[1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8,  9, 10, 10, 11, 12, 12, 13],
	[1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8,  9, 10, 10, 11, 12, 12, 13],
	[1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 8, 8,  9, 10, 10, 11, 12, 12, 12]
    ]
    hcom2 = [
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11, 11, 12, 13, 14, 16, 18, 21, 24, 25, 25],
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 11, 11, 12, 13, 14, 16, 18, 21, 24, 25, 25],
	[1, 2, 3, 4, 5, 6, 6, 8, 8, 9, 10, 11, 11, 12, 14, 16, 17, 20, 23, 25, 25],
	[1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 15, 17, 20, 23, 25, 25],
	[1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10, 10, 11, 13, 14, 16, 19, 22, 25, 25],
	[1, 2, 2, 3, 4, 5, 6, 8, 9, 8, 9, 9, 10, 11, 12, 14, 16, 19, 21, 24, 25]
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

    # Utilizacion de las tablas del INIA para sacar el riesgo de incencio mediante la temp, humd, expos y orient. 

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


    with open(path_file, 'rt') as f:
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


    if (orient == "S" ):
        ortn = "S"
    if (orient == "N" ):
        ortn = "N"
    if (orient == "E" ):
        ortn = "E"
    if (orient == "O" ):
        ortn = "O"
    
    if (expos == "E0" ):
        exps = "E0"
    if (expos == "E1" ):
        exps = "E1"
    if (expos == "SS" ):
        exps = "SS"


    mnth = strftime('%m')
    hour = strftime('%H')
    hour2 = str(hour) 

    #Checks if we use the 8-20 Table or the 20-8 Table
    if (hour2 == "20") or (hour2 == "21") or (hour2 == "22") or (hour2 == "23") or (hour2 == "00") or (hour2 == "01") or (hour2 == "02") or (hour2 == "03") or (hour2 == "04") or (hour2 == "05") or (hour2 == "06") or (hour2 == "07"):
        c = hcom2[T][H]
    
    else:
        m = dcor['moth'][mnth]
        o = dcor['ortn'][ortn]
        e = dcor['exps'][exps]
        h = int((int(hour)-8)/2)
        c = hcom[T][H] + ccor[m][o][e][h]

    tk.messagebox.showinfo(title="Humedad del Combustible Fino Muerto", message="Humedad del Combustible Fino Muerto: " + str(c))


def abrirarchivo(ruta_input):
    file = ctk.filedialog.askopenfilename(initialdir="/", title="Seleccione el archivo de entrada", filetypes= (("Archivos txt","*.txt"),("Archivos csv","*.csv"),("All files","*.*")))
    ruta_input.set(file) 



def abrirarchivooutput(ruta_output):
    file = ctk.filedialog.askdirectory(initialdir="/", title="Seleccione el archivo de salida")
    ruta_output.set(file)


def calculate_plague_percentage(image_path, year, mnth, day):
    
    ruta_archivo = str(os.path.dirname(__file__))
    ruta_archivo2 = ruta_archivo.replace("\\","/")
    ruta_archivo3 = ruta_archivo2.replace("c","C") 
    
    selected_date = day + "_" + mnth + "_" + year
    path_file = ruta_archivo3 + "/data/datos" + selected_date + ".txt"

    take_data_from_server(year, mnth, day)
    
    counter = 0
    sum_humd = 0
    sum_temp = 0
    sum_lum = 0

    with open(path_file, newline='') as csvfile:
        # Crea un lector CSV
        csvreader = csv.reader(csvfile)
        df = pd.read_csv(path_file, delimiter=",", decimal=".") 
    # Itera sobre cada fila en el archivo CSV
        for fila in csvreader:
        # Obtiene el valor de la columna específica y hace la 
            humd = float(fila[3])
            temp = float(fila[1])
            lum = float(fila[4])
            counter += 1
            sum_humd += humd
            sum_temp += temp
            sum_lum += lum

    media_humd = sum_humd / counter 
    media_temp = sum_temp / counter
    media_lum = sum_lum / counter


    image = cv2.imread(image_path)
    
    height, width = image.shape[:2]  
    total_pixels = height * width
    
    if image is None:
        messagebox.showerror(title="File Error", message="No se pudo leer el archivo")
        return

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    imageHSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    middle = np.array([30, 62, 99])  
    red = np.array([3, 82, 84])      

    if middle[0] > red[0]:
        mask1 = cv2.inRange(imageHSV, middle, np.array([179, 255, 255]))
        mask2 = cv2.inRange(imageHSV, np.array([0, 62, 99]), red)
        maskmid2red = cv2.bitwise_or(mask1, mask2)
    else:
        maskmid2red = cv2.inRange(imageHSV, middle, red)


    affctd_area = cv2.countNonZero(maskmid2red)

    affctd_area = total_pixels - affctd_area 

    res = cv2.bitwise_or(image, image, mask=maskmid2red)

    mask_black = np.all(res == [0, 0, 0], axis=-1)
    res[mask_black] = [255, 0, 0]  
    res[~mask_black] = [0, 255, 0]  


    plague_percentage = (affctd_area / total_pixels * 100) if total_pixels > 0 else 0.0



    #Identificación de Plaguas

    """
    Identifica la plaga comparando los valores promedio de temperatura, humedad y luminosidad
    con condiciones esperadas para cada plaga. Se calcula una métrica de error relativa y se
    selecciona la plaga cuyo perfil esperado tenga menor diferencia porcentual.
   
    Los valores esperados se basan en investigaciones generales:
      - Mildiu:  Temp ~18°C,  Humedad ~90%,  Luminosidad ~150 (condiciones húmedas y baja luz)
      - Oidio:   Temp ~23°C,  Humedad ~55%,  Luminosidad ~350 (condiciones moderadas)
      - Araña Roja: Temp ~30°C,  Humedad ~40%,  Luminosidad ~600 (calor, sequedad y alta luz)
      - Mosca Blanca: Temp ~25°C,  Humedad ~65%,  Luminosidad ~600 (condiciones cálidas y luminosas)
      - Botrytis (Moho gris): Temp ~17°C,  Humedad ~95%,  Luminosidad ~150 (muy alta humedad y baja luz)
    """
    plagas = {
         "Mildiu": {"temp": 18, "hum": 90, "lum": 150},
         "Oidio": {"temp": 23, "hum": 55, "lum": 350},
         "Araña Roja": {"temp": 30, "hum": 40, "lum": 600},
         "Mosca Blanca": {"temp": 25, "hum": 65, "lum": 600},
         "Botrytis (Moho gris)": {"temp": 17, "hum": 95, "lum": 150}
    }
    best_plague = None
    best_error = float("inf")
    for plague, expected in plagas.items():
        error = abs(temp - expected["temp"]) / expected["temp"] \
              + abs(humd - expected["hum"]) / expected["hum"] \
              + abs(lum - expected["lum"]) / expected["lum"]
        if error < best_error:
            best_error = error
            best_plague = plague
    
    messagebox.showinfo(title="Plague Porcentage", message=f"Porcentaje de plaga en la imagen es de: {plague_percentage:.2f}%. El tipo de plaga es {best_plague}")

    plt.imshow(res)
    plt.axis('off')
    plt.show()