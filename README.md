# Proyecto: Extractor de Código desde Archivos TXT

## Descripción

Este proyecto es un script en Python diseñado para recorrer todos los archivos con extensión `.txt` dentro de un directorio especificado. El script busca dentro de cada archivo las secciones de código delimitadas por las etiquetas `//{{CODEBEGIN` y `//{{CODEEND` y extrae el contenido que se encuentra entre ellas.

El contenido extraído se guarda en un nuevo archivo con el mismo nombre pero con la extensión `.gpt`. El script también maneja múltiples secciones de código dentro del mismo archivo `.txt`, y omite la escritura de las propias etiquetas `//{{CODEBEGIN` y `//{{CODEEND`.

## Requisitos

- Python 3.x

## Uso

1. **Clonar el repositorio o descargar los archivos.**

2. **Modificar la ruta del directorio:**
   
   Abre el archivo `extractor.py` y modifica la variable `directorio` con la ruta del directorio que contiene tus archivos `.txt`.

   ```python
   directorio = "ruta/a/tu/carpeta"
