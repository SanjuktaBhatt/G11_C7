import pygame
import random
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (400, 400)

player=pygame.Rect(50,200,20,20)
playerx=random.randint(1,2)
playery=random.randint(1,2)
wall=[pygame.Rect(350,i*50+5,20,40) for i in range(8)]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C6")
carryOn = True
while carryOn:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(YELLOW)
  player.x+=playerx
  player.y+=playery
  if player.x<=0 or player.x>=380:
    playerx=-playerx
  if player.y<=0 or player.y>=380:
    playery=-playery
  
  for i in wall:
   pygame.draw.rect(screen,RED,i)
  #Begin a for loop to iterate through the wall
  for i in wall:
    #Check if "i" and "player" collided
    if i.collidepoint(player.x,player.y):
      #Remove "i"
      wall.remove(i)
      #Change player direction
      playerx=-playerx
      playery=-playery
      
  pygame.draw.rect(screen,DARKBLUE,player)
  pygame.display.flip()
pygame.quit()
