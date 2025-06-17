import pygame, random, sys
from pygame.locals import *

#definições de variáveis
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
BRANCO = 255,255,255
AMARELO = 255,255,0
PRETO = 0,0,0
VELOCIDADE = 10
ALTURA = 600
LARGURA = 600

#definição de gerador de número randômico inteiro
def posicao_aleatoria():
    x = random.randint(50,590)
    y = random.randint(50,590)
    return (x//10 * 10, y//10 * 10) #o símbolo // entrega um resultado inteiro da divisão

#definição de colisão entre a cobrinha e o pontinho vermelho
def colisão(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def reiniciar_jogo():
    global cobra, direcao, pontinho_pos, placar
    cobra = [(200, 200), (210, 200), (220, 200), (230, 200)]
    direcao = LEFT
    pontinho_pos = posicao_aleatoria()
    placar = 0

pygame.init()
screen = pygame.display.set_mode((LARGURA,ALTURA))
pygame.display.set_caption('Jogo da Cobrinha')

#desenho da cobrinha por meio dos pontos cartesianos (x,y) em formato matricial [a11,a12,a13,a14]
cobra = [(200, 200), (210, 200), (220,200), (230, 200)] 
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((200,160,40))

#gerador do pontinho
pontinho_pos = posicao_aleatoria()
pontinho = pygame.Surface((10,10))
pontinho.fill((244,0,161))

direcao = LEFT

clock = pygame.time.Clock()

font = pygame.font.Font('SNAP.TTF', 18)
placar = 0

while True:
    clock.tick(VELOCIDADE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

#controle da cobrinha com as teclas direcionais do teclado
        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            elif event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            elif event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT
            elif event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT
            elif event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == K_r:
                reiniciar_jogo()
                           
#loop de colisão com o pontinho
    if colisão(cobra[0], pontinho_pos):
        pontinho_pos = posicao_aleatoria()
        cobra.append((0,0)) #adiciona mais uma célula a cobrinha
        placar = placar + 1
        if VELOCIDADE >= 40:
            VELOCIDADE = 40
        else:
           VELOCIDADE = VELOCIDADE + 1
 

    if (cobra[0][0] <= 0 or cobra[0][0] >= 600 or
        cobra[0][1] <= 0 or cobra[0][1] >= 600 or
        cobra[0] in cobra[1:]):
        pygame.quit()
        sys.exit()

#movimentação da cobrinha 
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

#loop de movimentação da cobrinha de acordo com os eixos cartesianos
    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
        
#desenho na tela e placar
    screen.fill((75,36,35))
    screen.blit(pontinho, pontinho_pos)
    for pos in cobra:
        screen.blit(cobra_skin,pos)

    placar_font = font.render('Placar: %s' % (placar), True, (AMARELO))
    placar_rect = placar_font.get_rect()
    placar_rect.topleft = (LARGURA - 0.2*LARGURA, 10)
    VELOCIDADE_font = font.render('Velocidade: %s' % (VELOCIDADE), True, (AMARELO))
    VELOCIDADE_rect = VELOCIDADE_font.get_rect()
    VELOCIDADE_rect.topright = (LARGURA - 0.7*LARGURA, 10)
    
    screen.blit(placar_font, placar_rect)
    screen.blit(VELOCIDADE_font, VELOCIDADE_rect)
    
    pygame.display.update()
