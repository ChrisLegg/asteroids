import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return
        for item in updateable:
            item.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(ship):
                print("Game over!")
                sys.exit()
        screen.fill("black")

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()


        #60fps Frame Limiter
        dt = gameClock.tick(60)/1000

if __name__=="__main__":
    main()