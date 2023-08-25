<h2>Semana 3 | Criação de uma aplicação protegida com CRUD</h2>

O presente diretório é destinado à entrega da atividade referente à aplicação do tipo To-do List.

<h3>Introdução à atividade</h3>

<p>Esta atividade tem por objetivo desenvolver um projeto web que possibilite os usuários registrarem dados em um banco de dados. O deploy do banco, da API do back-end e do front-end deve acontecer utilizando uma aplicação com múltiplos containers. A aplicação não precisa utilizar frameworks, pode ser realizada utilizando os primitivos presentes na linguagem de programação escolhida. O projeto consiste em um To-do List, em que o usuário deve se cadastrar no sistema para ter acesso às suas notas e adicionar novas notas.</p>

<h3>Implementação</h3>

<p>Para a realização da atividade, foram escolhidas as ferramentas descritas abaixo.</p>

<p><li><b>Flask:</b> constitui um framework Python para desenvolvimento web. No contexto da atividade, foi utilizado para a construção da API que interage com a interface construída.</p>

<p><li><b>SQLAlchemy:</b> foi a biblioteca de mapeamento objeto-relacional (ORM) escolhida. Permite interagir com bancos de dados relacionais, fornecendo o suporte necessário para gerenciar os dados da aplicação desenvolvida. Normalmente, é utilizado em conjunto com o Flask.</p>

<p><li><b>PostgreSQL:</b> é um sistema de gerenciamento de banco de dados relacional e licença open-source. No que concerne à atividade, foi escolhido para fins de aprendizado da tecnologia. Sua escolha justifica-se, também, pela praticidade de uso que apresenta quando integrado a frameworks de Python.</p>

<p><li><b>Semantic UI:</b> o framework destina-se a fornecer suporte para o design de interface de usuário. Apresenta facilidade de uso para a estilização de páginas web, proporcionando a criação de interfaces coesas e bem estruturadas. Devido a seus princípios semânticos, foi escolhido para estilizar os templates HTML desenvolvidos.</p>

<h4>Autenticação de login</h4>

<p>A fim de atender a um dos requisitos da atividade — a autenticação de login —, foi utilizado o <b>bcrypt</b>, uma ferramenta de criptografia do tipo hash para senhas. Para concretizar a autenticação de login e redirecionar o usuário para a página da to-do list, a senha em formato hash disposta no banco de dados é comparada à senha submetida pelo usuário no ato do login. Dessa forma, torna-se possível liberar a rota seguinte ou, caso a senha providenciada não corresponda à senha contida no registro do usuário, retornar uma mensagem de senha inválida.</p>

<h4>Fluxo da aplicação</h4>

<p>A primeira tela com a qual o usuário terá contato será a de registro. Uma vez que o usuário digita o e-mail e a senha que deseja cadastrar na aplicação, os dados são inseridos no banco de dados. Para isso, a senha inserida passa pelo processo de criptografia e, juntamente ao e-mail, é enviada ao banco de dados PostgreSQL através da ferramenta SQLAlchemy. Posteriormente, o usuário é redirecionado à página de login da aplicação, em que deve novamente inserir os dados registrados. Se o login for devidamente autenticado, o acesso à página de tarefas será bem-sucedido. Ao acessar a to-do list, por fim, o usuário torna-se capaz de inserir, visualizar, modificar e deletar tarefas, as quais estarão igualmente inseridas em um banco de dados.</p>

<h4>Containerização</h4>

<p>A containerização dos componentes da aplicação construída ainda está pendente. Infelizmente, tive muitos impedimentos para finalizar essa parte dentro do prazo estipulado! :/</p>

<h3>Estrutura de pastas</h3>

<p>Abaixo, encontra-se a estrutura de pastas da atividade.</p>

:file_folder: &nbsp; templates<br>
&nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; login.html<br>
&nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; register.html<br>
&nbsp; &nbsp; &nbsp; :page_with_curl: &nbsp; todo.html<br>
:page_with_curl: &nbsp; app.py<br>
:page_with_curl: &nbsp; docker-compose.yml<br>
:page_with_curl: &nbsp; Dockerfile<br>
:page_with_curl: &nbsp; README.md<br>
:page_with_curl: &nbsp; requirements.txt<br>