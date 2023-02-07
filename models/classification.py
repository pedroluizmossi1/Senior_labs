import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

from core.config import Config

file_path = Config.get_config_param('config.ini','DEFAULT', 'file_path')

data = pd.read_csv(file_path, encoding='unicode_escape')

# Criar um vetor de recursos a partir do texto das mensagens
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(data['Full_Text'])

# Separar os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(features, data['IsSpam'], test_size=0.2)

# Treinar o classificador Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Avaliar a acurácia do modelo
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)

# Prever a classificação de uma nova mensagem
def get_classification(message):
    new_features = vectorizer.transform([message])
    prediction = clf.predict(new_features)
    score = clf.predict_proba(new_features)
    print("Classification:", prediction[0])
    series = pd.Series(prediction[0]).to_json(orient='records')
    #remove [] and \\ and " from string
    series = series.replace('[','').replace(']','').replace('\\','').replace('"','')
    return series

def get_score(message):
    new_features = vectorizer.transform([message])
    score = clf.predict_proba(new_features)
    print("Score:", score[0])
    return pd.Series(score[0]).to_json(orient='records')
