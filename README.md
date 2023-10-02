# ProjetoIPequipe5
**Projeto de Introdução à Programação para criar um jogo em Python utilizando o Pygames.**

**Membros da equipe:** *Gabriel Stamford (gsa3), Igor Fragoso (ifplm), Pedro Dantas (phds3), Pedro Elias (pega) e Samuell Costa (shcpc).*


**INTRODUÇÃO**

	Este relatório busca explicar o processo de criação do projeto Frog Adventures e analisar o trabalho da equipe durante o processo, observando o desenvolvimento da estrutura do projeto, as dificuldades enfrentadas pela equipe e todo o processo de idealização decorrido.
	O projeto é feito na linguagem de Python e sob o domínio de Programação Orientada a Objetos, sendo resultado do desempenho dos integrantes no que foi aprendido a respeito dos exercícios da linguagem Python.

<img src="/sprites/foto_jogo.png">

<img src="/sprites/foto_jogo2.png">

<img src="/sprites/foto_game_over.png">

**Como Funciona o Jogo:**



	A princípio, o jogo possui uma tela de menu no qual ele poderá apertar o botão “Jogar” e “Créditos”, nos quais o primeiro ele iniciará o jogo e no segundo ele visualiza os criadores do jogo.
	Quando iniciado o jogo, o jogador estará controlando um personagem sapo o qual deve coletar três livros que representam algumas cadeiras componentes do primeiro período de Ciência da Computação: Álgebra Vetorial e Linear, Matemática Discreta e Cálculo.
	Para atrapalhar a coleta do jogador, são gerados de forma aleatória até dois inimigos: o esqueleto, sendo ele mais rápido, e o fantasma, sendo este capaz de atravessar paredes.
	O jogo termina apenas quando o jogador morre ou quando ele decide sair do jogo pelo Mouse.


**Descrição da Arquitetura:**

    A estrutura do projeto é constituída por um conjunto de pastas e códigos que são integrados para a funcionalidade do jogo Frog Adventures. De início, ela é baseada no arquivo “Main.py”, na qual ocorre as principais funcionalidades do jogo com respeito à interação dos coletáveis, saída e entrada da janela, menu, surgimento de monstros, ações e demais funcionalidades padrões. Integrada com a “Main.py”, temos o arquivo “UI.py”, que tem o papel de ligar o funcionamento do código com a interface do usuário - seria a própria tela do jogo.

	A estrutura do projeto é constituída por um conjunto de pastas e códigos que são integrados para a funcionalidade do jogo Frog Adventures. De início, ela é baseada no arquivo “Main.py”, na qual ocorre as principais funcionalidades do jogo com respeito à interação dos coletáveis, saída e entrada da janela, menu, surgimento de monstros, ações e demais funcionalidades padrões. Integrada com a “Main.py”, temos o arquivo “UI.py”, que tem o papel de ligar o funcionamento do código com a interface do usuário - seria a própria tela do jogo.

	Uma das principais estruturas criadas foi o arquivo de constantes. Nele, são guardados todos os coletáveis, variáveis fundamentais e tudo relacionado a mapa, itens e inimigos. A pasta de “Entities” estava totalmente relacionada ao arquivo de constantes por conter guardada todos os códigos com respeito à movimentação de inimigos, movimentação e controle do player e todos os objetos envolvidos. Dentro desta pasta, contamos com três arquivos essenciais: o código da elaboração do mapa e seus itens, o código para a elaboração dos inimigos e seu movimento - junto de todas as suas variáveis e o código que determina os status do jogador, o sapo.
	As imagens dos objetos foram guardadas dentro da pasta “sprites”, ela serviu como base para as ideias que foram ou não colocadas no jogo. Uma vez que foram escolhidos mais de 2 monstros e salvos dentro do arquivo durante o processo de criação do jogo.

**Ferramentas utilizadas:**

    Foi utilizada a biblioteca Pygame para desenvolver o projeto. A biblioteca gerencia e abstrai grande parte do trabalho com os elementos gráficos, sonoros e de entrada e saída. Logo, o Pygame foi a base para o projeto, permitindo que a equipe pudesse focar muito mais nas estruturas lógicas referentes ao próprio jogo e tivesse maior liberdade criativa para testar novas ideias e implementar novas funcionalidades.
    Foram utilizadas ainda outras bibliotecas mais conhecidas do Python, como o Math e o Random, além do OS e do SYS, que foram utilizados para trabalhar com o gerenciamento de pastas do projeto.


