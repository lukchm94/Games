from pygame.locals import *
import pygame
import time
from random import randint

class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))

class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 10

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # initial positions, no collision.
        self.x[1] = 1 * 44
        self.x[2] = 2 * 44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:

                return True
        return False

    def isWall(self, x1,y1,x2,y2,bsize, width, height):
        if x1 < 0:
            return True
        if x1 > (width - 1):
            return True
        if y1 < 0:
            return True
        if y1 > height:
            return True

        return False
class App:
    player = 0
    apple = 0
    count = 0
    w = 0
    h = 0
    width = 0
    height = 0
    times_played = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._background_image = None
        self._apple_surf = None
        self._text = None
        self.game = Game()
        self.player = Player(5)
        self.apple = Apple(5,5)
        self.count = 0
        self.width = 0
        self.height = 0
        self._game_over = False
        self.w = None
        self.h = None
        self._pause = False
        self._quit = False
        self._times_played = 2

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.w, self.h = pygame.display.get_surface().get_size()
        self.width = (self.w/44) - 1
        self.height = (self.h/44) - 1
        pygame.display.set_caption('Snake Game')
        self._running = True
        self._image_surf = pygame.image.load("logo.png").convert()
        self._apple_surf = pygame.image.load("apple.png").convert()
        if self.times_played % 2 == 0:
            self._background_image = pygame.image.load("back_ground.jpeg").convert()
        else:
            self._background_image = pygame.image.load("dude.jpg").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        if self._pause == False:
            self.player.update()
            # does snake eat apple?
            for i in range(0, self.player.length):
                if self.game.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 40):
                    self.apple.x = randint(2, 30) * 44
                    self.apple.y = randint(2, 16) * 44
                    self.player.length = self.player.length + 1
                    self.count = (self.player.length) - 5

            # does snake collide with itself?
            for i in range(2, self.player.length):
                if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                    print("You lose! Collision: ")
                    print("x[0] (" + str(self.player.x[0]) + "," + str(self.player.y[0]) + ")")
                    print("x[" + str(i) + "] (" + str(self.player.x[i]) + "," + str(self.player.y[i]) + ")")
                    self._game_over = True
                    self._pause = True

            # does snake hit the wall?
            for i in range(2, self.player.length):
                if self.game.isWall(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40, self.w, self.h):
                    if int(self.player.x[0]) < 0:
                        self.player.x[0] = int(self.width) * 44

                    if int(self.player.x[0]) > (int(self.w) - 1):
                        self.player.x[0] = 0

                    if int(self.player.y[0]) < 0:
                        self.player.y[0] = int(self.height) * 44

                    if int(self.player.y[0]) > (int(self.h) - 1):
                        self.player.y[0] = 0

            pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._background_image, [0, 0])
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Your score: " + str(self.count), True, (0,0,0))
        self._display_surf.blit(text, [0, 0])

        if self._game_over:
            score_font = pygame.font.SysFont('freesansbold.ttf', 125, True, False)
            score_text = score_font.render("Your Snake score is " + str(self.count) + "!", True, (255, 255, 255))
            textRectScore = score_text.get_rect()
            textRectScore.center = (self.w // 2, self.h // 5)
            self._display_surf.blit(score_text, textRectScore)
            large_font = pygame.font.SysFont('freesansbold.ttf', 115, True, False)
            large_text = large_font.render('Game Over', True, (255, 0, 0))
            textRect = large_text.get_rect()
            textRect.center = (self.w // 2, self.h // 2.25)
            self._display_surf.blit(large_text, textRect)
            l_font = pygame.font.SysFont('freesansbold.ttf', 100, True, False)
            l_text = l_font.render('Play Again? Y/N', True, (0, 0, 0))
            textRectL = l_text.get_rect()
            textRectL.center = (self.w // 2, self.h // 1.75)
            self._display_surf.blit(l_text, textRectL)
            keys = pygame.key.get_pressed()
            if (keys[K_n]):
                self._running = False
            if (keys[K_y]):
                self.times_played = self.times_played + 1
                self.count = 0
                self.player.length = 5
                self.player.x[0] = 1 * 44
                self.player.y[0] = randint(1, 16) * 44
                print(self.player.x[0])
                print(self.player.y[0])
                print(self.player.direction)
                if self.player.direction == 0:
                    self.player.direction = 2
                else:
                    self.player.direction = 0

                self.__init__()
                self.on_init()
                self._game_over = False
                self._pause = False


        if self._quit and self._game_over == False:
            large_font = pygame.font.SysFont('freesansbold.ttf', 115, True, False)
            large_text = large_font.render('Do you want to exit? Y/N', True, (255, 0, 0))
            textRect = large_text.get_rect()
            textRect.center = (self.w // 2, self.h // 2)
            self._display_surf.blit(large_text, textRect)
            keys = pygame.key.get_pressed()

            if (keys[K_y]):
                self._running = False
            if (keys[K_n]):
                self._quit = False
                self._pause = False
                self.player.moveRight()

        if self._pause and self._quit == False and self._game_over == False:
            large_font = pygame.font.SysFont('freesansbold.ttf', 115, True, False)
            large_text = large_font.render('Paused', True, (255, 255, 255))
            textRect = large_text.get_rect()
            textRect.center = (self.w // 2, self.h // 4)
            self._display_surf.blit(large_text, textRect)
            l_font = pygame.font.SysFont('freesansbold.ttf', 100, True, False)
            l_text = l_font.render('Press C to continue ot Q to exit', True, (0, 0, 0))
            textRectL = l_text.get_rect()
            textRectL.center = (self.w // 2, self.h // 2)
            self._display_surf.blit(l_text, textRectL)
            keys = pygame.key.get_pressed()

            if (keys[K_c]):
                self._pause = False
            if (keys[K_q]):
                self._running = False

        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()
            if (keys[K_LEFT]):
                self.player.moveLeft()
            if (keys[K_UP]):
                self.player.moveUp()
            if (keys[K_DOWN]):
                self.player.moveDown()
            if (keys[K_ESCAPE]):
                self._quit = True
                self._pause = True
            if (keys[K_SPACE]):
                self._pause = True

            self.on_loop()
            self.on_render()

            if int(self.count) < 5:
                time.sleep(500.0 / 10000.0);
            elif int(self.count) >= 5 and int(self.count) < 10:
                time.sleep(400.0 / 10000.0);
            elif int(self.count) >= 10 and int(self.count) < 20:
                time.sleep(300.0 / 10000.0);
            elif int(self.count) >= 20 and int(self.count) < 50:
                time.sleep(250.0 / 10000.0);
            elif int(self.count) >= 50:
                time.sleep(125.0 / 10000.0);
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()