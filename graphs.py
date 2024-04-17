#! /usr/bin/python3

import matplotlib.pyplot as plt
from numpy import arange

timelst = []
hghtlst = []
templst = []
prsslst = []
hdtylst = []
lghtlst = []
latlist = []
lonlist = []
spdlist = []
calclst = []
rmselst = []

graph_types = ('time', 'temp', 'prss', 'sped')

dicttypes = {
	'time': timelst,
	'temp': templst,
	'prss': prsslst,
	'sped': spdlist,
	'hght': hghtlst,
	'calc': calclst, # Alturas a partir de presión
	'rmse': rmselst  # Raíz del error cuadrático medio
}

dictlabel = {
	'time': 'Tiempo',
	'temp': 'Temperatura',
	'prss': 'Presión',
	'sped': 'Altura',
	'hght': 'Altura',
	'calc': 'Altura (presión)'
}


dictunits = {
	'time': 's',
	'temp': 'ºC',
	'prss': 'kPa',
	'sped': 'm',
	'hght': 'm',
	'calc': 'm'
} 



def import_file(file):

	try:
		csv_file = open(str(file), 'r')										# --> Opening file...
	except IOError:
		print(f'File {file} could not be opened.')
		return None

	# time,temp,prss,hdty,lght,lat,lon,hght,spd,\n

	for line in csv_file:

		line = str(line)
		
		if line.startswith('! '):									# --> Taking date and time...
			line = line.removeprefix('! ')
			dattime = line.removesuffix('\n')
			
		elif line.startswith('# '):									# --> Ignoring comments...
			pass

		elif line == []:
			pass

		else:															# --> Taking out line feeds and parsing data (# time,temp,prss,hdty,lght,lat,lon,hght,spd,\n)...
			line = line.split(',')
			line[-1] = float(line[-1])
			timelst.append(  float( line[0] )  )							# --> (***) {
			templst.append(  float( line[1] )  )							#	Modify for changing the template...
			prsslst.append(  float( line[2] )  )							#
			hdtylst.append(  float( line[3] )  )							#
			lghtlst.append(  float( line[4] )  )							# }
			latlist.append(  float( line[6] )  )
			lonlist.append(  float( line[5] )  )
			hghtlst.append(  float( line[6] )  )
			spdlist.append(  float( line[7] )  )
			
	print(f'Data from {file} were imported.')
	
	csv_file.close()
	


def ptv():

	fig, ax = plt.subplots(nrows=3, ncols=1)
		
	xcoord = 'time'
	ycoord = ['temp', 'prss', 'sped']									# --> Taking Y coordinate(s) and cheking if valid...

	
	for i in enumerate(ycoord):
		ax[i[0]].plot(dicttypes[xcoord], dicttypes[ycoord[i[0]]], marker='.', label=f"{dictlabel[ ycoord[i[0]] ]} ({ dictunits[ ycoord[i[0]] ] })")

		
	xlbl = 'Time'

	for i in enumerate(ycoord):
		sv = 0
		mn = dicttypes[ycoord[i[0]]][-1]
		mx = mn
		for j in dicttypes[ycoord[i[0]]]:
			if j == 0:
				print(j, endline='')
			sv += j
			if j < mn:
				mn = j
			elif j > mx:
				mx = j
			mm = sv/len(dicttypes[ycoord[i[0]]])
		tycks = [mn, (mn+mm)/2, mm, (mm+mx)/2, mx]
		
		ax[i[0]].set_xlabel(xlbl)
		ax[i[0]].set_ylabel( dictlabel[ graph_types[ i[0]+1 ] ] )
		d = (tycks[-1]-tycks[0])/10
		ax[i[0]].set_ylim([ mn - d, mx + d])	 
	
		ax[i[0]].set_xticks( arange( min(dicttypes[xcoord]), max(dicttypes[xcoord]), 400) )
		ax[i[0]].set_yticks( tycks )
		ax[i[0]].minorticks_on()
		ax[i[0]].tick_params(direction='inout', length=20)

		ax[i[0]].legend()
	
	fig.subplots_adjust(left=0.1, bottom=0.1, right=0.98, top=0.93, hspace=0.35)
	fig.suptitle('CANSAT', fontsize=15)
	
	plt.show()
	
	

def hcs():
	
	T0 = 288.15  
	L = 0.0065   
	P0 = 1013.25 
	R = 287.05   

	for i in prsslst:
		calclst.append( (T0 / L) * (1 - ( (10*i) / P0) ** (R / L)) )
	
	k = 0
	for i in enumerate(hghtlst):
		k += ( ( hghtlst[i[0]] - calclst[i[0]] )**2 )
	
	rmse = ( k/len(hghtlst) )**(1/2)
	
	print(rmse)
	
	fig, ax = plt.subplots(nrows=3, ncols=1)
		
	xcoord = 'time'
	ycoord = ['prss', 'hght', 'calc']

	
	for i in enumerate(ycoord):
		ax[i[0]].plot(dicttypes[xcoord], dicttypes[ycoord[i[0]]], marker='.', label=f"{dictlabel[ ycoord[i[0]] ]} ({ dictunits[ ycoord[i[0]] ] })")

		
	xlbl = 'Time'

	for i in enumerate(ycoord):
		sv = 0
		mn = dicttypes[ycoord[i[0]]][-1]
		mx = mn
		for j in dicttypes[ycoord[i[0]]]:
			if j == 0:
				print(j, endline='')
			sv += j
			if j < mn:
				mn = j
			elif j > mx:
				mx = j
			mm = sv/len(dicttypes[ycoord[i[0]]])
		tycks = [mn, (mn+mm)/2, mm, (mm+mx)/2, mx]
		
		ax[i[0]].set_xlabel(xlbl)
		ax[i[0]].set_ylabel( dictlabel[ graph_types[ i[0]+1 ] ] )
		d = (tycks[-1]-tycks[0])/10
		ax[i[0]].set_ylim([ mn - d, mx + d])	 
	
		ax[i[0]].set_xticks( arange( min(dicttypes[xcoord]), max(dicttypes[xcoord]), 400) )
		ax[i[0]].set_yticks( tycks )
		ax[i[0]].minorticks_on()
		ax[i[0]].tick_params(direction='inout', length=20)

		ax[i[0]].legend()
	
	fig.subplots_adjust(left=0.1, bottom=0.1, right=0.98, top=0.93, hspace=0.35)
	fig.suptitle('CANSAT', fontsize=15)
	
	plt.show()
	

import_file( input('\n--> file:   ') )
ptv()
#hcs()
