<html>
<body>
<h1>Requisitos:</h1>
  <a>Python 3.7 ou superior: <a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></a> <br>
  <a>pip: <a href="https://pip.pypa.io/en/stable/installation/">https://pip.pypa.io/en/stable/installation/</a></a><br>
  <a>PyTorch: <a href="https://pytorch.org/get-started/locally/">https://pytorch.org/get-started/locally/</a></a><br><br>
  <a>Obs: É sempre possivel que falte alguma biblioteca quando for rodar o comando do pip dentro do arquivo start.bat/sh fique atento a saida do prompt, geralmente tera o nome do modulo no final, indicando a falta do mesmo e para instalar basta utilizar o comando 'pip install <module>'.<br><br>
    
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
<p>Pronto agora sua aplicação esta rodando no endereço local "127.0.0.1:8000".</p>
    <h1>Configurações:</h1>
</body>
</html>



