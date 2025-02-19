# Aula 01

Altere o timbre da voz de uma pessoa.

## Introdução: 

Vimos que as deepfakes podem aparecer em diversos contextos e mídias, sejam elas com apenas sons ou imagens e também com ambos. Será que podemos desenvolver um APP capaz de realizar algum tipo de alteração na voz das pessoas? 

## Tarefa: 

Criar um aplicativo, utilizando a plataforma [MIT APP Inventor](https://appinventor.mit.edu/), capaz de captar a voz de uma pessoa, convertê-la em texto e depois reproduzir com frequência e velocidade diferentes do som original.

## Primeiros passos: 

  * Acesse a plataforma [MIT APP Inventor](https://appinventor.mit.edu/) e faça o login na sua conta.
    
  * Crie um novo projeto clicando em *"New Project"*
![New Project](https://github.com/user-attachments/assets/326c30a8-f749-4c0b-8a28-688214f140ab)

  * Você deve adicionar as ferramentas listadas abaixo, elas podem ser encontradas na *"Interface do Usuário"*:
    1. 2 botões;
    2. 1 caixa de texto;
    3. 2 legendas;
    4. 2 deslizadores;
       
  * Adicione as ferramentas listadas abaixo que você encontrará no menu lateral *"Mídia"*:
    1. Reconhecedor de Voz;
    2. Texto para falar;

  * Agora seu projeto está pronto para começar a ser customizado e receber os comandos em blocos.

## Organização:

  Você deve organizar seu aplicativo de uma maneira funcional pensando nas funções de cada elemento do aplicativo:
  
  * Um dos botões será utilizado para gravar o som, formate seu visual para representar essa função.
  * A caixa de texto irá apresentar a transcrição da fala que será capturada quando o botão de gravar for acionado.
  * O outro botão deve reproduzir o som que foi gravado quando for acionado. Formate o seu visual também.
  * Um dos deslizadores será utilizado para alterar a velocidade da reprodução e o outro para deixar o som mais grave ou agudo. Eles devem ser configurados para *valor mínimo igual a zero* e *valor máximo igual a dois*.
  * Organize os botões utilizando os *Organizadores*.
  * Adicione um ícone para seu APP acessando as *Propriedades do seu projeto*.
    ![Propriedades](https://github.com/user-attachments/assets/9f2ce0b6-de80-46c8-9a56-f4685c850d33)


## Comandos em Blocos:

  Você deve organizar os blocos de comando para realizar as seguintes operações:

  * Quando o botão para *gravação* for acionado *("quando botão .Clique fazer")* ele deve chamar o *Reconhecedor De Voz* para *obter o texto* daquilo que for falado.
  * O *Reconhecedor de voz*, após obter o texto, deve *ajustar a caixa de texto* para *obter o resultado da gravação*. Essa função poderá ser encontrada nos blocos *"Internos->Variáveis"*.
  * Quando o botão de *reprodução* for acionado ele deve *ajustar a altura do Texto Para Falar* para a *posição do indicador do deslizador* responsável por alterar a frequência da voz. Também deve *ajustar a velocidade do Texto Para Falar* para a *posição do indicador* do outro deslizador que será responsável por *alterar a velocidade* de reprodução da voz.
  * Por fim você deve *chamar* a função *Texto Para Falar* a mensagem *obtida* na *caixa de texto*.

  Se tudo estiver correto, seu aplicativo deve estar funcionando perfeitamente. Compile e teste seu APP.

## :pushpin:Entregas :eyes::

  * *Publicar* seu aplicativo em sua galeria.
    ![Galeria](https://github.com/user-attachments/assets/ac20a4ec-5ec8-42f7-ac19-dfddfc729ac7)

  * Registrar a atividade no seu portfólio fazendo um breve resumo a respeito da atividade e disponibilizando o link da sua galeria para acessar o aplicativo desenvolvido.
  * Postar o link da galeria no **Google Sala de Aula** na turma de [GAMES e APPs](https://classroom.google.com/c/Njg0OTk5NTIxMzA5?cjc=vktf4pd).

## Exemplo:

[Aplicativo de Exemplo](https://gallery.appinventor.mit.edu/?galleryid=2fe90414-f4c1-4f6e-852c-6802a0c18a02)
