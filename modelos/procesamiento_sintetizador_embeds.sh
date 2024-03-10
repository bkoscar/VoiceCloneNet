#!/bin/bash

color_echo() {
  case $1 in
    "green") echo -e "[*] \033[0;32m$2\033[0m" ;;
    "red") echo -e "\033[0;31m$2\033[0m" ;;
    *) echo "[*] $2" ;;
  esac
}

echo "*****************************************************************"
echo "*                                                                *"
echo "*    Bienvenido al procesamiento de los embeddings de la data    *"
echo "*             y entrenamiento del sintetizador                   *"
echo "*                                                                *"
echo "*****************************************************************"
echo

color_echo "green" "Este script te guiará a través del proceso de preprocesamiento de archivos de audio para el entrenamiento del sintetizador y el codificador."
color_echo "green" "Procesa archivos de audio de tu conjunto de datos personalizado, los codifica como espectrogramas mel y los guarda en el disco."
color_echo "green" "Esto te permitirá entrenar el codificador. Asegúrate de que tu conjunto de datos esté organizado correctamente.\n"

# Solicitar los argumentos synthesizer_root y encoder_model_fpath
read -p "$(color_echo 'green' '[*] Ruta al directorio de entrenamiento del sintetizador (Es la ruta donde se guardo el procesamiento del script procesamiento_sintetizador.sh debes encontrar train.txt carpeta mels y audios): ')" synthesizer_root
read -p "$(color_echo 'green' '[*] Ruta al modelo encoder entrenado previamente: ')" encoder_model_fpath

echo
echo "[*] Resumen de configuración:"
color_echo "green" "Ruta al directorio de entrenamiento del sintetizador: $(color_echo 'red' "$synthesizer_root")"
color_echo "green" "Ruta al modelo de codificador entrenado: $(color_echo 'red' "$encoder_model_fpath")"

read -p "$(color_echo 'green' '[*] ¿Quieres ejecutar el script principal? (S/n): ')" confirm_run
if [ "$confirm_run" != "S" ] && [ "$confirm_run" != "s" ]; then
  color_echo "red" "[*] Ejecución cancelada. Saliendo del script."
  exit 1
fi

# Activar entorno virtual
source Enviroment/bin/activate
if [ -z "$VIRTUAL_ENV" ]; then
    color_echo "red" "[*] Error al activar el entorno virtual. Saliendo del script."
    exit 1
else
    color_echo "green" "[*] Entorno virtual activado correctamente."
fi

# Ejecutar script de Python con los argumentos proporcionados
python synthesizer_preprocess_embeds.py "$synthesizer_root" -e "$encoder_model_fpath"

color_echo "green" "\n[*] Procesamiento de archivos de audio completado."
color_echo "green" "[*] La creacion de los embeddings de los audios se ha completado y los puedes encontrar en $(color_echo 'red' "${synthesizer_root}")."
