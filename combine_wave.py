import wave
import os

def combine_wav_files(input_files, output_file):
    # Create a list to hold the input WAV files
    input_wav_files = []

    try:
        # Open each input WAV file and add it to the list
        for input_file in input_files:
            input_wav = wave.open(input_file, 'rb')
            input_wav_files.append(input_wav)

        # Create an output WAV file
        output_wav = wave.open(output_file, 'wb')

        # Set the output file's parameters to match the first input file
        output_wav.setparams(input_wav_files[0].getparams())

        # Loop through each input WAV file and append its data to the output file
        for input_wav in input_wav_files:
            output_wav.writeframes(input_wav.readframes(input_wav.getnframes()))

        # Close the output WAV file
        output_wav.close()

        print(f"Combined {len(input_files)} WAV files into {output_file}")

    except Exception as e:
        print("Error combining WAV files:", str(e))
    finally:
        # Close all input WAV files
        for input_wav in input_wav_files:
            input_wav.close()

# Usage example
if __name__ == "__main__":
    input_files = ["pink60.wav", "pink60.wav", "pink60.wav", "pink60.wav", "pink60.wav"]  # List of input WAV files
    output_file = "output.wav"  # Output combined WAV file
    combine_wav_files(input_files, output_file)
