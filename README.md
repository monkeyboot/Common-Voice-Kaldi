## Common Voice Data Extraction
This repo is used for extraction of common voice data into kaldi dataset

## Feature
1. extract csv data with adjustable delimiter [comma or tabs] (conf.yaml)
2. convert mp3 to wav 
3. make kaldi dataset from common voice data
4. output sample rate adjustable (conf.yaml)

## Dependencies
1. pydub
2. pyYaml
3. tqdm
4. python 3.6

## Installation Dependencies
### Automatic
1. virtualenv -p python3.6 venv
2. source venv/bin/activate
3. pip install -r requirements.txt
### Manual
1. virtualenv -p python3.6 venv
2. source venv/bin/activate
3. pip install pyyaml
4. pip install pydub
5. pip install tqdm

## How to Use
### Command
1. source venv/bin/activate
2. make sure audio path in (conf/conf.yaml) is location of audio
3. python extractDataCV.py --input [input-file-csv] --output-dir [directory-output]

### Configuration (conf/conf.yaml)
```yaml
# Delimiter (tabs or comma) in csv file
delimiter: tabs
audio-path: /data/suara/NEW/cv-corpus-6.1-2020-12-11/id/clips
# Output Data
sample-rate: 16000
```

### Example
```
source venv/bin/activate

python extractDataCV.py --input /data/suara/NEW/cv-corpus-6.1-2020-12-11/id/train.tsv --output_dir /data/suara/NEW/wav-cv-corpus-6.1-2020-12-11/train
```

### Output data
```
- /data/suara/NEW/wav-cv-corpus-6.1-2020-12-11/train
    - [audio...n_audio]
    - wav.scp
    - text
    - spk2utt
    - utt2spk
```