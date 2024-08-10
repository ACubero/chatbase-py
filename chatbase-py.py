import os
import shutil
from datetime import datetime

def copiar_renombrar_smd_a_txt(directorio_origen, directorio_proyecto):
    # Crear la carpeta "source_txt" dentro del proyecto si no existe
    carpeta_destino = os.path.join(directorio_proyecto, "source_txt")
    os.makedirs(carpeta_destino, exist_ok=True)
    
    # Copiar y renombrar archivos .SMD a .TXT (considerando mayúsculas y minúsculas)
    for nombre_archivo in os.listdir(directorio_origen):
        if nombre_archivo.lower().endswith('.smd'):
            ruta_origen = os.path.join(directorio_origen, nombre_archivo)
            nuevo_nombre = f"{os.path.splitext(nombre_archivo)[0]}.txt"
            ruta_destino = os.path.join(carpeta_destino, nuevo_nombre)
            shutil.copy(ruta_origen, ruta_destino)

def extraer_codigos_txt_a_gpt(directorio_proyecto):
    # Recorre todos los archivos TXT en la carpeta "source_txt"
    carpeta_txt = os.path.join(directorio_proyecto, "source_txt")
    for nombre_archivo in os.listdir(carpeta_txt):
        if nombre_archivo.lower().endswith('.txt'):
            ruta_archivo_txt = os.path.join(carpeta_txt, nombre_archivo)
            nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
            ruta_archivo_gpt = os.path.join(carpeta_txt, f"{nombre_sin_extension}.gpt")
            
            with open(ruta_archivo_txt, 'r') as archivo_txt, open(ruta_archivo_gpt, 'w') as archivo_gpt:
                guardar = False
                for linea in archivo_txt:
                    if "//{{CODEBEGIN" in linea:
                        guardar = True
                        continue  # No graba esta línea
                    elif "//{{CODEEND" in linea:
                        guardar = False
                        continue  # No graba esta línea
                    
                    if guardar:
                        archivo_gpt.write(linea)

def generar_fichero_resultado(directorio_proyecto):
    # Crear la carpeta "result" si no existe
    carpeta_result = os.path.join(directorio_proyecto, "result")
    os.makedirs(carpeta_result, exist_ok=True)
    
    # Obtener la fecha actual en formato AAAAMMDD
    fecha_actual = datetime.now().strftime("%Y%m%d")
    
    # Nombre del archivo de salida con la fecha actual
    nombre_archivo_salida = f"source_train_sample_cosmos_{fecha_actual}.txt"
    ruta_archivo_salida = os.path.join(carpeta_result, nombre_archivo_salida)
    
    # Recorrer todos los archivos .GPT en la carpeta "source_txt" y combinar su contenido
    carpeta_txt = os.path.join(directorio_proyecto, "source_txt")
    with open(ruta_archivo_salida, 'w') as archivo_salida:
        for nombre_archivo in os.listdir(carpeta_txt):
            if nombre_archivo.lower().endswith('.gpt'):
                ruta_archivo_gpt = os.path.join(carpeta_txt, nombre_archivo)
                with open(ruta_archivo_gpt, 'r') as archivo_gpt:
                    archivo_salida.write(archivo_gpt.read())
                    archivo_salida.write("\n")  # Agrega un salto de línea entre contenidos

if __name__ == "__main__":
    # Definir la ruta del directorio de origen y del directorio del proyecto
    directorio_origen = "c:/cosmos/samples"
    directorio_proyecto = os.getcwd()  # Carpeta donde se ejecuta el script de Python
    
    copiar_renombrar_smd_a_txt(directorio_origen, directorio_proyecto)
    extraer_codigos_txt_a_gpt(directorio_proyecto)
    generar_fichero_resultado(directorio_proyecto)
