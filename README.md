# Aula 05

Construindo um jogo de tiro FPS

## Introdução: 

O objetivo desta aula é desenvolver um layout para um jogo de tiro (que também é conhecido como FPS - First-Person Shooters, não confundir com FPS de um jogo que é Frames Per Second) onde o objetivo é acertar vinte vezes o cogumelo (alvo) que se move aleatoriamente na tela.

## Primeiros passos: 

  * Analise a parte inicial do código na qual são inicializadas as bibliotecas, definição de cores e carregamento das imagens que serão utilizadas;
  * Logo depois são definidas algumas funções para configurar o texto que aparecerá na tela, as dimensões e posicionamento do cogumelo e do alvo na tela;
  * Em seguida temos as configurações da tela e variáveis de controle para movimentação do cogumelo;
  * Verifique a dinâmica do jogo na função "while True" e entenda como são realizadas as atualizações da posição do cogumelo e as condições para que o alvo seja atingido;
  * Por fim definimos que o ponteiro do mouse ficará invisível para que a imagem da mira apareça. Criamos a animação para que a vida do cogumelo diminua a cada acerto do atirador e criamos a condição de reiniciar o jogo quando a vida do cogumelo zerar.

## Tarefa:

  * Clicar com o botão direito na imagem “cenario-mario.jpg”, ir em propriedades, depois na aba detalhes. Procure as dimensões da imagem;
  * Altere a resolução da tela para que apareça o cenário completo, mas não aparece a tela preta ao redor do cenário;
  * Altere o código para que o cogumelo se mova até o fim da tela na horizontal, perceba que ele está desaparecendo próximo ao meio da tela.
  * Altere a velocidade de movimentação do cogumelo deixando-o mais rápido, porém ainda deve ser possível vê-lo se movendo na tela;
  * Aumente o número de vezes que deve-se acertar o cogumelo para vencer o jogo de 10 para 20;
      * Note que a barra de vida ficará desconfigurada, ajuste a configuração da barra de vida para que ela permaneça do mesmo tamanho do código original.
  * Adicione um botão para sair do jogo a qualquer momento;

## Desafio:

Nesta etapa você deve criar uma continuação para a história.

* Adicione um som de tiro a cada clique do mouse;
* Implemente o código para que a velocidade do cogumelo mude de maneira aleatória;
* Adicione um som ambiente para o jogo.


Veja o resultado em https://trinket.io/pygame/959a71b171f6
