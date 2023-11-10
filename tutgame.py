import pygame
x = pygame.init()

gameWindow = pygame.display.set_mode((1200, 500))  #used for display the window 
pygame.display.set_caption("My first game") #Title of the game 

#Game specific variables: 
exit_game = False
game_over = False

#Creating a game loop 
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True
            
#Creating a control pygame using keydown 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right arrow key")

pygame.quit()
quit()