**Divisão do trabalho:**

    De início, a idealização do projeto quanto ao estilo de jogo, personagens, coletáveis e design foi determinada pela equipe como um todo. No decorrer da criação do projeto, os códigos principais como movimentação, imagens e ambiente foram criados por Samuell, dando um grande passo logo no início do projeto. Igor teve a ideia do jogo, fez a maioria dos mapas do jogo e supervisionou o GitHub.
    Com o decorrer do tempo de entrega, Pedro Dantas seguiu com o desenvolvimento do código. A criação de diversos mapas foi feita com auxílio de todos do grupo e a instalação de música foi colocada para as diversas situações do jogo por Gabriel. Além disso, o sistema de combate e a última alteração dos mapas foram fixados por Pedro Elias.

**Conceitos utilizados para a criação do projeto:**

    Estruturas Condicionais: foram utilizadas por todo o projeto para tomar decisões com base nas informações do game e alternar entre comportamentos dadas as interações do jogador.

    Estruturas de Repetição: foram de grande importância para o laço de repetição principal do jogo, onde são realizadas todas as ações durante a execução da aplicação.

    Tuplas: são utilizadas para guardar informações como taxas de cores RGB, coordenadas e tamanhos de objetos no mapa e para recorte de sprites das imagens.

    Dicionários: Utilizamos para manter salvos os modelos de cada “chunk”  no mapa, que por ser infinito e ter geração pseudo-aleatória não poderia ser armazenado em uma lista.

    Listas: os modelos de cada “chunk” do mapa, ou seja, de cada parte do mapa, para serem interpretados pelo gerador, foram feitos utilizando-se listas e strings.

    Funções: foram utilizadas para separar funcionalidades de forma a deixar o código mais legível e organizado, separando blocos de código com mesma finalidade em funções definidas.

    Programação Orientada a Objetos (POO): de grande importância no projeto, classes e objetos foram utilizados tanto de forma integrada ao Pygame, estendendo classes dessa biblioteca, como de forma autônoma criando classes próprias para gerenciamento, unificação e centralização de tarefas. Vale mencionar a grande importância da orientação a objetos para o controle in game do player, dos inimigos e do gerenciamento do mapa, junto com os blocos, itens e background.


**Qual foi o maior erro cometido durante o projeto e como foi resolvido?**

    O maior erro cometido foi o fato de que alguns membros começaram a criar o projeto de maneira mais tardia que os demais, pois não possuíam o conhecimento técnico necessário. Assim, tais membros tiveram que se adaptar ao código já criado e esse processo não foi realizado da forma mais eficiente. A resolução se baseou na busca por esse conhecimento técnico, por meio de processos autodidatas, além de recorrer aos membros mais experientes.


**Qual foi o maior desafio enfrentado durante o projeto e como vocês lidaram com ele?**

    O maior desafio foi a implementação de POO no projeto, uma vez que demanda tempo o estudo do conteúdo e isso se tornou um desafio, pois o assunto demandava certo comprometimento para a criação organizada do projeto e o tempo ficou sendo competido pelas demais disciplinas.
    Com o tempo livre de cada membro, cada parte do projeto foi sendo desenvolvida e integrada. Apesar de não ter sido de forma simultânea, o projeto acabou sendo finalizado de maneira satisfatória para a equipe.


**O que foi aprendido durante o processo de criação do projeto?**

    Durante nosso período de aprendizado em Python, adquirimos habilidades práticas, incluindo uma compreensão da Programação Orientada a Objetos e o uso eficaz do GitHub para gerenciar nossos projetos. Além disso, exploramos a biblioteca Pygame, permitindo-nos criar jogos interativos e aprimorar nossa capacidade de aplicar a programação de forma criativa. A colaboração em equipe foi algo essencial para esse projeto, aprimorando nossa comunicação e resolução de problemas conjuntos.
    Em resumo, nossa jornada em Python nos equipou com habilidades essenciais de programação, domínio de ferramentas-chave e experiência em trabalhar colaborativamente em projetos, preparando-nos para futuros desafios no campo da tecnologia e do desenvolvimento de software.
    
**Como executar o sistema interativo:**

    1. Instalar o Python
    2. Instalar a biblioteca do pygame através do comando "pip install pygame" dentro do prompt de comando do computador 
    3. Realizar o Download do arquivo ZIP associado ao main.py 
    4. Realizar o processo de clonagem dos arquivos a partir do comando "git clone" 
    5. Executar no prompt de comando através do python main.py

	






