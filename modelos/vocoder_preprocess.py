from synthesizer.synthesize import run_synthesis
from synthesizer.hparams import hparams
from utils.argutils import print_args
import argparse
import os

if __name__ == "__main__":
    class MyFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
        pass
    
    parser = argparse.ArgumentParser(
        description="Crea espectrogramas alineados a la verdad básica (GTA) a partir del vocoder.",
        formatter_class=MyFormatter
    )
    parser.add_argument("datasets_root", type=str, help=\
        "Ruta al directorio que contiene tu directorio SV2TTS. Si especificas tanto --in_dir como "
        "--out_dir, este argumento no se utilizará.")
    parser.add_argument("--model_dir", type=str, 
                        default="synthesizer/saved_models/pretrained/", help=\
        "Ruta al directorio del modelo preentrenado.")
    parser.add_argument("-i", "--in_dir", type=str, default=argparse.SUPPRESS, help= \
        "Ruta al directorio del sintetizador que contiene los espectrogramas mel, los wavs y los "
        "embeds. Por defecto, <datasets_root>/SV2TTS/synthesizer/.")
    parser.add_argument("-o", "--out_dir", type=str, default=argparse.SUPPRESS, help= \
        "Ruta al directorio del vocoder de salida que contendrá los espectrogramas mel alineados "
        "a la verdad básica. Por defecto, <datasets_root>/SV2TTS/vocoder/.")
    parser.add_argument("--hparams", default="",
                        help="Reemplazos de hiperparámetros como una lista de pares nombre=valor separados por comas")
    parser.add_argument("--no_trim", action="store_true", help=\
        "Procesa el audio sin recortar los silencios (no recomendado).")
    parser.add_argument("--cpu", action="store_true", help=\
        "Si es True, el procesamiento se realiza en la CPU, incluso cuando hay una GPU disponible.")
    args = parser.parse_args()
    print_args(args, parser)
    modified_hp = hparams.parse(args.hparams)
    
    if not hasattr(args, "in_dir"):
        args.in_dir = os.path.join(args.datasets_root, "SV2TTS", "synthesizer")
    if not hasattr(args, "out_dir"):
        args.out_dir = os.path.join(args.datasets_root, "SV2TTS", "vocoder")

    if args.cpu:
        # Oculta las GPUs de Pytorch para forzar el procesamiento en CPU
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    
    # Verifica que webrtcvad esté disponible
    if not args.no_trim:
        try:
            import webrtcvad
        except:
            raise ModuleNotFoundError("Paquete 'webrtcvad' no encontrado. Este paquete permite "
                "la eliminación de ruido y se recomienda. Por favor, instálalo e inténtalo nuevamente. "
                "Si la instalación falla, usa --no_trim para desactivar este mensaje de error.")
    del args.no_trim

    run_synthesis(args.in_dir, args.out_dir, args.model_dir, modified_hp)
