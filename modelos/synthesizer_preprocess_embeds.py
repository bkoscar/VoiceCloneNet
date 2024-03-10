from synthesizer.preprocess import create_embeddings
from utils.argutils import print_args
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Crea embeddings para el sintetizador a partir de las expresiones de LibriSpeech.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("synthesizer_root", type=Path, help=\
        "Ruta a los datos de entrenamiento del sintetizador que contiene los audios y el archivo train.txt. "
        "Si dejas todo como predeterminado, debería ser <datasets_root>/SV2TTS/synthesizer/.")
    parser.add_argument("-e", "--encoder_model_fpath", type=Path, 
                        default="encoder/saved_models/pretrained.pt", help=\
        "Ruta de tu modelo de codificador entrenado.")
    parser.add_argument("-n", "--n_processes", type=int, default=4, help= \
        "Número de procesos paralelos. Se crea un codificador para cada uno, por lo que es posible que necesites reducir "
        "este valor en GPUs con memoria baja. Establécelo en 1 si CUDA no está funcionando correctamente.")
    args = parser.parse_args()
    
    # Preprocesa el conjunto de datos
    print_args(args, parser)
    create_embeddings(**vars(args))
