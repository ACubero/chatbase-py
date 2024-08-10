import os

def extraer_codigos_txt_a_gpt(directorio):
    # Recorre todos los archivos del directorio
    for nombre_archivo in os.listdir(directorio):
        if nombre_archivo.endswith('.txt'):
            ruta_archivo_txt = os.path.join(directorio, nombre_archivo)
            nombre_sin_extension = os.path.splitext(nombre_archivo)[0]
            ruta_archivo_gpt = os.path.join(directorio, f"{nombre_sin_extension}.gpt")
            
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

if __name__ == "__main__":
    directorio = "source_txt"  # Reemplaza con la ruta a la carpeta donde están los archivos TXT
    extraer_codigos_txt_a_gpt(directorio)
