'''
Created on Jul 20, 2017

@author: Ranaar Araajakata
'''

import pygame, sys, random, time, math

check_errors = pygame.init()  # @UndefinedVariable

if check_errors[1] > 0:
    print("(!) {0} init error(s), exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("PyGame successfully initialized!")

dispSize = (720, 460)
playSurface = pygame.display.set_mode(dispSize)
pygame.display.set_caption('Snakes!')

red = pygame.Color(255, 0, 0, 255)  # gameover
green = pygame.Color(0, 255, 0, 255)  # snake
black = pygame.Color(0, 0, 0, 255)  # score
white = pygame.Color(255, 255, 255, 255)  # bkgd
yellow = pygame.Color(255, 255, 0, 255)  # food

fpsController = pygame.time.Clock()

snakeBody = [(100, 50), (90, 50), (80, 50), (70, 50)]
direction = 'R'

food = (random.randrange(0, math.floor(dispSize[0] / 10)) * 10,
        random.randrange(0, math.floor(dispSize[1] / 10)) * 10)
foodSpawn = False

def gameOver(dispWidth):
    myFont = pygame.font.SysFont(name="Comic Sans", size=70, bold=True)
    GOsurf = myFont.render("Game Over" , True , red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (math.floor(dispWidth / 2), 15)
    playSurface.blit(GOsurf , GOrect)
    pygame.display.update()
    time.sleep(10)
    
    pygame.quit()
    sys.exit()

while True:
    changeTo = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == ord('w'):
                direction = 'U'
            elif event.key == pygame.K_LEFT or event.key == ord('a'):
                direction = 'L'
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                direction = 'D'
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                direction = 'R'
            elif event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        else:
            pass



    if 






