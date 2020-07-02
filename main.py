import pygame
from game import game

pygame.init()

# caption
pygame.display.set_caption("My game")
# fenetre size
screen = pygame.display.set_mode((1080 , 720))
backgroud = pygame.image.load('assets/bg.jpg')
my_game = game()
running = True
while running:
    # setting background :
    screen.blit(backgroud,(0,-200))
    # setting player
    screen.blit(my_game.primary_player.image,my_game.primary_player.rect)
    #setting projectiles
    my_game.primary_player.list_projectile.draw(screen)
    # mettre a jour l image
    pygame.display.flip()
    #move player
    if 0 <= my_game.primary_player.rect.x <= screen.get_width() - my_game.primary_player.rect.width :
        my_game.move_player()
    elif my_game.primary_player.rect.x > screen.get_width() - my_game.primary_player.rect.width :
        my_game.primary_player.rect.x = screen.get_width() - my_game.primary_player.rect.width
    elif  my_game.primary_player.rect.x <= 0:
        my_game.primary_player.rect.x = 0
    #move projectiles
    for projectile in my_game.primary_player.list_projectile:
        projectile.move()
        if projectile.rect.x > screen.get_width() :
            my_game.primary_player.list_projectile.remove(projectile)
            print("Projectile Removed !")

    for event in pygame.event.get():
        # fermeture" de fenetre
        if event.type == pygame.QUIT :
            running = False
            print("Fermeture de la fenetre")

        #detecter les touches de clavier
        elif event.type == pygame.KEYDOWN:
            my_game.pressed[event.key] = True
            # launch projectile
            if event.key == pygame.K_SPACE:
                my_game.primary_player.launch_projectile()
        elif event.type == pygame.KEYUP:
            my_game.pressed[event.key] = False
