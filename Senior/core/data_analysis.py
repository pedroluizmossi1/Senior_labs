from core.json_function import JsonFunctions
from models.sentiment import get_sentiment_score
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from operator import itemgetter
import numpy as np

plt.style.use('_mpl-gallery')


class DataAnalysis():

    def __init__(self):
        pass

    def get_word_count(self, json_file_path):
        json_data = JsonFunctions.read_json_file('export_json',json_file_path)
        key_dict = {}
        for i in range(len(json_data)):
            json_data[i] = {k: v for k, v in json_data[i].items() if v != 0}
            keys = list(json_data[i].keys())
            for j in range(len(keys)):
                #exclude the Full_Text key, Word_Count, Date, IsSpam
                if keys[j] == 'Full_Text' or keys[j] == 'Word_Count' or keys[j] == 'Date' or keys[j] == 'IsSpam' or keys[j] == 'Common_Word_Count' or keys[j] == 'Sentiment':
                    continue
                else:
                    #if the key is not in the dictionary, add it with counted value
                    if keys[j] not in key_dict:
                        key_dict[keys[j]] = 1
                    else:
                        key_dict[keys[j]] += 1
        sort_dict = dict(sorted(key_dict.items(), key=itemgetter(1), reverse=True))
        return sort_dict

    def get_messages_count_by_mouth(self, json_file_path, is_spam = False):
        json_data = JsonFunctions.read_json_file('export_json',json_file_path)
        key_dict = {}
        for i in range(len(json_data)):
            #count the messages from Is Spam column and group them by mouth
            if is_spam == True:
                if json_data[i]['IsSpam'] == 'yes':
                    if json_data[i]['Date'][:7] not in key_dict:
                        key_dict[json_data[i]['Date'][:7]] = 1
                    else:
                        key_dict[json_data[i]['Date'][:7]] += 1
            else:
                if json_data[i]['Date'][:7] not in key_dict:
                    key_dict[json_data[i]['Date'][:7]] = 1
                else:
                    key_dict[json_data[i]['Date'][:7]] += 1

        return key_dict

    def get_word_count_statistics(self, json_file_path):
        json_data = JsonFunctions.read_json_file('export_json',json_file_path)
        #get the word count key from the json file
        word_count = []
        for i in range(len(json_data)):
            word_count.append(json_data[i]['Word_Count'])
        #get the min,max, mean, median, standard deviation, variance
        min = np.min(word_count)
        max = np.max(word_count)
        mean = np.mean(word_count)
        median = np.median(word_count)
        std = np.std(word_count)
        var = np.var(word_count)
        return min, max, mean, median, std, var

    def get_word_count_statistics_by_mouth(self, json_file_path):
        json_data = JsonFunctions.read_json_file('export_json',json_file_path)
        #get the word count key from the json file
        word_count = []
        #get the min,max, mean, median, standard deviation, variance for each mouth
        min = {}
        max = {}
        mean = {}
        median = {}
        std = {}
        var = {}
        for i in range(len(json_data)):
            if json_data[i]['Date'][:7] not in min:
                min[json_data[i]['Date'][:7]] = [json_data[i]['Word_Count']]
                max[json_data[i]['Date'][:7]] = [json_data[i]['Word_Count']]
                mean[json_data[i]['Date'][:7]] = [json_data[i]['Word_Count']]
                median[json_data[i]['Date'][:7]] = [json_data[i]['Word_Count']]
                std[json_data[i]['Date'][:7]] = [json_data[i]['Word_Count']]
                var[json_data[i]['Date'][:7]] = [json_data[i]['Word_Count']]
            else:
                min[json_data[i]['Date'][:7]].append(json_data[i]['Word_Count'])
                max[json_data[i]['Date'][:7]].append(json_data[i]['Word_Count'])
                mean[json_data[i]['Date'][:7]].append(json_data[i]['Word_Count'])
                median[json_data[i]['Date'][:7]].append(json_data[i]['Word_Count'])
                std[json_data[i]['Date'][:7]].append(json_data[i]['Word_Count'])
                var[json_data[i]['Date'][:7]].append(json_data[i]['Word_Count'])
        for key in min:
            min[key] = np.min(min[key])
            max[key] = np.max(max[key])
            mean[key] = np.mean(mean[key])
            median[key] = np.median(median[key])
            std[key] = np.std(std[key])
            var[key] = np.var(var[key])
        return {'min': min, 'max': max, 'mean': mean, 'median': median, 'std': std, 'var': var}

    def get_messages_count_by_day(self, json_file_path, is_spam = False):
        json_data = JsonFunctions.read_json_file('export_json',json_file_path)
        key_dict = {}
        for i in range(len(json_data)):
            if is_spam == True:
                if json_data[i]['IsSpam'] == 'yes':
                    if json_data[i]['Date'][:10] not in key_dict:
                        key_dict[json_data[i]['Date'][:10]] = 1
                    else:
                        key_dict[json_data[i]['Date'][:10]] += 1
            else:
                if json_data[i]['Date'][:10] not in key_dict:
                    key_dict[json_data[i]['Date'][:10]] = 1
                else:
                    key_dict[json_data[i]['Date'][:10]] += 1

        return key_dict

    def get_messages_text(self, json_file_path):
        json_data = JsonFunctions.read_json_file('export_json',json_file_path)
        return json_data

class DataPlot():
    def __init__(self):
        pass

    def plot_word_cloud(self, values):
        wordcloud = WordCloud().generate_from_frequencies(values)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    def plot_bar_chart(self, values):
        #plot the bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(range(len(values)), list(values.values()), align='center')
        plt.xticks(range(len(values)), list(values.keys()))
        plt.show()

    def plot_line_chart(self, values):
        #plot the line chart
        plt.figure(figsize=(10, 5))
        plt.plot(list(values.keys()), list(values.values()))
        plt.show()

    def plot_pie_chart(self, values):
        #plot the pie chart
        plt.figure(figsize=(10, 5))
        plt.pie(list(values.values()), labels=list(values.keys()), autopct='%1.1f%%')
        plt.show()

    def stacked_bar_chart(self, values1, values2):
        #plot the stacked bar chart
        plt.figure(figsize=(10, 5))
        plt.bar(range(len(values1)), list(values1.values()), align='center', label='Not Spam')
        plt.bar(range(len(values2)), list(values2.values()), align='center', label='Spam')
        plt.xticks(range(len(values1)), list(values1.keys()))
        plt.legend()
        plt.show()