import pygame

# def isNearObstacle(point,clearance= 0):
    # circle = (point[0] - 225)**2 + (point[1]-150)**2
    # print(circle)
    # ellipse = (point[0] - 225)**2/40**2 + (point[1]-150)**2/25**2
    # if(circle <= 25**2 or ellipse<= 1):
        # return True
    # return False



pygame.init()

white = (255,255,255)
black = (0,0,0)


red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((300,200))
gameDisplay.fill(white)

pygame.draw.rect(gameDisplay, red, (400,400,50,25))
pygame.draw.circle(gameDisplay, red, (225,50), 5)
pygame.draw.polygon(gameDisplay, green, ((25,185),(75,185),(100,150),(50,150),(20,120),(75,120)))
pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)

# pixAr = pygame.PixelArray(gameDisplay)
# pixAr[10][:] = green
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
