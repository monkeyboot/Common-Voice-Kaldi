# Save audio to Kaldi Data Formatted

import os
import re

def get_file_without_extension(filename):
    """A helper function to get a file's extension"""
    return os.path.splitext(filename)[0].lstrip(".")

# create spk2utt
def createSpk2utt(dataset, output_dir):
    spk2uttfile=os.path.join(output_dir, "spk2utt")
    index=0
    with open(spk2uttfile, 'w') as f:
        for audio_id in dataset:
            index = index+1
            # Get File Name Without extension
            f.write(audio_id +" "+ audio_id)
            if (index==len(dataset)):
                pass
            else:
                f.write('\n')

# create utt2spk
def createUtt2spk(dataset, output_dir ):
    utt2spkfile=os.path.join(output_dir, "utt2spk")
    index=0
    with open(utt2spkfile, 'w') as f:
        for audio_id in dataset:
            index = index+1
            # Get File Name Without extension
            f.write(audio_id +" "+ audio_id)
            if (index==len(dataset)):
                pass
            else:
                f.write('\n')

# create text
def createText(dataset, output_dir):
    textfile=os.path.join(output_dir, "text")
    index=0
    with open(textfile, 'w') as f:
        for data in dataset:
            index = index+1
            # Get File Name Without extension
            audio_id=get_file_without_extension(os.path.basename(data[0]))
            transcript = re.sub("[^0-9a-zA-Z-]+", " ", data[1])
            f.write(audio_id +" "+ transcript.lower())
            if (index==len(dataset)):
                pass
            else:
                f.write('\n')


# create wav.scp
def createWavSCP(dataset, output_dir):
    wavscpfile=os.path.join(output_dir, "wav.scp")
    audio_id_list=[]
    index=0
    with open(wavscpfile, 'w') as f:
        for data in dataset:
            index = index+1
            # Get File Name Without extension
            audio_id=get_file_without_extension(os.path.basename(data[0]))
            f.write(audio_id +" "+ data[0])
            if (index==len(dataset)):
                pass
            else:
                f.write('\n')
            audio_id_list.append(audio_id)

    return audio_id_list

# create dataset
def createDataset(extracted_data, output_dir):
    # Create wav.scp
    audio_id = createWavSCP(extracted_data, output_dir)
    #  Create text
    createText(extracted_data, output_dir)
    
    # Create spk2utt
    createSpk2utt(audio_id, output_dir)
    # Create utt2spk
    createUtt2spk(audio_id, output_dir)
  


