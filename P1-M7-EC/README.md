<h2>Atividade Prática | P1 do Módulo 7</h2>

<p>A atividade tem por objetivo a elaboração dos arquivos necessários para configurar a containerização dos componentes de uma aplicação.</p>

<h3>Implementação</h3>

<p>Primeiramente, foi necessário construir um arquivo Dockerfile para o diretório <code>frontend</code> e um arquivo Dockerfile para o diretório <code>backend</code>. Cada Dockerfile se faz necessário para a construção das imagens que utilizaremos em cada container. Dessa forma, entende-se que deve haver um Dockerfile para a API desenvolvida em Python, bem como para o banco de dados em SQLite, e também um arquivo semelhante para a interface da aplicação, desenvolvida em Node.</p>

<p>O arquivo <code>docker-compose.yml</code> se faz necessário, por fim, para que a interdependência entre os containers seja concretizada, de modo que não seja preciso lançar um container por vez.</p>

<p>Para a implementação dos procedimentos descritos acima, foi necessária a construção de cada uma das imagens (Dockerfiles). Posteriormente, foi construído o arquivo docker-compose, o qual descreve o nome da imagem destinada a seu respectivo container, a porta utilizada por cada componente, a versão da aplicação e demais configurações. Para executar a aplicação, por fim, foi necessário executar o comando <code>docker-compose up</code>.</p>

<p>Ao final, teremos uma aplicação composta por dois containers: <code>api-container</code> e <code>database-container</code>.</p>