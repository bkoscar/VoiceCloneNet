# VoiceCloneNet

VoiceCloneNet es un modelo de aprendizaje profundo diseñado para generar voces sintéticas realistas mediante el proceso de clonación de voz.

## Preprocesamiento para Espectrogramas Mel

Este script facilita el preprocesamiento de un conjunto de datos al extraer espectrogramas de Mel. Los espectrogramas de Mel son representaciones visuales de la frecuencia del sonido, comúnmente utilizadas en tareas de procesamiento de audio.

### Uso

Para ejecutar el script en un entorno Ubuntu, utiliza el siguiente comando en tu terminal:

```bash
chmod +x preprocesamiento_encoder.sh
./preprocesamiento_encoder.sh
```

### Requisitos

Asegúrate de tener instalado Python 3.9 en tu sistema y el entorno debes llamarlo Enviroment. Puedes instalar las dependencias necesarias ejecutando el siguiente comando:

```bash
python3.9 -m venv Enviroment
source venv/bin/activate
pip install -r requirements.txt
```
### Funcionalidad

El script preprocesamiento_encoder.sh puede ejecutarse sin argumentos para realizar el preprocesamiento con valores predeterminados. Realiza las siguientes acciones:
1. Extracción de Espectrogramas de Mel: Utiliza técnicas de procesamiento de audio para convertir los archivos de audio en espectrogramas de Mel.
2. Almacenamiento de Resultados: Guarda los espectrogramas de Mel generados en la ruta predeterminada.


## Entrenamiento del Embedding
Este script de Python parece estar diseñado para entrenar un modelo de codificación de hablantes. 

### Uso

Instala Pytorch:
    https://pytorch.org/

Antes de ejecutar el script, utiliza el siguiente comando en tu terminal:

```bash
chmod +x encoder_train.sh
./encoder_train.sh
```

##  Preprocesamiento de Audio para Synthesizer

## Descripción
Este script  preprocesamiento_sintetizador.sh se utiliza para realizar el preprocesamiento de archivos de audio como parte del proceso de entrenamiento del Synthesizer. El objetivo principal es codificar archivos de audio como espectrogramas mel y guardarlos en disco, facilitando así el entrenamiento del codificador. Además, los archivos de audio procesados son guardados para su uso durante el entrenamiento del vocoder.

## Uso

Asegúrate de tener correctamente configurado tu entorno virtual y todos los paquetes necesarios antes de ejecutar el script. Puedes utilizar el siguiente comando para ejecutar el script:

```bash
chmod +x encoder_train.sh
./preprocesamiento_sintetizador.sh
```
## Estructura de las carpetas de la data
La carpeta donde se encuentran los datos se llama Wav, dentro de ella hay un subfolder llamado mydata, debes tener la estructura de esta forma para poder correr el script.
```bash
tree -L 2

Wav
└── mydata
    ├── 367
    └── 533
```

