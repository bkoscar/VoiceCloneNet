# VoiceCloneNet
VoiceCloneNet: Genera voces sintéticas realistas con este modelo de deep learning para clonación de voz.

# Script de preprocesamiento para espectrogramas Mel

Este script realiza el preprocesamiento de un conjunto de datos, extrayendo espectrogramas de Mel. Los espectrogramas de Mel son representaciones visuales de la frecuencia del sonido que se utilizan comúnmente en tareas de procesamiento de audio.

## Uso

Para ejecutar el script, utiliza el siguiente comando en tu terminal:

```bash
./preprocesamiento_encoder.sh <ruta_del_dataset> <nombre_del_dataset> <ruta_de_salida>
```
Argumentos

    <ruta_del_dataset>: La ruta al directorio que contiene los archivos de audio del dataset.
    <nombre_del_dataset>: El nombre del dataset, que se utilizará para identificar los archivos generados.
    <ruta_de_salida>: La ruta donde se guardarán los espectrogramas de Mel generados.

Funcionalidad

El script realiza las siguientes acciones:
    Extracción de Espectrogramas de Mel: Utiliza técnicas de procesamiento de audio para convertir los archivos de audio en espectrogramas de Mel.
    Almacenamiento de Resultados: Guarda los espectrogramas de Mel generados en la ruta de salida especificada.


```bash
./preprocesamiento_encoder.sh ./datos/ mi_dataset ./espectrogramas_mel
```