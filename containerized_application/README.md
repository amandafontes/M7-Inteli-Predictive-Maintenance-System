<h2>Semana 1 | Aplicação containerizada</h2>

O presente diretório é destinado à entrega da atividade referente à aplicação containerizada.

<h4>Introdução à atividade</h4>

<p>Este autoestudo tem por objetivo verificar se o estudante consegue criar uma aplicação e um container para executá-la. Espera-se que os estudantes possam criar suas imagens e descrever o que foi necessário para realizar seu desenvolvimento. Espera-se ainda que os estudantes possam buscar as informações complementares para o desenvolvimento da aplicação.</p>

<h4>Implementação</h4>

<p>O primeiro passo para a implementação da atividade foi criar um ambiente virtual denominado <code>container_environment</code>. Uma vez ativado o ambiente, foram feitas as instalações necessárias para a construção da aplicação, bem como a criação do arquivo <code>requirements.txt</code>. Para a concretização dessa etapa, foram necessários os seguintes passos:</p>

<p>Criação e ativação do ambiente virtual:</p>
<br>

```powershell
python -m venv container_environment
cd container_environment/Scripts
activate
```
<br>
<p>Instalação do framework utilizado para a construção da API:</p>
<br>

```powershell
pip install Flask
```
<br>

<p>Criação do arquivo de requerimentos do ambiente virtual:</p>
<br>

```powershell
pip freeze > requirements.txt
```
<br>

<p>Posteriormente, foi criada uma API simples utilizando Flask, um framework da linguagem Python. A rota criada chama a função <code>display_curriculum()</code>, responsável por retornar <index.html> — o arquivo em que foi construída a página estática referente ao currículo profissional. Abaixo, encontra-se o código da API.</p>
<br>

```python
from flask import Flask, render_template

app = Flask(__name__, '/static')

@app.route("/")
def display_curriculum():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
```
<br>

<p>O próximo passo é construir um arquivo Dockerfile. Um Dockerfile é composto por um conjunto de instruções capazes de gerar um ambiente isolado, em que será possível executar a aplicação criada dentro de um container. Abaixo, encontra-se o conteúdo do Dockerfile criado, considerando o uso do framework Flask.</p>
<br>

```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```
<br>

<p>Por fim, deve-se criar uma imagem utilizando o Docker. Posteriormente, a imagem deve ser inserida em seu repositório de destino no DockerHub. Para isso, os seguintes comandos devem ser executados:</p>
<br>

```	powershell
docker build -t <image_name> .
docker tag <image_name> <repository_name>/<image_name>
docker push <repository_name>/<image_name>
```
<br>

<p>Se o procedimento acima for bem-sucedido, a imagem poderá ser visualizada no DockerHub, assim como na demonstração abaixo:</p><br>

<p align="center"><img src=".\images\dockerhub.png" width="60%"></img></p><br>

<p>Por meio <a href="https://hub.docker.com/repository/docker/amandafontes/curriculum_application/general">deste link</a>, é possível acessar o repositório que criei para a atividade.</p><br>

<h4>Estrutura de pastas</h4>

:file_folder: &nbsp; containerized_application<br>
&nbsp; :file_folder: &nbsp; conteiner_environment<br>
&nbsp; :file_folder: &nbsp; images<br>
&nbsp; &nbsp; &nbsp; :file_folder: &nbsp; dockerhub.png<br>
&nbsp; :file_folder: &nbsp; static<br>
&nbsp; &nbsp; &nbsp; :file_folder: &nbsp; image.png<br>
&nbsp; &nbsp; &nbsp; &nbsp; templates<br>
&nbsp; &nbsp; &nbsp; :file_folder: &nbsp; index.html<br>
&nbsp; &nbsp; &nbsp; &nbsp; Dockerfile<br>
&nbsp; &nbsp; &nbsp; &nbsp; main.py<br>
&nbsp; &nbsp; &nbsp; &nbsp; README.md<br>
&nbsp; &nbsp; &nbsp; &nbsp; requirements.txt<br>