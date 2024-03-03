from encoder.preprocess import preprocess_mydataset
from utils.argutils import print_args
from pathlib import Path
import argparse
from encoder.config import custom_dataset

# Modificar la configuración en config.py
if "mydataset" in custom_dataset["train"]:
    custom_dataset["train"]["mydataset"][0] = ""

if __name__ == "__main__":
    class MyFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
        pass
    
    parser = argparse.ArgumentParser(
        description="Procesa archivos de audio de tu conjunto de datos personalizado, los codifica como espectrogramas mel "
                    "y los guarda en el disco. Esto te permitirá entrenar el codificador. "
                    "Asegúrate de que tu conjunto de datos esté organizado correctamente.",
        formatter_class=MyFormatter
    )
    parser.add_argument("datasets_root", type=Path, help="Ruta al directorio que contiene tu conjunto de datos personalizado.")
    parser.add_argument("datasets", nargs='+', help="Lista de conjuntos de datos a procesar (por ejemplo, 'mydataset')")
    parser.add_argument("-o", "--out_dir", type=Path, default=argparse.SUPPRESS, 
                        help="Ruta al directorio de salida para los espectrogramas mel.")
    parser.add_argument("-s", "--skip_existing", action="store_true", 
                        help="Si se debe omitir archivos de salida existentes con el mismo nombre. Útil si se interrumpió.")
    parser.add_argument("--folder_name", type=str, help="Nombre de la carpeta que contiene tus audios.")
    args = parser.parse_args()

    # Modificar la configuración en config.py
    if "mydataset" in custom_dataset["train"]:
        custom_dataset["train"]["mydataset"][0] = args.folder_name

    # Procesar los argumentos
    if not hasattr(args, "out_dir"):
        current_directory = Path.cwd()  # Obtener el directorio actual
        args.out_dir = current_directory.joinpath("encoder_output_mel")
    args.out_dir.mkdir(exist_ok=True, parents=True)

    # Preprocesar el conjunto de datos personalizado
    print_args(args, parser)
    preprocess_func = {"custom_dataset": preprocess_mydataset}
    args = vars(args)
    
    for dataset in args.pop("datasets"):
        print("Preprocesando %s" % dataset)
        preprocess_func[dataset](**args)