import pygame
from projectile import projectile

#classe joueur
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lives = 100
        self.max_lives = 100
        self.attack = 5
        self.velocity = 10
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.list_projectile = pygame.sprite.Group()

    def launch_projectile(self):
        self.list_projectile.add(projectile(self))

    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity