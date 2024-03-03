#!/bin/bash

color_echo() {
  case $1 in
    "green") echo -e "[*] \033[0;32m$2\033[0m" ;;
    "red") echo -e "\033[0;31m$2\033[0m" ;;
    *) echo "[*] $2" ;;
  esac
}

echo "*****************************************************************"
echo "*                                                               *"
echo "*    Bienvenido al entrenamiento del codificador de altavoces   *"
echo "*                                                               *"
echo "*****************************************************************"
echo

color_echo "green" "Este script entrenará el codificador de altavoces. Asegúrate de haber ejecutado encoder_preprocess.py primero."

# Solicitar argumentos de entrada
read -p "$(color_echo 'green' '[*] Nombre para esta instancia del modelo: ')" run_id
read -p "$(color_echo 'green' '[*] Ruta al directorio de datos preprocesados: ')" clean_data_root
read -p "$(color_echo 'green' '[*] Ruta al directorio de salida que contendrá los pesos del modelo guardados : ')" models_dir
# Establecer valores predeterminados
vis_every=10
umap_every=100
save_every=500
backup_every=7500
force_restart=false
visdom_server="http://localhost"
no_visdom=--no_visdom

# Ejecutar el script de entrenamiento
source Enviroment/bin/activate

if [ -z "$VIRTUAL_ENV" ]; then
    color_echo "red" "[*] Error al activar el entorno virtual. Saliendo del script."
    exit 1
else
    color_echo "green" "[*] Entorno virtual activado correctamente."
fi

python encoder_train.py "$run_id" "$clean_data_root" -m "$models_dir" "$no_visdom"

color_echo "green" "\n[*] Entrenamiento del codificador de altavoces completado."
color_echo "green" "[*] Los modelos entrenados se guardaron en $(color_echo 'red' "$models_dir")."