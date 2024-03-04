#!/bin/bash

color_echo() {
  case $1 in
    "green") echo -e "[*] \033[0;32m$2\033[0m" ;;
    "red") echo -e "\033[0;31m$2\033[0m" ;;
    *) echo "[*] $2" ;;
  esac
}

echo  "*****************************************************************"
echo  "*                                                               *"
echo  "*    Bienvenido al procesamiento de datos de tus audios         *"
echo  "*                                                               *"
echo   "*****************************************************************"
echo 

color_echo "green" "Este script te guiará a través del proceso de preprocesamiento de archivos de audio para el entrenamiento de un embedding."
color_echo "green" "Procesa archivos de audio de tu conjunto de datos personalizado, los codifica como espectrogramas mel y los guarda en el disco."
color_echo "green" "Esto te permitirá entrenar el codificador. Asegúrate de que tu conjunto de datos esté organizado correctamente.\n"

custom_dataset="custom_dataset"
# Solicitar la ruta al directorio de datos
read -p "$(color_echo 'green' '[*] Ruta al directorio que contiene tu conjunto de datos personalizado: ')" datasets_root
read -p "$(color_echo 'green' '[*] Ruta de salida para los archivos procesados (o presiona Enter para usar el directorio actual): ')" output_dir
# Solicitar el nombre del conjunto de datos hasta que se proporcione uno válido
while true; do
  read -p "$(color_echo 'green' '[*] Nombre del conjunto de datos (dataset_name): ')" dataset_name
  if [ -z "$dataset_name" ]; then
    color_echo "red" "[*] Debes proporcionar un nombre para el conjunto de datos."
  else
    break
  fi
done
read -p "$(color_echo 'green' '[*] Nombre de la carpeta que contiene tus audios: ')" folder_name

echo
echo "[*] Resumen de configuración:"
color_echo "green" "Ruta al directorio de datos: $(color_echo 'red' "$datasets_root")"
color_echo "green" "Conjunto de datos personalizado: $(color_echo 'red' "$custom_dataset")" 
color_echo "green" "Ruta de salida para los archivos procesados: $(color_echo 'red' "${output_dir:-Directorio actual}")"
color_echo "green" "Nombre del conjunto de datos (dataset_name): $(color_echo 'red' "$dataset_name")"
color_echo "green" "Nombre de la carpeta que contiene tus audios(es la subcarpeta que esta contenida en dataset_name y contiene tus audios): $(color_echo 'red' "${folder_name:-No especificado}")"
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

# Ejecutar script de Python
python synthesizer_preprocess_audio.py "$datasets_root" -o "${output_dir:-$datasets_root/SV2TTS/synthesizer}" --subfolders "${folder_name:-train-clean-100,train-clean-360}" --datasets_name "${datasets_root}/${dataset_name}" --no_alignments

color_echo "green" "\n[*] Procesamiento de archivos de audio completado. Los archivos procesados se guardaron en $(color_echo 'red' "${output_dir:-$datasets_root/SV2TTS/synthesizer}")."
