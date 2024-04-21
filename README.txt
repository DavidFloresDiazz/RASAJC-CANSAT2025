Hola y muchas gracias por acceder al repositorio de nuestro proyecto en la competicion de CANSAT realizada por ESERO 
(la sección educativa de la Agencia Espacial Europea-ESA).
En este archivo explicaremos un poco más detalladamente la parte del codigo que no pudimos poner por falta de espacio en
el informe entregado en la competición regional y explicaremos nuestra mision secundaria. Nuestra mision secundaria es
poder lograr la estimacion de el riesgo de incendio. Esto lo conseguimos usando dos métodos que combinados nos dan una estimación 
del riego de incendio muy precisa. 
El primer método es gráfico mediante el ïncide de Exceso de Varde Normalizado(NExV), donde obtenemos el riesgo de incendio visualmente 
gracias gracias a fotos tomadas en una mini camara con una SD de 32GB y el segundo método es obteniendo la humedad del combustible fino muerto
de la zona registrada por la cámara.
Para la realización del primer método, antes del lanzamineto del CANSAT al aire encendemos la
camara en modo de video, para posteriormente, despues del aterrizaje leemos el contenido de la tarjeta mediante un lector 
usb. Después en el programa gratuito VLC, sacamos fotogramas en formato .TIFF que pasamos por un código en 
Python diseñado por el miembro del equipo-David Flores Díaz, algoritmo que ejecutamos dentro de la consola de Python de QGIS puesto que utiliza 
extensiones de este programa. Este código lo que hace es extraernos el NExG de la imagen .tiff, que nos 
devuelve una imagen una escala de grises especifica. A esto le ponemos la paleta cromática de análisis forestal RdYlGn que va de rojo 
a verde. Y finalmente activamos el histograma para marcar más las diferencias de colores. Todo esto dentro del programa QGIS. 
Nuesto plan de futuro es que todo esta aparte esté totalmente automatizado, es que gracias a una red neuronal entrenada
y programada por nosotros nos saque un csv o un txt con analisis de datos ya hecho (EJEMPLO: Le metemos como input a la red 
neuronal la imagen y el indice de combustible de fino muerto, explicado a continución, y nos daria, un texto que explique 
los datos y lo haga poniendo y referenciando partes de fotogramas exactos. 
El segundo método de estimación del riesgo de incendio en la zona objeto de estudio. Nuestro CanSat una vez que aterriza actúa como una sonda midiendo y 
emitiendo en tiempo real datos de Humedad del aire y temperatura a aras de suelo, esos datos son el input de nuestro algoritmo (escrito por otro miembro 
del equipo-Carlos Casas) para estimar la humedad del combustible fino muerto computando los datos a través de los datos ofrecidos por el ministerio 
de medio ambiente y corriginedo los valores dependiendo de la hora del dia, mes, exposicion y orientacion del lugar. Esto sumado a unos calculos, 
los cuales son muy largos para este documento, nos dan ese indice. 
A continucaion pasare a explicar cada codigo más detalladamente.
Muchas Gracias por apoyar nuestro proyecto.


EXPLICACION "cansat.py"

Lo primero que hace el programa cansat.py es preguntarte "¿Que quieres hacer?". Para indicar
lo que queremos hacer definimos unas funciones. Estas son las siguientes:

La primera es "graphs" para graficar altitud, temperatura, presión y humedad en base al 
tiempo (counter, que sabemos que tarda exactamente un segundo en llegar es decir if counter == 1: seg = 1) 

La segunda es "graphs_height" nos devuelve una gráfica de la altura detectada por el MKR GPS (nuestra placa controladora) 
y una que calcula la altitud gracias a una fórmula a partir de los datos obtenidos de presión. El análisis de estos datos constituye la misión primaria
 de nuestro proyecto CanSat. Y lo realizamos tanto numérica como gráficamente. 

La funcion "txt_to_csv" nos pide ruta de input y output para pasar un archivo txt a csv. La funcion fireindex nos permite
calcular el indice de combustible fino muerto mediante la hora, exposicion y pendiente del lugar. 

Y la ultima funcion es "help" que muestra los comandos/funciones explicados brevemente.

Todas estas funciones estan basadas en la utilización de un archivo txt/csv. 
Aunque en el futuro pretendemos que esto no sea asi y mediante un plugin de Python llamado PySerial, 
leeriamos todos los datos en tiempo real permitiéndonos gráficar también en tiempo real y ver "in situ" lo que pasa.
De igual manera se contempla emitir las imágenes de la zon boscosa en remoto mediante un módulo wifi instalado en el satélite
para evitar la extracción de los datos de vídeo del dispositivo.

EXPLICACION "graphs.py"

Este codigo separa el txt/csv en varias partes para después graficarlas con la extension de Python Matplotlib,
logrando así, las gráficas necesarias para visualizar los datos. Como en el otro archivo, esperamos en un futuro no muy lejano
mejorar este código para que sea en tiempo real.
