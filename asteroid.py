import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        split_as1v = self.velocity.rotate(split_angle)
        split_as2v = self.velocity.rotate(-split_angle)
        split_asR = self.radius - ASTEROID_MIN_RADIUS

        split_as1 = Asteroid(self.position.x, self.position.y, split_asR)
        split_as1.velocity = split_as1v * 1.2
        split_as2 = Asteroid(self.position.x, self.position.y, split_asR)
        split_as2.velocity = split_as2v * 1.2
        