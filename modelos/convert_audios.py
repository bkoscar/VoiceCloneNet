from pydub import AudioSegment
import argparse
import os
import shutil

def convert(args):
    print("The folder from which audio will be extracted is:", args.input_path)
    print("The output folder for the audio is:", args.output_path)
    print("The chosen audio format is:", args.output_format)
    for actual_file, _, files in os.walk(args.input_path):
        output_path = actual_file.replace(args.input_path, args.output_path)
        os.makedirs(output_path, exist_ok=True)
        for file in files:
            if file.lower().endswith((".flac", ".mp3", ".ogg")):
                input_file_path = os.path.join(actual_file, file)
                output_file_path = os.path.join(output_path, os.path.splitext(file)[0] + "." + args.output_format)
                audio = AudioSegment.from_file(input_file_path, format=file.split(".")[-1])
                audio.export(output_file_path, format=args.output_format)
        for text in files:
            if text.endswith(".txt"):
                input_txt_path = os.path.join(actual_file, text)
                output_txt_path = os.path.join(output_path, text)
                if os.path.exists(input_txt_path):
                    shutil.copy(input_txt_path, output_txt_path)
                    print(f"Copied {input_txt_path} to {output_txt_path}")
    print("Conversion completed!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert audio files to a specified format using Pydub")
    parser.add_argument("--input_path", help="The folder containing your audio files")
    parser.add_argument("--output_path", help="The folder where you want to save the converted files")
    parser.add_argument("--output_format", help="The desired output audio format (e.g., wav, mp3)")
    args = parser.parse_args()
    if args.output_format is None:
        print("Please specify the output format using the --output_format argument.")
    else:
        convert(args)
