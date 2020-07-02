from player import player
import pygame

class game:
    def __init__(self):
        self.primary_player = player()
        self.pressed = {}

    def move_player(self):
        for key in self.pressed:
            if self.pressed[key] :
                if key == pygame.K_LEFT:
                    self.primary_player.move_left()
                elif key == pygame.K_RIGHT:
                    self.primary_player.move_right()