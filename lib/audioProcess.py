# Convert Audio From MP3 to WAV
from pydub import AudioSegment
from tqdm import tqdm
import os

# Get File Extension
def get_file_without_extension(filename):
    """A helper function to get a file's extension"""
    return os.path.splitext(filename)[0].lstrip(".")

def convertAudio(extracted_data, config, output_dir):

    #  Create Directory if directory not exist
    if os.path.isdir(output_dir):
        pass
    else :
        os.mkdir(output_dir)

    # Convert Process
    for audio in extracted_data:
        # Get File Name Without extension
        filename=get_file_without_extension(os.path.basename(audio[0]))

        # convert audio to wav 16Khz 16Bit    
        audio_dest = os.path.join(output_dir, filename+".wav")                                                        
        audSeg = AudioSegment.from_file(audio[0])
        audSeg.export(audio_dest, format="wav", parameters=["-ar", str(config["sample-rate"])])
        
        # change path of audio (get from result convert)
        audio[0]=audio_dest
        # break

    # Return List Data
    return extracted_data