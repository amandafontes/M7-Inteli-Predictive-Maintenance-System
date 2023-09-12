<h2>Deploy de modelo de Machine Learning na nuvem</h2>

O presente diretório é destinado à entrega da atividade ponderada da semana 6.

<h4>Introdução à atividade</h4>

<p>Construção e deploy de um modelo de predição ou classificação criados pelos alunos. Este modelo deve ser deployado em uma nuvem comercial e uma API de acesso a ele deve ser desenvolvida.</p>

<h4>Implementação</h4>

<p>O primeiro passo para a implementação da atividade foi a criação de um arquivo <code>.ipynb</code> para desenvolver o modelo de Machine Learning. Foi criado um modelo de classificação para a predição de clima, que utiliza como base o dataset disponível <a href="https://www.kaggle.com/datasets/ananthr1/weather-prediction">neste link</a>. Após análises realizadas a partir da aplicação de ferramentas do <code>Pycaret</code>, foi possível concluir que o algoritmo que melhor performou sobre os dados foi o <code>Ridge Classifier</code>.</p>

<p>Posteriormente, foi criada uma API em <code>FastAPI</code> para servir o modelo. O script conta com uma rota <code>post</code>, que torna possível testar o modelo de classificação ao inserir os dados necessários para o retorno do modelo.</p>

<p>Por fim, a API construída foi containerizada e sua imagem foi inserida em um repositório no Docker Hub. Para executar o container, basta acessar o repositório e utilizar os comandos abaixo.</p>

```powershell
docker pull amandafontes/predictive_model:predictive_model
```

```powershell
docker run -p 8000:80 amandafontes/predictive_model:predictive_model
```

<p>Uma vez que a aplicação é executada, torna-se possível acessá-la por meio do seguinte URL:</p>

```
127.0.0.1:8000/docs
```

<p>Dessa forma, é possível acessar a rota da API e testar o modelo preditivo.</p>