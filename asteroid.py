import pygame
from constants import *
from circleshape import CircleShape
import random


class Asteroid(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.velocity = pygame.Vector2(0, 0)

    def set_velocity(self, speed, direction):
        self.velocity = pygame.Vector2(direction) * speed

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle) 
            velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.set_velocity(1.2, velocity1)

            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.set_velocity(1.2, velocity2)