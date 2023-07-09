import yaml
import argparse
import pandas as pd



def read_config(config_path:str):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path:str)->pd.DataFrame:
    config = read_config(config_path)
    df = pd.read_csv(config["data_source"]["s3_source"])
    return df



if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)
        
