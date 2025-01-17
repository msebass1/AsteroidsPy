import sys
import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    time = pygame.time.Clock()
    delta_time = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shoots, updatable, drawable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        for update in updatable:
            update.update(delta_time)

        for asteroid in asteroids:
            if asteroid.colision(player):
                sys.exit()
            for shoot in shoots:
                if shoot.colision(asteroid):
                    shoot.kill()
                    asteroid.split()

        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        delta_time = time.tick(60)/1000

if __name__ == '__main__':
    main()
