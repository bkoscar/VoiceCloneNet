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
echo "*    Bienvenido al procesamiento del vocoder                      *"
echo "*                                                                *"
echo "*****************************************************************"
echo

color_echo "green" "Este script te guiará a través del proceso de procesamiento del vocoder."
color_echo "green" "Asegúrate de que tu conjunto de datos esté organizado correctamente y que hayas entrenado un modelo de sintetizador previamente.\n"

# Solicitar los argumentos datasets_root, model_dir, in_dir y out_dir
read -p "$(color_echo 'green' '[*] Ruta al directorio principal que contiene tu directorio Dataset(archivos de audios en .wav): ')" datasets_root
read -p "$(color_echo 'green' '[*] Ruta al directorio del modelo sintetizador.pt: ')" model_dir
read -p "$(color_echo 'green' '[*] Ruta al directorio del sintetizador que contiene los espectrogramas mel, los wavs y los embeds: ')" in_dir
read -p "$(color_echo 'green' '[*] Ruta al directorio del vocoder de salida que contendrá los espectrogramas mel alineados a la verdad básica: ')" out_dir

echo
echo "[*] Resumen de configuración:"
color_echo "green" "Ruta al directorio principal que contiene tu directorio Dataset: $(color_echo 'red' "$datasets_root")"
color_echo "green" "Ruta al directorio del modelo sintetizador.pt: $(color_echo 'red' "$model_dir")"
color_echo "green" "Ruta al directorio del sintetizador: $(color_echo 'red' "$in_dir")"
color_echo "green" "Ruta al directorio del vocoder de salida: $(color_echo 'red' "$out_dir")"

# Preguntar si se desea ejecutar el script en CPU
read -p "$(color_echo 'green' '[*] ¿Quieres ejecutar el script en CPU? (S/n): ')" confirm_cpu
if [ "$confirm_cpu" == "S" ] || [ "$confirm_cpu" == "s" ]; then
  cpu_option="--cpu"
else
  cpu_option=""
fi

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
python vocoder_preprocess.py "$datasets_root" --model_dir "$model_dir" -i "$in_dir" -o "$out_dir" "$cpu_option"

color_echo "green" "\n[*] Procesamiento del vocoder completado."
color_echo "green" "[*] Puedes encontrar los resultados en $(color_echo 'red' "$out_dir")."
