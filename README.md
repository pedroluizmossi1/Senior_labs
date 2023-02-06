<html>
<body>
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



