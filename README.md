# VoiceCloneNet

VoiceCloneNet es un modelo de aprendizaje profundo diseñado para generar voces sintéticas realistas mediante el proceso de clonación de voz.

## Script de Preprocesamiento para Espectrogramas Mel

Este script facilita el preprocesamiento de un conjunto de datos al extraer espectrogramas de Mel. Los espectrogramas de Mel son representaciones visuales de la frecuencia del sonido, comúnmente utilizadas en tareas de procesamiento de audio.

### Uso

Para ejecutar el script en un entorno Ubuntu, utiliza el siguiente comando en tu terminal:

```bash
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