<h2>Instanciando aplicações em serviços AWS</h2>

<p>O presente arquivo destina-se a anotações e estudos relacionados ao processo de deploy de aplicações em serviços AWS.</p>

<h3>EC2 (Elastic Compute Cloud)</h3>

Para instanciar uma máquina EC2, podemos utilizar as configurações dispostas abaixo.

<li>Amazon Machine Image (AMI): Ubuntu Server 22.04
<li>Instance type: t2.micro (1vCPU 1 GiB)
<li>Key pair: M7-Inteli-Keys

**Newtork Settings**

<li>Allow SSH traffic from anywhere
<li>Allow HTTPS traffic from the internet
<li>Allow HTTP traffic from the internet

**Configure Storage**

Utilizar a configuração default.

**Elastic IP**

É possível alocar um IP elástico à instância EC2 criada. Para isso, basta indicar a instância e o endereço de IP privado.

<h3>RDS (Relational Database Service)</h3>

**Engine Options**

<li>PostgreSQL: opção de engine selecionada
<li>Free tier: template escolhido
<li>DB instance identifier: nome para identificar a instância criada
<li>Master username: nome escolhido para o banco de dados
<li>Auto generate a password
<li>Instance configuration: db.t3.micro
<li>Storage: default values
<li>Connectivity: é possível conectar com uma instância EC2
<li>Default VPC
<li>Public access: sim
<li>Database port: 5432
<li>Password authentication

<h3>Construindo o ambiente para hospedar a aplicação</h3>

Abaixo, encontram-se instruções relacionadas às etapas necessárias para construir o ambiente em que a aplicação será executada. Supõe-se, para esse caso, uma aplicação 

1. Criar uma instância da API no EC2
2. Associar um IP elástico à instância da API
3. Criar uma instância do banco de dados no RDS
4. Estabelecer a conexão entre o banco de dados e a máquina EC2
5. Criar uma segunda instância no EC2 para o front-end
6. Configurar o servidor web Apache para servir o front-end
7. Configurar o front-end para consumir a API na primeira instância EC2 criada
8. As chamadas da API devem estar direcionadas para o endpoint correto da instância que hospeda a API
9. Estabelecer as configurações de segurança para permitir que a API acesse o banco de dados
10. Testar a aplicação por meio do front-end, que pode ser acessado pelo endereço IP
11. Certificar a conexão entre API e banco de dados (verificar se é possível alimentar a tabela)