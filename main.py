import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        for item in updateable:
            item.update(dt)
        
        
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()


        #60fps Frame Limiter
        dt = gameClock.tick(60)/1000

if __name__=="__main__":
    main()