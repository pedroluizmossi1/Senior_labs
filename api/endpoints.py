import pandas as pd
import json
import datetime
import requests
from fastapi import FastAPI, Request, Form

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from core.config import Config
from core.import_csv import CsvFile
from core.json_function import JsonFunctions
from models.sentiment import get_sentiment_score
from models.classification import get_classification, get_score
from core.data_analysis import DataAnalysis, DataPlot

api = FastAPI()

file_path_json_treated = Config.get_config_param('config.ini','DEFAULT', 'file_path_json_treated')
file_path_json_sentiment = Config.get_config_param('config.ini','DEFAULT', 'file_path_json_sentiment')
#config endpoints
@api.get("/config/all")
def get_all_config():
    config = Config.get_all_config('config.ini')
    return config

@api.get("/config/section/{section}")
def get_all_config_section(section):
    config = Config.get_all_config_param('config.ini',section)
    return config

@api.get("/config/section/{section}/param/{param}")
def get_config_param(section, param):
    config = Config.get_config_param('config.ini',section, param)
    return config

@api.post("/config/section/{section}/param/{param}")
def update_config_param(section, param, value):
    Config.update_config_param('config.ini',section, param, value)
    return "Config Updated"
########################################################################

@api.get("/file/import_csv/{file_path}")
def import_csv(file_path):
    try:
        df = CsvFile(file_path).import_csv()
        return df.to_json(orient='records')
    except:
        return "Error importing csv file"

@api.get("/file/import_csv/{file_path}/to_json/{file_path_json}")
def import_csv_to_json(file_path, file_path_json):
    try:
        JsonFunctions.convert_csv_to_json_file(file_path, file_path_json)
        return "CSV file imported to JSON"
    except:
        return "Error importing csv file"

@api.get("/file/import_csv/{file_path}/to_json/{file_path_json}/treated/{file_path_json_treated}")
def import_csv_to_json_treated(file_path, file_path_json, file_path_json_treated):
    try:
        json_file = JsonFunctions.read_json_file(file_path_json)
        json_treated = JsonFunctions.treat_json_data(json_file)
        JsonFunctions.save_json_file(json_treated, file_path_json_treated)
        return "CSV file imported to JSON and treated"
    except:
        return "Error importing csv file"

@api.get("/file/import_csv/to_json/treated/{file_path_json_treated}/sentiment/{file_path_json_sentiment}")
def import_csv_to_json_treated_sentiment(file_path_json_treated, file_path_json_sentiment):
    try:
        json_file = JsonFunctions.read_json_file(file_path_json_treated)
        json_sentiment = JsonFunctions.append_sentiment_to_json_file(json_file, file_path_json_sentiment)
        return "CSV file imported to JSON and treated and sentiment added"
    except:
        return "Error importing csv file"

@api.post("/file/import_csv/to_json/treated/sentiment/default")
def import_csv_to_json_treated_sentiment_default(sentiment: bool):
    file_path = "dataset/sms_senior.csv"
    file_path_json = "dataset/sms_senior.json"
    file_path_json_treated = "dataset/sms_senior_treated.json"
    file_path_json_sentiment = "dataset/sms_senior_sentiment.json"
    try:
        JsonFunctions.convert_csv_to_json_file('import',file_path, file_path_json)
        json_file = JsonFunctions.read_json_file('import',file_path_json)
        json_treated = JsonFunctions.treat_json_data('import',json_file)
        JsonFunctions.save_json_file('import',json_treated, file_path_json_treated)
        if sentiment == True:
            for i in range(len(json_file)):
                json_file[i]['Sentiment'] = get_sentiment_score(json_file[i]['Full_Text'])
                json_file[i]['Classification'] = get_classification(json_file[i]['Full_Text'])
                json_file[i]['Score'] = get_score(json_file[i]['Full_Text'])
                length = len(json_file)
                progress_bar = int((i/length)*100)
                print(progress_bar)
            JsonFunctions.append_sentiment_to_json_file('export_json',json_file, file_path_json_sentiment)
        return "CSV file imported to JSON and treated and sentiment added"
    except Exception as e:
        print(e)
        return e

@api.get("/data_analysis/word_count/{file_path_json_treated}")
def get_word_count(file_path_json_treated):
    word_count = DataAnalysis.get_word_count('export_json',file_path_json_treated)
    return word_count

@api.get("/data_analysis/word_count_statistics/{file_path_json_treated}")
def get_word_count_statistics(file_path_json_treated):
    word_count_statistics = DataAnalysis.get_word_count_statistics('export_json',file_path_json_treated)
    return word_count_statistics

