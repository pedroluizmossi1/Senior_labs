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
