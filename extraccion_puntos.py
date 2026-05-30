import urllib.request
import zipfile
import xml.etree.ElementTree as ET
import io

# 1. El ID que viene al final de tu enlace
geogebra_id = "n79ygfcg"

# La API oculta de GeoGebra para descargar el archivo .ggb directo
url = f"https://www.geogebra.org/material/download/format/file/id/{geogebra_id}"

print(f"Conectando a GeoGebra para descargar el proyecto: {geogebra_id}...\n")

try:
    # 2. Descargamos el archivo a la memoria (sin crear basura en tu computadora)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    respuesta = urllib.request.urlopen(req)
    archivo_zip = zipfile.ZipFile(io.BytesIO(respuesta.read()))
    
    # 3. Leemos las matemáticas internas del archivo
    with archivo_zip.open('geogebra.xml') as f:
        tree = ET.parse(f)
        root = tree.getroot()

    # 4. Extraemos e imprimimos los puntos en formato Python
    print("puntos_semaforo = np.array([")
    
    for element in root.findall('.//element'):
        if element.get('type') == 'point':
            coords = element.find('coords')
            if coords is not None:
                x = float(coords.get('x'))
                y = float(coords.get('y'))
                print(f"    [{x}, {y}],")
                
    print("])")
    print("\n¡Listo! Copia el arreglo de arriba directo a tu código del Perceptrón.")

except Exception as e:
    print("Hubo un error al intentar descargar los puntos:", e)
    print("Asegúrate de que tu proyecto en GeoGebra esté guardado como 'Público' o 'Compartido con enlace'.")