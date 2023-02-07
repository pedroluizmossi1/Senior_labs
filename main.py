
import matplotlib.pyplot as plt

from core.import_csv import CsvFile
from core.config import Config
from core.json_function import JsonFunctions
from core.data_analysis import DataAnalysis, DataPlot
from models.sentiment import get_sentiment_score
from models.classification import get_classification, get_score
from api.endpoints import api
from core.config import Config

config_file = 'config.ini'
#Default Config
config_csv = Config.get_config_param(config_file,'DEFAULT', 'file_path')
config_json = Config.get_config_param(config_file,'DEFAULT', 'file_path_json')
config_json_treated = Config.get_config_param(config_file,'DEFAULT', 'file_path_json_treated')
file_path_json_sentiment = Config.get_config_param(config_file,'DEFAULT', 'file_path_json_sentiment')
reset_json = Config.get_config_param(config_file,'DEFAULT', 'reset_json')
reset_json_treated = Config.get_config_param(config_file,'DEFAULT', 'reset_json_treated')
matplot_graph = Config.get_config_param(config_file,'DEFAULT', 'matplot_graph')
#Models Config
sentiment_config = Config.get_config_param(config_file,'MODELS', 'sentiment')

#API Config
api_host = Config.get_config_param(config_file,'API', 'host')
api_port = Config.get_config_param(config_file,'API', 'port')



if reset_json == 'True':
    JsonFunctions.convert_csv_to_json_file('export_json',config_csv, config_json)
    Config.update_config_param(config_file,'DEFAULT', 'reset_json', 'False')

if reset_json_treated == 'True':
    json_file = JsonFunctions.read_json_file('export_json',config_json)
    json_treated = JsonFunctions.treat_json_data('export_json',json_file)
    JsonFunctions.save_json_file('export_json',json_treated, config_json_treated)
    Config.update_config_param(config_file,'DEFAULT', 'reset_json_treated', 'False')

if sentiment_config == 'True':
    json_file = JsonFunctions.read_json_file('export_json',config_json_treated)
    for i in range(len(json_file)):
        json_file[i]['Sentiment'] = get_sentiment_score(json_file[i]['Full_Text'])
        json_file[i]['Classification'] = get_classification(json_file[i]['Full_Text'])
        json_file[i]['Score'] = get_score(json_file[i]['Full_Text'])
        length = len(json_file)
        progress_bar = int((i/length)*100)
        print(progress_bar)
    JsonFunctions.append_sentiment_to_json_file('export_json',json_file, file_path_json_sentiment)
    Config.update_config_param(config_file,'MODELS', 'sentiment', 'False')


word_count = DataAnalysis.get_word_count('word_count',config_json_treated)
messages_by_mounth = DataAnalysis.get_messages_count_by_mouth('messages_by_mounth',config_json_treated, False)
spam_by_mounth = DataAnalysis.get_messages_count_by_mouth('spam_by_mounth',config_json_treated, True)
word_count_statistics_by_mounth = DataAnalysis.get_word_count_statistics_by_mouth('word_count_statistics_by_mounth',config_json_treated)
messages_count_by_day = DataAnalysis.get_messages_count_by_day('messages_count_by_day',config_json_treated)

JsonFunctions.save_json_file('export_json',word_count, 'data/word_count.json')
JsonFunctions.save_json_file('export_json',[messages_by_mounth, spam_by_mounth], 'data/messages_by_mounth.json')
JsonFunctions.save_json_file('export_json',word_count_statistics_by_mounth, 'data/word_count_statistics_by_mounth.json')
JsonFunctions.save_json_file('export_json',messages_count_by_day, 'data/messages_count_by_day.json')

if matplot_graph == 'True':
    DataPlot.plot_bar_chart('word_count',word_count)
    DataPlot.plot_bar_chart('messages_by_mounth',messages_by_mounth)
    DataPlot.plot_bar_chart('spam_by_mounth',spam_by_mounth)
    DataPlot.plot_bar_chart('word_count_statistics_by_mounth',word_count_statistics_by_mounth)
    DataPlot.plot_bar_chart('messages_count_by_day',messages_count_by_day)
    plt.show()





