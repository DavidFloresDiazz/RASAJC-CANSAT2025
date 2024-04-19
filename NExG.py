
from qgis.core import QgsApplication, QgsRasterLayer
from qgis.analysis import QgsRasterCalculatorEntry, QgsRasterCalculator

# Inicializar la aplicación QGIS
QgsApplication.setPrefixPath('/path/to/qgis/installation', True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Rutas de entrada y salida
input_raster_path = 'C:/Users/madrid/Desktop/PYTHON/PROCESADO DE IMAGENES/bosque1.tif'
output_raster_path = 'C:/Users/madrid/Desktop/sque1.tif'

# Cargar la capa raster de entrada
input_raster = QgsRasterLayer(input_raster_path, 'input_raster')

# Comprobar si la capa se cargó correctamente
if not input_raster.isValid():
    print("Error: No se pudo cargar la capa raster de entrada")
else:
    # Definir las bandas para el filtro NExG (generalmente bandas NIR, Red y Azul)
    green_band = QgsRasterCalculatorEntry()
    green_band.ref = 'input_raster@2'
    green_band.raster = input_raster
    green_band.bandNumber = 2

    red_band = QgsRasterCalculatorEntry()
    red_band.ref = 'input_raster@1'
    red_band.raster = input_raster
    red_band.bandNumber = 1

    blue_band = QgsRasterCalculatorEntry()
    blue_band.ref = 'input_raster@3'
    blue_band.raster = input_raster
    blue_band.bandNumber = 3

    # Fórmula para calcular el filtro NExG
    formula = '((2 * {green} - {red} - {blue}) / ( 2 * {green} + {red} + {blue}))'.format(green=green_band.ref, red=red_band.ref, blue=blue_band.ref)

    # Configurar el objeto QgsRasterCalculator
    calc = QgsRasterCalculator(formula, output_raster_path, 'GTiff', input_raster.extent(), input_raster.width(), input_raster.height(), [green_band, red_band, blue_band])

    # Ejecutar el cálculo
    calc.processCalculation()

    print("Filtro NExG aplicado exitosamente. El resultado se ha guardado en:", output_raster_path)

# Finalizar la aplicación QGIS
qgs.exitQgis()
