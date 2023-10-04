<h2>Semana 9 | Resenha de artigo</h2>

O presente diretório é destinado à entrega da última atividade ponderada do módulo, e caracteriza-se pela resenha de um artigo que relaciona Machine Learning e IoT.

<h3>Introdução à atividade</h3>

Esta atividade ponderada tem por objetivo realizar a construção de uma comparação com o que foi desenvolvido nas outras atividades ponderadas e o artigo lido durante o autoestudo da semana. Os alunos deverão fazer uma comparação do que foi implementado por eles, com o que foi proposto pelo artigo, comparando as similaridades e diferenças. A resenha não deve possuir mais que 1000 palavras, sendo que eventuais códigos utilizados para demonstração, não fazem parte desta contagem.

<a href="https://www.sciencedirect.com/science/article/pii/S235286481730247X">Machine learning for internet of things data analysis: a survey</a>

<h3>Resenha</h3>

O artigo "Machine learning for internet of things data analysis: a survey" apresenta um estudo referente à implementação de estratégias de machine learning para lidar com os dados gerados por sistemas de IoT. De acordo com os autores, o processamento inteligente e a análise do significativo volume de dados provenientes de soluções IoT caracteriza a chave para o desenvolvimento de dispositivos IoT inteligentes. O objetivo do estudo é explorar o uso do aprendizado de máquina enquanto ferramenta para encarar os desafios do mercado de IoT e, para isso, foi enfatizado o caso das cidades inteligentes.

A partir da introdução do artigo, é possível compreender que IoT representa, em termos gerais, qualquer dispositivo cuja conexão com a internet seja possível. Por essa razão, recebe um volume significativo de dados, e deve ser capaz de explorá-los a fim de extrair informações relevantes.

**Pontos importantes:**

<li>Ciência de dados é uma área que tem muito a contribuir com o aprimoramento de aplicações IoT.
<li>Nesse contexto, destacam-se campos científicos como mineração de dados, aprendizado de máquina e outras técnicas.
<li>O processo de análise de dados envolve os tipos de dados com os quais estamos lidando, os modelos que melhor se adaptam às circunstâncias do sistema e os algoritmos mais aplicáveis às características dos conjuntos de dados.

O estudo busca proporcionar uma série de contribuições à comunidade acadêmica. As perguntas respondidas pelo artigo são: como o aprendizado de máquina se aplica a smart data em IoT? Qual é a taxonomia dos algoritmos de aprendizado de máquina que podem ser aplicados em IoT? Quais são as características dos dados de IoT no mundo real? Por que as cidades inteligentes configuram um caso típico de uso de aplicações IoT?

Após discorrer sobre o conceito de IoT e sobre os diferentes frameworks da computação, os autores apresentam o conceito de cidades inteligentes com significativa riqueza de detalhes, evidenciando a aplicabilidade de soluções de Internet of Things nesse contexto.

**Características relevantes em dados de IoT:**

<li>Big data: volume, variedade e velocidade
<li>Qualidade dos dados: redundância, acurácia, dinamicidade e granularidade
<li>Uso dos dados: semântica, completude e ausência de ruídos

O próximo tópico explorado pelo estudo se refere à taxonomia dos algoritmos de machine learning. Nele, são discutidos conceitos importantes sobre aprendizado de máquina, bem como algoritmos frequentemente aplicados para a análise inteligente de dados. Além disso, os autores se aprofundam nos algoritmos mais utilizados, tanto no campo da classificação, quanto no da regressão, descrevendo as técnicas empregadas por cada estudo analisado.

Cabe destacar também que, ao discorrer sobre diferentes algoritmos em contextos variados, o estudo apresenta outros procedimentos da ciência de dados que são de extrema importância ao construir um modelo, como técnicas de pré-processamento, identificação de outliers, desbalanceamento de dados, seleção de features, otimização de performance, etc.

Por fim, é proposta uma discussão a respeito dos desafios enfrentados na área de análise de dados de IoT na atualidade. Nessa seção, destacam-se:

<li>A dificuldade ao equilibrar as características dos dados, de modo que haja uma limitação quanto à acurácia máxima alcançada por um modelo.
<li>Os processos de coleta de dados, que podem ser interferidos por aspectos como a privacidade dos dados e regras de negócio.
<li>O desafio de contemplar big data, sobretudo quando os dados obtidos são originados de diferentes fontes.

**Relação com o projeto**

Com base na leitura do artigo, é possível inferir que a temática central do estudo relaciona-se significativamente ao propósito do projeto desenvolvido ao longo do módulo 7. Em nosso projeto para a Azul Linhas Aéreas, foi projetado um sistema de manutenção preditiva para o sistema de Bleed Air das dezesseis aeronaves do modelo E2 de posse da companhia. Nesse caso, foram utilizados os dados puros provenientes dos sensores acoplados ao sistema de sangria das aeronaves. Uma vez extraídos os dados desse sistema, eles passaram por um processo de transformação a fim de que pudessem treinar um algoritmo de predição, cujo objetivo concentra-se em alertar o setor de manutenção sobre possíveis falhas no sistema das aeronaves antes que elas aconteçam.

Desse modo, o primeiro sistema de IoT com o qual a solução interage é o sistema responsável pela extração e codificação dos dados, ainda no interior da aeronave. A submissão dos dados ao modelo, por sua vez, ocorre por meio de uma plataforma web que possibilita a interação entre o usuário final do produto e a inteligência artificial construída.

Em projetos que relacionam ciência de dados e sistemas IoT, características importantes sobre os dados devem ser consideradas. No artigo, os autores indicam que dispositivos de cidades inteligentes geram dados de maneira contínua e coletam informações de múltiplas origens (gestão de tráfego, energia, saúde, etc). No contexto do projeto, os dados disponibilizados eram provenientes de diferentes sensores e possuíam diferentes tipos e especificidades que deveriam ser compreendidas anteriormente à construção do modelo de aprendizado de máquina. Nesse sentido, a característica dinâmica dos dados indica alguns pontos de preocupação relacionados à qualidade da informação (QoI). São eles: os erros quanto à medida ou precisão da coleta de dados, os ruídos presentes no ambiente do qual os dados são extraídos, e as medições provenientes de observação discreta.

Um dos exemplos fornecidos pelo estudo se refere à falta de correspondência temporal de coleta de dados por meio de sensores. Os autores explicam que a medição do GPS pode ocorrer com a periodicidade de um segundo, enquanto o sensor de temperatura pode realizar a medição a cada uma hora. A incompatibilidade do tempo de medição deve ser levada em consideração, uma vez que informações importantes podem ser perdidas se houver um procedimento para o ajuste das variáveis envolvidas. No projeto de manutenção preditiva, nos deparamos com um problema semelhante: sensores que coletavam os dados em diferentes intervalos de milissegundos. Prezando pela qualidade da informação, optou-se pela utilização de cálculos estatísticos que possibilitassem o melhor aproveitamento dos dados obtidos.

No que se refere à construção de modelos de machine learning, assim como em cidades inteligentes, foi possível desenvolver para o projeto um algoritmo de classificação com base na aprendizagem supervisionada — isto é, aprender a predizer de forma apropriada para um determinado input com base em dados existentes. Além disso, ocorreu também o processo de Feature Engineering, em que os atributos existentes foram analisados a fim de selecionar as variáveis que apresentam maior correlação com o atributo-alvo do modelo.

Assim como no estudo em questão, diferentes algoritmos foram testados pelo grupo até que o melhor modelo fosse encontrado: K-Nearest Neighbors, Naive Bayes, Support Vector Machine, Classification Tree, Random Forest, entre outros.
