import pygame
import sys
from constants import *
from player import Player
from player import Shot
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_speed = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)) 

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #limit framerate to 60fps
        dt = game_speed.tick(60) / 1000


if __name__ == "__main__":
    main()