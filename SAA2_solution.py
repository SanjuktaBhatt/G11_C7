size = (600, 600)
screen = pygame.display.set_mode(size)
carryOn = True
while carryOn:
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                  carryOn = False # Flag that we are done so we exit this loop             
    screen.fill(DARKBLUE)
    font = pygame.font.Font(None, 34)
    text = font.render("First Name: John " , 1, WHITE)
    screen.blit(text, (20,10))
    text = font.render("Country: India " , 1, WHITE)
    screen.blit(text, (20,40))
    text = font.render("State: Bengal" , 1, WHITE)
    screen.blit(text, (20,60))
pygame.quit()
    
