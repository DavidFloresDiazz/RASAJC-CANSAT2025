Hola y muchas gracias por acceder al repositorio de nuestro proyecto en la competicion de CANSAT realizada por la ESA.
En este archivo explicaremos un poco más detalladamente la parte del codigo que no pudimos poner por falta de espacio en
el informe entregado en la competición regional y explicaremos nuestra mision secundaria. Nuestra mision secundaria es
poder lograr la estimacion de el riesgo de incendio. Esto lo conseguimos gracias a fotos tomadas en una mini camara
con una SD de 32GB dentro de ella y un codigo diseñado Carlos Casas Bueno que nos estima el indice de riesgo del combstible
fino muerto. La parte de las imaganes es relativamente sencilla, nosotros antes de que suba el CANSAT al aire encendemos la
camara en modo de video y despues del aterrizaje y extraccion de este conseguimos el video que extraemos gracias a un lector
usb de la tarjeta SD. Despues en el programa gratuito VLC, sacamos fotogramas en formato .TIFF que pasamos por un codigo en 
Python diseñado por David Flores Diaz el cual solo se puede ejecutar dentro de la consola de Python de QGIS ya que utiliza 
extensiones de este programa. Este codigo resumidamente lo que hace este ahorrarnos el proceso de poner el NExG, que nos 
devolveria una imagen una escala de grises especifica. A esto le ponemos una paleta especifica llamada RdYlGn que va de rojo 
a verde. Y finalmente activaremos el histograma para marcar mas la diferencia de colores. Todo esto dentro del programa QGIS. 
Nuesto plan a futuro seria que todo este aparte de estar totalmente automatizado, es que gracias a una red neuronal entrenada
y programada por nosotros nos saque un csv o un txt con analisis de datos ya hecho (EJEMPLO: Le metemos como input a la red 
neuronal la imagen y el indice de combustible de fino muerto, explicado a continucaion, y nos daria, un texto que explique 
los datos y lo haga poniendo y referenciando oartes de fotogramas exactos. Esto sujeto a cambios). La segunda parte de nuestra 
mision secundaria (el indice de combustible fino muerto) funciona de la siguiente manera. Basado en el documento de el Ministerio 
de Medio Ambiente sobre este indice y sacamos unos valores dependiendo de lahora del dia, mes, exposicion y orientacion del lugar. 
Esto sumado a unos calculos, los cuales son muy largos para este documento, nos dan ese indice. A continucaion pasare a explicar 
cada codigo más detalladamente, el unico codigo que no puedo poner es el de QGIS por el hecho de que solo se puede utilizar ahi.
Muchas Gracias por apoyar nuestro proyecto.


EXPLICACION "cansat.py"

Lo primero que el programa cansat.py es preguntarte "¿Que quieres hacer?", para indicar
lo que queremos hacer definimos unas funciones las cuales son las siguientes

La primera es "graphs" para graficar altitud, temperatua, presion y humedad en base al 
tiempo (counter, que sabemos que tarda exactamente un segundo en llegar es decir if counter == 1: seg = 1) 

La segunda es "graphs_height" nos devuelve un grafica de la altura detectada por el MKR GPS y una que calcula la altitud
gracias a una formula. Obviamente esto no es exacto y lo comparamos con estas graficas. 

La funcion "txt_to_csv" nos pide ruta de input y output para pasar un archivo txt a csv. La funcion fireindex nos permite
calcular el indice de combustible fino muerto mediante la hora, exposicion y pendiente del lugar. 

Y la ultima funcion es "help" que muestra los comandos/funciones explicados brevemente.

Todas estas funciones estan basadas en la utilizacion de un archivo txt/csv. 
Aunque en el futuro pretendemos que esto no sea asi y mediante un plugin de Python llamado PySerial, 
lo leriamos en tiempo real permitiendonos hacer graficas en tiempo real y ver "in situ" lo que pasa.

EXPLICACION "graphs.py"

Este codigo separa el txt/csv en varias partes para después graficarlas despues con la extension de Python Matplotlib
Logrando las graficas necesarias para visualizar los datos. Como en el otro archivo, esperamos en un futuro no muy lejano
mejorar este codigo para que sea en tiempo real
