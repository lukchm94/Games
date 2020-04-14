import pygame

w = 800
h = 400

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

pygame.init()
screen = pygame.display.set_mode((w,h), pygame.HWSURFACE)

pygame.draw.lines(screen, black, False, [(100,100), (150,200), (200,100)], 1)
#pygame.display.fill(pink)
backImg = pygame.image.load('dude.jpg')
print(backImg)
#pygame.display.fill((255, 0, 0))


#screen.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False