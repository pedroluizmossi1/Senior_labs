import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Carregar dados de exemplo
data = pd.read_csv('models/sms_senior.csv', encoding='unicode_escape')

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
new_message = "Hello, how are you? here is Claudia from BANK OF AMERICA. I am calling to inform you that your account has been locked. Please call us at 1-800-123-4567 to unlock your account."
def classify(message):
    new_features = vectorizer.transform([message])
    prediction = clf.predict(new_features)
    print("Classification:", prediction[0])
    return prediction[0]
