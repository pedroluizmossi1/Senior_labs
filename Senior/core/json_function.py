import json
import os
import pandas as pd

from core.import_csv import CsvFile


class JsonFunctions():
    #convert csv to json

    def convert_csv_to_json(self, file_path):
        df = CsvFile(file_path).import_csv()
        return df.to_json(orient='records')

    def convert_csv_to_json_file(self, file_path, file_path_json):
        df = CsvFile(file_path).import_csv()
        df.to_json(orient='records', path_or_buf=file_path_json)
        json_file = open(file_path_json, 'r')
        json_data = json.load(json_file)
        return json_data

    def treat_json_data(self, json_data):
        for i in range(len(json_data)):
            #remove all the keys that have 0 values
            json_data[i] = {k: v for k, v in json_data[i].items() if v != 0}
        return json_data

    def save_json_file(self, json_data, file_path_json):
        with open(file_path_json, 'w') as outfile:
            json.dump(json_data, outfile)

    def read_json_file(self, file_path_json):
        json_file = open(file_path_json, 'r')
        json_data = json.load(json_file)
        return json_data

    def append_sentiment_to_json_file(self, json_data, file_path_json):
        with open(file_path_json, 'w') as outfile:
            json.dump(json_data, outfile)