import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()

        #60fps Frame Limiter
        dt = gameClock.tick(60)/1000

if __name__=="__main__":
    main()