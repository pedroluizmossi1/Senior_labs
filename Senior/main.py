import threading
import gradio as gr

from core.import_csv import CsvFile
from core.config import Config
from core.json_function import JsonFunctions
from core.data_analysis import DataAnalysis, DataPlot
from models.sentiment import get_sentiment_score
from api.endpoints import api

config_file = 'config.ini'

#Default Config
config_csv = Config.get_config_param(config_file,'DEFAULT', 'file_path')
config_json = Config.get_config_param(config_file,'DEFAULT', 'file_path_json')
config_json_treated = Config.get_config_param(config_file,'DEFAULT', 'file_path_json_treated')
reset_json = Config.get_config_param(config_file,'DEFAULT', 'reset_json')
reset_json_treated = Config.get_config_param(config_file,'DEFAULT', 'reset_json_treated')

#Models Config
sentiment_config = Config.get_config_param(config_file,'MODELS', 'sentiment')

#API Config
api_host = Config.get_config_param(config_file,'API', 'host')
api_port = Config.get_config_param(config_file,'API', 'port')

def main():

    if reset_json == 'True':
        JsonFunctions.convert_csv_to_json_file('export_json',config_csv, config_json)
        Config.update_config_param(config_file,'DEFAULT', 'reset_json', 'False')
    if reset_json_treated == 'True':
        json_file = JsonFunctions.read_json_file('export_json',config_json)
        json_treated = JsonFunctions.treat_json_data('export_json',json_file)
        JsonFunctions.save_json_file('export_json',json_treated, config_json_treated)
        Config.update_config_param(config_file,'DEFAULT', 'reset_json_treated', 'False')

    if sentiment_config == 'True':
        for i in range(len(json_file)):
            json_file[i]['Sentiment'] = str(get_sentiment_score(json_file[i]['Full_Text']))
            progress_bar = (i, len(json_file))
            print(progress_bar)
        JsonFunctions.append_sentiment_to_json_file('export_json',json_file, config_json_treated)
        Config.update_config_param(config_file,'MODELS', 'sentiment', 'False')


    word_count = DataAnalysis.get_word_count('export_json',config_json_treated)    
    messages_by_mounth = DataAnalysis.get_messages_count_by_mouth('export_json',config_json_treated, False)
    spam_by_mounth = DataAnalysis.get_messages_count_by_mouth('export_json',config_json_treated, True)
    word_count_statistics_by_mounth = DataAnalysis.get_word_count_statistics_by_mouth('export_json',config_json_treated)
    messages_count_by_day = DataAnalysis.get_messages_count_by_day('export_json',config_json_treated)


if __name__ == "__main__":
    main()
    api.run(host=api_host, port=api_port)



