#!/bin/bash

color_echo() {
  case $1 in
    "green") echo -e "[*] \033[0;32m$2\033[0m" ;;
    "red") echo -e "[*] \033[0;31m$2\033[0m" ;;
    *) echo "[*] $2" ;;
  esac
}

color_echo "green" "Procesa archivos de audio de tu conjunto de datos personalizado, los codifica como espectrogramas mel y los guarda en el disco. Esto te permitirá entrenar el codificador. Asegúrate de que tu conjunto de datos esté organizado correctamente.\n"

custom_dataset="custom_dataset"
# Solicitar la ruta al directorio de datos
color_echo "red" "Ruta al directorio que contiene tu conjunto de datos personalizado: \c"
read datasets_root
color_echo "red" "Nombre de la carpeta que contiene tus audios (o presiona Enter para omitir): \c"
read folder_name
color_echo "green" "\n[*] Resumen de configuración:"
color_echo "green" "[*] Ruta al directorio de datos: $datasets_root"
color_echo "green" "[*] Conjunto de datos personalizado: $custom_dataset"
color_echo "green" "[*] Nombre de la carpeta de audios: ${folder_name:-No especificado}"
color_echo "red" "[*] ¿Quieres ejecutar el script principal? (S/n): "
read confirm_run
if [ "$confirm_run" != "S" ] && [ "$confirm_run" != "s" ]; then
  color_echo "red" "[*] Ejecución cancelada. Saliendo del script."
  exit 1
fi
python encoder_preprocess.py "$datasets_root" "$custom_dataset" --folder_name "${folder_name}"

