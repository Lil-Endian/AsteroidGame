import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("asteroid eliminated!")
        else:
            random_angle = random.uniform(20,50)
            new_vector_1 = pygame.Vector2(self.velocity).rotate(random_angle)
            new_vector_2 = pygame.Vector2(self.velocity).rotate(-random_angle)
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_1.velocity = new_vector_1 * 1.2
            new_asteroid_2.velocity = new_vector_2 * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white",  self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt