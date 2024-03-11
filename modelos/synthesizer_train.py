from synthesizer.hparams import hparams
from synthesizer.train import train
from utils.argutils import print_args
import argparse

if __name__ == "__main__":
    # Configurar el analizador de argumentos de línea de comandos
    parser = argparse.ArgumentParser()
    parser.add_argument("run_id", type=str, help= \
        "Nombre para esta instancia del modelo. Si se guardó un estado del modelo con el mismo ID de ejecución, "
        "el entrenamiento se reiniciará desde allí. Use -f para sobrescribir estados guardados y "
        "reiniciar desde cero.")
    parser.add_argument("syn_dir", type=str, default=argparse.SUPPRESS, help= \
        "Ruta al directorio del sintetizador que contiene los espectrogramas mel de referencia, "
        "los archivos de audio (wavs) y los embeddings.")
    parser.add_argument("-m", "--models_dir", type=str, default="synthesizer/saved_models/", help=\
        "Ruta al directorio de salida que contendrá los pesos del modelo guardados y los registros.")
    parser.add_argument("-s", "--save_every", type=int, default=1000, help= \
        "Número de pasos entre actualizaciones del modelo en el disco. Establecer en 0 para no guardar "
        "el modelo.")
    parser.add_argument("-b", "--backup_every", type=int, default=25000, help= \
        "Número de pasos entre copias de seguridad del modelo. Establecer en 0 para no realizar copias de seguridad "
        "del modelo.")
    parser.add_argument("-f", "--force_restart", action="store_true", help= \
        "No cargar ningún modelo guardado y reiniciar desde cero.")
    parser.add_argument("--hparams", default="",
                        help="Sobrescribir hiperparámetros como una lista separada por comas de pares nombre=valor")
    args = parser.parse_args()
    
    # Imprimir los argumentos proporcionados
    print_args(args, parser)

    # Analizar los hiperparámetros
    args.hparams = hparams.parse(args.hparams)

    # Ejecutar el entrenamiento
    train(**vars(args))
