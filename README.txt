EXPLICACION "cansat.py"

Lo primero que el programa cansat.py es preguntarte "¿Que quieres hacer?", para indicar
lo que queremos hacer definimos unas funciones las cuales son las siguientes

La primera es "graphs" para graficar altitud, temperatua, presion y humedad en base al 
tiempo (counter, que sabemos que tarda exactamente un segundo en llegar es decir if counter == 1: seg = 1) 

La segunda es "graphs_height" nos devuelve un grafica de la altura detectada por el MKR GPS y una que calcula la altitud gracias a una formula. Obviamente esto no es exacto y lo comparamos con estas graficas. 

La funcion "txt_to_csv" nos pide ruta de input y output para pasar un archivo txt a csv. La funcion fireindex nos permite calcular el indice de combustible fino muerto mediante la hora, exposicion y pendiente del lugar. 

Y la ultima funcion es "help" que muestra los comandos/funciones explicados brevemente.

Todas estas funciones estan basadas en la utilizacion de un archivo txt/csv. 
Aunque en el futuro pretendemos que esto no sea asi y mediante un plugin de Python llamado PySerial, 
lo leriamos en tiempo real permitiendonos hacer graficas en tiempo real y ver "in situ" lo que pasa.
