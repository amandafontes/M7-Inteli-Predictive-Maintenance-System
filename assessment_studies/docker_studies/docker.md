<h2>Containerização de aplicações utilizando Docker</h2>

<p>O presente arquivo destina-se a anotações e estudos relacionados ao processo de containerização de aplicações por meio do Docker.</p>

<h3>Instruções iniciais</h3>

<p>O primeiro passo é executar o Docker Desktop. O status do Docker Daemon deve exibir "engine running" para que o login seja bem-sucedido. Abaixo, encontra-se descrito o procedimento básico para criar e rodar uma imagem Docker.</p>

<p>Para realizar o login:</p>

```powershell
docker login
```

<p>Para criar e nomear uma imagem:</p>

```powershell
docker build -t <nome da imagem> .
```

<p>Para criar e nomear uma imagem:</p>

```powershell
docker build -t <nome da imagem> .
```

<p>Para executar a imagem do Docker:</p>

```powershell
docker run <nome da imagem>
```

<h3>Comandos úteis</h3>

<p>Abaixo, encontram-se descritos alguns comandos úteis para a utilização do Docker.</p>

<p>Para listar as imagens existentes no Docker:</p>

```powershell
docker image ls
```

<p>Para excluir uma determinada imagem:</p>

```powershell
docker image rm <nome da imagem>
```

<p>Para excluir todas as imagens existentes:</p>

```powershell
docker image rm $(docker images -a -q)
```

<p>Para listar todos os containers existentes (em execução ou não):</p>

```powershell
docker ps -a
```

<p>Para listar todos os containers em execução:</p>

```powershell
docker container ls
```

<p>Para parar um container específico:</p>

```powershell
docker stop <nome da imagem>
```

<p>Para parar todos os containers em execução:</p>

```powershell
docker stop $(docker ps -a -q)
```

<p>Para excluir um container específico:</p>

```powershell
docker rm <nome do container>
```

<p>Para excluir todos os containers (caso estejam parados):</p>

```powershell
docker rm $(docker ps -a -q)
```

<p>Para exibir os logs de um container:</p>

```powershell
docker logs <nome do container>
```