@api.get("/data_analysis/word_count_statistics_by_mouth/{file_path_json_treated}")
def get_word_count_statistics_by_mouth(file_path_json_treated):
    word_count_statistics_by_mounth = DataAnalysis.get_word_count_statistics_by_mouth('export_json',file_path_json_treated)
    return word_count_statistics_by_mounth

@api.get("/data_analysis/messages_count_by_mouth/{file_path_json_treated}")
def get_messages_count_by_mouth(file_path_json_treated):
    messages_by_mounth = DataAnalysis.get_messages_count_by_mouth('export_json',file_path_json_treated, False)
    return messages_by_mounth

@api.get("/data_analysis/spam_count_by_mouth/{file_path_json_treated}")
def get_spam_count_by_mouth(file_path_json_treated):
    spam_by_mounth = DataAnalysis.get_messages_count_by_mouth('export_json',file_path_json_treated, True)
    return spam_by_mounth

@api.get("/data_analysis/messages_count_by_day/{file_path_json_treated}")
def get_messages_count_by_day(file_path_json_treated):
    messages_count_by_day = DataAnalysis.get_messages_count_by_day('export_json',file_path_json_treated)
    return messages_count_by_day

@api.get("/classification/naive_bayes/{message}")
def naive_bayes(message: str):
    return get_classification(message)

@api.post("/message/{message}")
async def create_message(message: str):
    data = {'Full_Text': message, 'Word_Count':0, 'Date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'IsSpam': get_classification(message), 'Sentiment': get_sentiment_score(message)}
    data_no_sentiment = {'Full_Text': message, 'Word_Count':0, 'Date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'IsSpam': get_classification(message)}
    JsonFunctions.append_new_message_to_json_file('export_json',data, file_path_json_sentiment)
    JsonFunctions.append_new_message_to_json_file('export_json',data_no_sentiment, file_path_json_treated)
    return data

api.mount("/static", StaticFiles(directory="api/static"), name="static")
templates = Jinja2Templates(directory="api/templates")

@api.get("/", response_class=HTMLResponse)
async def root( request: Request):
    word_count = DataAnalysis.get_word_count('export_json',file_path_json_treated)
    word_count_by_mounth = DataAnalysis.get_word_count_by_mouth('export_json',file_path_json_treated)
    message_count_by_mounth = DataAnalysis.get_messages_count_by_mouth('export_json',file_path_json_treated, False)
    spam_count_by_mounth = DataAnalysis.get_messages_count_by_mouth('export_json',file_path_json_treated, True)
    word_count_statistics_by_mouth = DataAnalysis.get_word_count_statistics_by_mouth('export_json',file_path_json_treated)
    messages_count_by_day = DataAnalysis.get_messages_count_by_day('export_json',file_path_json_treated)
    print(word_count_statistics_by_mouth)
    return templates.TemplateResponse("index.html", context={"request": request, 
                                                            "word_count": word_count, 
                                                            "word_count_by_mounth": word_count_by_mounth, 
                                                            "message_count_by_mounth": message_count_by_mounth, 
                                                            "spam_count_by_mounth": spam_count_by_mounth,
                                                            "word_count_statistics_by_mouth": word_count_statistics_by_mouth,
                                                            "messages_count_by_day": messages_count_by_day
                                                            })

@api.get("/messages", response_class=HTMLResponse)
async def messages( request: Request):
    data_messages = DataAnalysis.get_messages_text('export_json',file_path_json_sentiment)
    return templates.TemplateResponse("messages.html", context={"request": request, "messages": data_messages})

@api.post("/messages", response_class=HTMLResponse)
async def post_messages( request: Request, message: str = Form(...)):
    data = await request.form()
    message = data['message']
    data = {'Full_Text': message, 'Word_Count':0, 'Date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'IsSpam': get_classification(message), 'Sentiment': get_sentiment_score(message)}
    data_no_sentiment = {'Full_Text': message, 'Word_Count':0, 'Date': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'IsSpam': get_classification(message)}
    JsonFunctions.append_new_message_to_json_file('export_json',data, file_path_json_sentiment)
    JsonFunctions.append_new_message_to_json_file('export_json',data_no_sentiment, file_path_json_treated)
    data_messages = DataAnalysis.get_messages_text('export_json',file_path_json_sentiment)
    return templates.TemplateResponse("messages.html", context={"request": request, "messages": data_messages})
