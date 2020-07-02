import pygame
#from player import player

class projectile(pygame.sprite.Sprite):#add sprite

    def __init__(self,player):
        super().__init__()
        self.velocity = 10
        self.image = pygame.transform.scale(pygame.image.load('assets/projectile.png'),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.angle = 0
        self.rotation_speed = 8
        self.rotated_image = self.image


    def move(self):
        self.rect.x += self.velocity
        self.angle += self.rotation_speed
        self.image = pygame.transform.rotozoom(self.rotated_image,self.angle,1)
