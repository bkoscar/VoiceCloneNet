from utils.argutils import print_args
from encoder.train import train
from pathlib import Path
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Entrena el codificador de hablantes. Debes haber ejecutado encoder_preprocess.py primero.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("run_id", type=str, help= \
        "Nombre para esta instancia del modelo. Si se guardó previamente un estado del modelo con la misma identificación de ejecución (run ID), el entrenamiento se reiniciará desde allí. Usa -f para sobrescribir estados guardados y reiniciar desde cero.")
    parser.add_argument("clean_data_root", type=Path, help= \
        "Ruta al directorio de salida de encoder_preprocess.py. Si dejaste el directorio de salida predeterminado durante el preprocesamiento, debería ser <datasets_root>/modelos/encoder_output_mel/.")
    parser.add_argument("-m", "--models_dir", type=Path, default="encoder/saved_models/", help=\
        "Ruta al directorio de salida que contendrá los pesos del modelo guardados, así como copias de seguridad de esos pesos y gráficos generados durante el entrenamiento.")
    parser.add_argument("-v", "--vis_every", type=int, default=10, help= \
        "Número de pasos entre actualizaciones de la pérdida y los gráficos.")
    parser.add_argument("-u", "--umap_every", type=int, default=100, help= \
        "Número de pasos entre actualizaciones de la proyección UMAP. Establece en 0 para no actualizar las proyecciones.")
    parser.add_argument("-s", "--save_every", type=int, default=500, help= \
        "Número de pasos entre actualizaciones del modelo en el disco. Establece en 0 para no guardar el modelo.")
    parser.add_argument("-b", "--backup_every", type=int, default=7500, help= \
        "Número de pasos entre copias de seguridad del modelo. Establece en 0 para no hacer copias de seguridad del modelo.")
    parser.add_argument("-f", "--force_restart", action="store_true", help= \
        "No cargar ningún modelo guardado.")
    parser.add_argument("--visdom_server", type=str, default="http://localhost")
    parser.add_argument("--no_visdom", action="store_true", help= \
        "Deshabilitar visdom.")
    args = parser.parse_args()
    
    # Procesar los argumentos
    args.models_dir.mkdir(exist_ok=True)
    
    # Ejecutar el entrenamiento
    print_args(args, parser)
    train(**vars(args))
