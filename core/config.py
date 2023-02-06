import os
import configparser

class Config():

    def get_config_param(path,section, param):
        config = configparser.ConfigParser()
        config.read(path)
        return config[section][param]

    def get_all_config_param(path,section):
        config = configparser.ConfigParser()
        config.read(path)
        return config[section]

    def get_all_config(path):
        config = configparser.ConfigParser()
        config.read(path)
        return config

    def update_config_param(path,section, param, value):
        config = configparser.ConfigParser()
        config.read(path)
        config[section][param] = value
        with open(path, 'w') as configfile:
            config.write(configfile)
    
    def create_config_file(path):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'file_path': 'dataset/sms_senior.csv',
                            'file_path_json': 'dataset/sms_senior.json',
                            'file_path_json_treated': 'dataset/sms_senior_treated.json',
                            'file_path_json_sentiment': 'dataset/sms_senior_sentiment.json',
                            'reset_json': 'True',
                            'reset_json_treated': 'True'}
        config['MODELS'] = {'sentiment': 'True'}
        config['API'] = {'host': '127.0.0.1', 'port': '8000'}
        with open(path, 'w') as configfile:
            config.write(configfile)
