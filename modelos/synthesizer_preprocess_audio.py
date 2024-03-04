from synthesizer.preprocess import preprocess_dataset
from synthesizer.hparams import hparams
from utils.argutils import print_args
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Procesa archivos de audio de conjuntos de datos, los codifica como espectrogramas mel "
                    "y los escribe en el disco. Los archivos de audio también se guardan para ser utilizados por el "
                    "vocoder durante el entrenamiento.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("datasets_root", type=Path, help=\
        "Ruta al directorio que contiene tus conjuntos de datos de LibriSpeech/TTS.")
    parser.add_argument("-o", "--out_dir", type=Path, default=argparse.SUPPRESS, help=\
        "Ruta al directorio de salida que contendrá los espectrogramas mel, los archivos de audio y los "
        "incrustados. Por defecto, es <datasets_root>/SV2TTS/synthesizer/")
    parser.add_argument("-n", "--n_processes", type=int, default=None, help=\
        "Número de procesos en paralelo.")
    parser.add_argument("-s", "--skip_existing", action="store_true", help=\
        "Si se deben sobrescribir los archivos existentes con el mismo nombre. Útil si la preprocesamiento fue "
        "interrumpido.")
    parser.add_argument("--hparams", type=str, default="", help=\
        "Anulaciones de hiperparámetros como una lista de pares de nombre y valor separados por comas")
    parser.add_argument("--no_trim", action="store_true", help=\
        "Procesar audio sin recortar silencios (no recomendado).")
    parser.add_argument("--no_alignments", action="store_true", help=\
        "Usar esta opción cuando el conjunto de datos no incluye alineaciones "
        "(se utilizan para dividir archivos de audio largos en subutterancias).")
    parser.add_argument("--datasets_name", type=str, default="/home/oscar/Documents/AudioCloning/VoiceCloneNet/Wav", help=\
        "Nombre del directorio del conjunto de datos a procesar.")
    parser.add_argument("--subfolders", type=str, default="train-clean-100, train-clean-360", help=\
        "Lista de subdirectorios separados por comas para procesar dentro del directorio de tu conjunto de datos.")
    args = parser.parse_args()

    # Procesar los argumentos
    if not hasattr(args, "out_dir"):
        args.out_dir = args.datasets_root.joinpath("SV2TTS", "synthesizer")

    # Crear directorios
    assert args.datasets_root.exists()
    args.out_dir.mkdir(exist_ok=True, parents=True)

    # Verificar la disponibilidad de webrtcvad
    if not args.no_trim:
        try:
            import webrtcvad
        except:
            raise ModuleNotFoundError("Paquete 'webrtcvad' no encontrado. Este paquete permite "
                "la eliminación de ruido y es recomendado. Por favor, instálalo e intenta de nuevo. Si la instalación falla, "
                "usa --no_trim para deshabilitar este mensaje de error.")
    del args.no_trim

    # Preprocesar el conjunto de datos
    print_args(args, parser)
    args.hparams = hparams.parse(args.hparams)
    preprocess_dataset(**vars(args))
