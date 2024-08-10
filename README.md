# Proyecto: Extractor de Código desde Archivos SMD y TXT

## Descripción

Este proyecto es un script en Python que realiza varias tareas automatizadas sobre archivos con las extensiones `.SMD` y `.TXT`. El script recorre un directorio específico en `c:/cosmos/samples`, copia y renombra los archivos `.SMD` a `.TXT` dentro del proyecto, extrae bloques de código específicos dentro de los archivos `.TXT`, y finalmente genera un archivo de resultado combinando todo el código extraído.

## Funcionalidades

1. **Copia y renombra archivos `.SMD`**:
   - El script crea una carpeta llamada `source_txt` dentro del directorio donde se ejecuta el script.
   - Copia todos los archivos `.SMD` (en cualquier combinación de mayúsculas y minúsculas) desde `c:/cosmos/samples` a `source_txt` y los renombra con la extensión `.TXT`.

2. **Extracción de código**:
   - En los archivos `.TXT` dentro de la carpeta `source_txt`, el script busca y extrae contenido entre las etiquetas `//{{CODEBEGIN` y `//{{CODEEND`.
   - El contenido extraído se guarda en archivos con la misma base de nombre, pero con la extensión `.gpt`, dentro de la carpeta `source_txt`.

3. **Generación de archivo combinado**:
   - El script crea una carpeta `result` dentro del proyecto y genera un archivo llamado `source_train_sample_cosmos_AAAAMMDD.txt`, donde `AAAAMMDD` es la fecha en formato año-mes-día.
   - Este archivo contiene la concatenación de todo el código extraído desde los archivos `.GPT` que se encuentran en la carpeta `source_txt`.

## Requisitos

- Python 3.x

## Uso

1. **Clonar el repositorio o descargar los archivos.**

2. **Ejecutar el script:**

   - Abre una terminal o línea de comandos.
   - Navega hasta el directorio donde se encuentra el archivo `extractor.py`.
   - Ejecuta el script:
   
   ```bash
   python extractor.py
