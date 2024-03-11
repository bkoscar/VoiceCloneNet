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
echo "*    Bienvenido al entrenamiento del sintetizador                *"
echo "*                                                                *"
echo "*****************************************************************"
echo

color_echo "green" "Este script te guiará a través del proceso de entrenamiento del sintetizador."
color_echo "green" "Asegúrate de que tu conjunto de datos esté organizado correctamente y que hayas entrenado un modelo de codificador previamente.\n"

# Solicitar los argumentos run_id, synthesizer_root y encoder_model_fpath
read -p "$(color_echo 'green' '[*] Nombre para esta instancia del modelo (sintetizador por ejemplo): ')" run_id
read -p "$(color_echo 'green' '[*] Ruta al directorio de la data que se proceso en los scirpts anteriores esta carpeta debe contener las siguientes carpetas(audio, embeds, mels y train.txt)): ')" synthesizer_root
read -p "$(color_echo 'green' '[*] Ruta donde se guardara el procesamiento del entrenamiento del sintetizador: ')" sintetizador_model_fpath

echo
echo "[*] Resumen de configuración:"
color_echo "green" "Nombre para esta instancia del modelo (run_id): $(color_echo 'red' "$run_id")"
color_echo "green" "Ruta al directorio de entrenamiento del sintetizador: $(color_echo 'red' "$synthesizer_root")"
color_echo "green" "Ruta al modelo de codificador entrenado: $(color_echo 'red' "$sintetizador_model_fpath")"

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
python synthesizer_train.py "$run_id" "$synthesizer_root" -m "$sintetizador_model_fpath"

color_echo "green" "\n[*] Entrenamiento del sintetizador completado."
color_echo "green" "[*] Puedes encontrar el modelo entrenado en $(color_echo 'red' "${sintetizador_model_fpath}/${run_id}")."
