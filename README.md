
 <h1>Projeto:</h1>
  <a> Seja bem vindo ao projeto Desafio - Data Science SL, esse projeto tem como intuito cumprir os requisitos e desafios propostos no material <a href="https://github.com/SeniorSA/seniorlabs-challenge/blob/main/data-science.md"> https://github.com/SeniorSA/seniorlabs-challenge/blob/main/data-science.md</a> oferecido pelo pessoal do Senior Labs. O projeto trata se de uma aplicação em python, tanto backend quanto frontend e que darei mais detalhes abaixo.</a> <br>
 <p align="center">
  <img src="https://github.com/pedroluizmossi1/Senior_labs/blob/main/giphy.gif" width="750" />
</p>
<br>
<p> Você pode acessar uma versão da aplicação hospedada na AWS atraves do Link <a href="http://52.91.182.218:8000/">http://52.91.182.218:8000/</a>

<h1>Python e Seus Pacotes:</h1>
<p> O projeto se sustenta na linguagem Python, usando e abusando de suas packages, no backand temos o 'configparser' para o nosso arquivo de configurações, utilizei o 'pandas' para ler o arquivo csv do desafio, temos o 'json' padrão do próprio Python para lidar com a conversões do arquivo csv e diversas funções na hora de chamar os dados e salvar.</p> <br>

<p> Em relação ao frontend, optei pelo 'FastAPI', não por ser bom em criar um frontend mas por que tive a ideia de disponibilizar as funções do sistema via API e por ele ter uma certa integração com o 'Jinja' o que facilitaria um pouco a criação da interface Web, essa que foi disponizilada através do 'uvicorn' é claro que o intuito do projeto é a analise dos dados por isso preferi mostrar atraves de graficos/planilhas no navegador para facilitar a visualização dos mesmos e permitir alguma interatividade como o cadastro de novas mensagens e como elas refletem em tempo real nos gráficos assim como demonstrar a utilização de dois modelos de análise. </p>  <br>

<p>Resumidamente utilizei dois modelos de análise, um para definir se a mensagem é um Spam como pedia o desafio e outro para classificar o sentimento das mensagens em "positiva", "neutra" ou "negativa". 

Para criar o modelo que classifica se uma mensagem é Spam ou não, foi preciso um pouco de pesquisa principalmente por nunca ter feito isto. Mas encontrei alguns artigos que vou deixar no final da página que serviram e foram utilizados como base para criar o código, utilizando o algoritmo Naive Bayes, 'scikit-learn' o código foi capaz de treinar e classificar uma nova mensagem, para o treinamento utilizei o mesmo arquivo csv do desafio, já que ele possui uma base já classificada de mensagens.

Para a classificação de sentimento foi mais tranquilo, já que não era pedido pelo desafio tomei a liberade de "adaptar" hehehe o código presente no https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest, essa inclusive foi uma das questões que me levaram a utilizar os arquivos do desafio em JSON ao inves do arquivo csv original e como no exemplo abaixo.

<pre>
{
        "Full_Text": "Hey! Congrats 2u2. id luv 2 but ive had 2 go home!",
        "hey": 1,
        "home": 1,
        "ive": 1,
        "Common_Word_Count": 3,
        "Word_Count": 12,
        "Date": "2017-01-01 00:08:00",
        "IsSpam": "no",
        "Sentiment": {
            "positive": "0.9796274",
            "neutral": "0.016392197",
            "negative": "0.0039804312"
        }
    },
    {
        "Full_Text": "came to look at the flat, seems ok, in his 50s? * Is away alot wiv work. Got woman coming at 6.30 too.",
        "got": 1,
        "work": 1,
        "coming": 1,
        "Common_Word_Count": 3,
        "Word_Count": 23,
        "Date": "2017-01-01 00:19:00",
        "IsSpam": "no",
        "Sentiment": {
            "neutral": "0.72847307",
            "positive": "0.25450087",
            "negative": "0.017026067"
        }
    },
</pre>

Sei que eu poderia ter utilizado a mesma estrutura em um arquivo csv tranquilamente apenas adicionando as 3 colunas no final do arquivo, mas dessa maneira achei mais organizado e fácil de retornar como uma resposta para a API. 
</p>


<h1>Requisitos:</h1>
  <a>Python 3.7 ou superior: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></a> <br>
  <a>pip: <a href="https://pip.pypa.io/en/stable/installation/">https://pip.pypa.io/en/stable/installation/</a></a><br>
  <a>PyTorch: <a href="https://pytorch.org/get-started/locally/">https://pytorch.org/get-started/locally/</a></a><br><br>
  <a>Obs: É sempre possivel que falte alguma biblioteca quando for rodar o comando do pip dentro do arquivo start.bat/sh fique atento a saida do prompt, geralmente terá o nome do modulo no final, indicando a falta do mesmo e para instalar basta utilizar o comando 'pip install <module>'.<br><br>
    
<h1>Primeiros Passos:</h1>
<p>Após concluir a instalação dos requisitos, basta executar a aplicação no arquivo:</p>
<h3>start.bat windows</h3>
<p>ou</p>
<h3>start.sh linux</h3>
<p>O prompt de saída no terminal aberto deve ser parecido com este:</p>
<pre>
INFO:     Will watch for changes in these directories: ['C:\\Users\\Pedro\\Desktop\\Senior']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [35692] using StatReload
Some weights of the model checkpoint at cardiffnlp/twitter-roberta-base-sentiment-latest were not used when initializing RobertaForSequenceClassification: ['roberta.pooler.dense.weight', 'roberta.pooler.dense.bias']
- This IS expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Accuracy: 0.9829596412556054
INFO:     Started server process [28412]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
</pre>
<h3>Pronto agora sua aplicação esta rodando no endereço local "127.0.0.1:8000", basta ir no navegador e colar o endereço para acessar a aplicação.</h3>
    <h1>Configurações:</h1>
    <p> O arquivo de configurações se encontra na raiz do diretório com o nome de config.ini.</p>
    
   <pre>
[DEFAULT]
file_path = dataset/sms_senior.csv      #Caminho do arquivo csv com os dados iniciais do desafio.
file_path_json = dataset/sms_senior.json      #Caminho do arquivo JSON com os dados do arquivo csv.
file_path_json_treated = dataset/sms_senior_treated.json      #Caminho do arquivo JSON tratado para a retirada de palavras sem valor.
file_path_json_sentiment = dataset/sms_senior_sentiment.json      #Caminho do arquivo JSON tratado e com sentimentos adicionados.
reset_json = False or True     #Esta opção cria/refaz o arquivo sms_senior.json. !importante para o funcinamento da aplicação
reset_json_treated = False or True      #Esta opção cria/refaz o arquivo sms_senior_treated.json. !importante para o funcinamento da aplicação

[MODELS]
sentiment = False      #Esta opção cria/refaz o arquivo sms_senior_treated.json. !importante para o funcinamento da aplicação e pode levar varios minutos para criar o arquivo dependendo do seu hardware.

[API]
host = 127.0.0.1      #Endereço de escuta/acesso da aplicação.
port = 8000 #Porta de acesso da aplicação.
</pre>
<h1>Pasta Data:</h1>
<p> Dentro da pasta "data" temos os arquivos em formato JSON dos desafios propostos. Estes arquivos tem apenas o propósito de serem consultados rapidamente a fim de checar alguma infomação. </p>
    
 <h1>Duvidas e Contato:</h1>
    <p>Qualquer dúvida pode ser enviada aqui diretamente na pagina do repositório.</p>
    <h2>Ass: Pedro Mossi</h2>
</body>
</html>



