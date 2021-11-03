# Extract CSV file from common voice
import csv
import os

def extractCSV(input, output_dir, config):
    data=[]
    _delimiter=""
    extracted_data=[]

    if config["delimiter"] == "tabs" :
        _delimiter = '\t'
    elif config["delimiter"] == "comma" :
        _delimiter = ','
    else :
        print("delimiter not valid")
        sys.exit("delimiter not valid, use \"tabs\" or \"comma\" at conf\/conf.yaml")
    
    try:
        with open(input, newline='') as f:
            reader = csv.reader(f, delimiter=_delimiter)
            # header handler
            next(reader)
            # data handler
            data = list(reader)
            print(config["audio-path"])
            audiopath=config["audio-path"]

            for dataset in data:
                full_audio_path=os.path.join(audiopath, dataset[1])
                extracted_data.append([full_audio_path,dataset[2]])
            
            return extracted_data
            # print(extracted_data)
        
        return data
    except Exception as err:
            print("ERROR: "+str(err))
            print("Please Check delimiter, make sure delimiter of csv file and config file is the same")
        
