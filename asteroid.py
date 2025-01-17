import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return 
        rand_angle = random.uniform(20, 50)
        
        n_x,n_y = self.position.xy
        new_asteroid1 = Asteroid(n_x, n_y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2 = Asteroid(n_x, n_y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid1.velocity = self.velocity.rotate(rand_angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-rand_angle) * 1.2



