# Aula 02

Construindo um Storyboard 

## Introdução: 

O objetivo desta aula é criar uma narrativa baseada em 10 telas com a programação Python(com o uso da biblioteca Pygame). Como seria a sequência de telas para dar início, meio e fim a uma história contada? Construa essa narrativa. 

## Tarefa: 

Desenvolver um Storyboard e nele precisam estar presentes alguns elementos como: tamanho da tela e legenda. Siga os passos do Processo abaixo e você terá como resultado o desenvolvimento do Storyboard do seu game.

## Primeiros passos: 

  * Salve as imagens e o arquivo Story.py em uma mesma pasta;
  * Abra o arquivo Story.py com a IDLE;
  * Pressione F5 para testar o código.

Teste alguns comandos para entender seu funcionamento:

* Altere os valores (250,185) da linha de comando *screen=pygame.display.set_mode((250,185),0,0)* para (500,370) e veja o que acontece com o jogo;
* Altere os valores (0,0) no último  *elif* no comando *screen.blit* para (30,30) e veja o que acontece.
* Veja o que acontece se você adicionar o código abaixo após a última linha com a função **elif**
  
        elif (event.type == MOUSEBUTTONUP) and (estado == 6):
            pygame.display.quit ()

## Desafio:

Nesta etapa você deve criar uma continuação para a história.

* Primeiro entenda qual é o contexto da problematização apresentada no game e faça uma pesquisa da possibilidade ou impossibilidade dessa situação acontecer.
* Na última tela a trollface pergunta se há algum problema, a partir dessa tela crie:
* No mínimo mais 4 telas, ou seja, o jogo completo deve ter no mínimo 10 telas:
* Nessas telas você deve continuar a problematização respondendo qual ou quais são os problemas da lógica apresentada pelas telas anteriores, com base na sua pesquisa;
* Desenvolva as imagens com legendas;
* Configure o tamanho da tela de acordo com suas imagens.
* O Storyboard deve ser acionado pelo botão do mouse, ou seja, a cada clique a tela deve ser atualizada para a próxima imagem da história.
* Após a útlima tela da história, ao clicar com o mouse, a tela do jogo deve ser fechada.

## Critérios de avaliação

Sua produção final será avaliada pelos seguintes critérios:

| Critério | Conceito A | Conceito B | Conceito C |
| -------- | -------- | -------- | -------- | 
| Código e Interatividade | 10 telas integradas, com clique do mouse funcionando perfeitamente e sem erros de execução. | Transição de telas funciona, mas apresenta pequenos erros ou menos de 10 telas. | Transição não funciona via clique ou código incompleto. |
| Estética e Mídia | Imagens ajustadas ao tamanho da tela, legendas claras e som de fundo adequado. | Imagens sem dimensionamento adequado ou falta de som/legendas. | Sem adaptação de mídia ou legendas ausentes. |
| Comentários e Matemática | Código totalmente comentado explicando a lógica e a matemática utilizada. | Presença de poucos comentários ou explicação matemática superficial. | Ausência de comentários explicativos no código. |

## Orientação para Entrega no Google Classroom

* Salve o arquivo final do seu código com o nome Storyboard_Nome_Sobrenome.py.
* Adicione em uma pasta do seu Drive o código juntamente com a pasta de mídias (imagens e sons utilizadas).
* Compartilhe o link dessa pasta na atividade no Google Classroom até o horário indicado pelo professor.

## Atualização do Portfólio Digital

Responda as perguntas abaixo ao registrar a atividade:

* Qual foi o maior desafio técnico encontrado na programação do Pygame hoje?
* Como os conceitos de medida e proporção ajudaram a organizar o layout visual do game?

Por fim, capture 2 a 3 telas da sua narrativa, grave um pequeno trecho ou gif do storyboard em funcionamento e publique no seu Portfólio Digital com uma breve descrição explicativa da atividade.
