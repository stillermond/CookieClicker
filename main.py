#gopher mash
#written by Dr. Mo, 11/10/2020
import pygame
import math #needed for square root function



pygame.init()#initializes Pygame
print(pygame.font.get_fonts())
pygame.display.set_caption("Cookie Clicker")#sets the window title
screen = pygame.display.set_mode((400,400))#creates game screen

print(pygame.font.get_fonts())
#player variables
isBig = False
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
numClicks = 0

#circle variables: circX and circY are the coordinates of the center (where it's drawn), and the radius is how big it is
circX = 200
circY = 200
radius = 100
CookiePic = pygame.image.load("cookie.png")
CookieRect = CookiePic.get_rect(topleft=(100,100))

CookiePic2 = pygame.image.load("cookie2.png")
CookieRect2 = CookiePic2.get_rect(topleft=(90,90))

font = pygame.font.Font('freesansbold.ttf',32)
text1 = font.render('score:',False,(0,200,200))
text2 = font.render(str(int(numClicks)),1,(0,200,200))
#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()

    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN: #check if clicked
      if math.sqrt((mousePos[0]-circX)**2+(mousePos[1]-circY)**2) <radius:
            numClicks+=1
      print("CLICK")

    if event.type == pygame.MOUSEMOTION: #check if mouse moved
        mousePos = event.pos #refreshes mouse position
        print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")
        if math.sqrt((mousePos[0]-circX)**2+(mousePos[1]-circY)**2) <radius:
            isBig = True
        else:
            isBig = False
 
#render section---------------------------------------------
    screen.fill((255, 255, 255)) #wipe screen (without this, things smear)
    text2 = font.render(str(int(numClicks)),1,(0,200,200))
    screen.blit(text1, (10,10))
    screen.blit(text2, (110,10))
    pygame.draw.circle(screen, (200, 0, 200), (circX,circY), radius)
    print("clicks:", numClicks) #uncomment this once collision is set up
    if math.sqrt((mousePos[0]-circX)**2+(mousePos[1]-circY)**2) <radius:
        isBig = False
        screen.blit(CookiePic, CookieRect)
    else:
        isBig = True
        screen.blit(CookiePic2, CookieRect2)
    
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()


