import argparse
import os

from yaml import safe_load
from lib.extractCSV import extractCSV
from lib.kaldiDataset import createDataset
from lib.audioProcess import convertAudio


def run(args, config):
    # Extract CSV File
    dataset = extractCSV(args.input_file, args.output_dir, config)
    
    # Convert Audio
    convertAudio(dataset, config, args.output_dir)

    # Create Dataset Kaldi Format
    createDataset(dataset, args.output_dir)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input_file', required=True)
    parser.add_argument('--output_dir', dest='output_dir', required=True)
    parser.add_argument("-c", "--config", default="conf/conf.yaml")
    
    args = parser.parse_args()

    config = safe_load(open(args.config, "rb"))
    run(args, config)
    