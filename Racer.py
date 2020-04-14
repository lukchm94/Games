from pygame.locals import *
import pygame
import time
from random import randint

class Apple:
    x = [0]
    y = [0]
    step = 33
    direction = 3
    length = 10

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length):
        self.length = length
        for i in range(0, 2000):
            self.x.append(-100)
            self.y.append(-100)

        # initial positions, no collision.
        self.x[0] = randint(1,555)
        self.y[0] = 0



    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i - 1]
                self.y[i] = self.y[i - 1]

            # update position of head of snake
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))


class Player:
    x = [0]
    y = [0]
    step = 34
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
        self.x[0] = randint(1,540)
        self.y[0] = 625

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

            self.updateCount = 0

    def moveRight(self):
        self.x = self.x + (self.speed * 2)

    def moveLeft(self):
        self.x = self.x - (self.speed * 2)

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))

class Game:

    def isCollision(self,x1,y1,x2,y2,bsize):
        if (y1 > (630-75)):
            if x1 >= x2 and x1 <= x2 + bsize or x2 >= x1 and x2 <= x1 + bsize:
                return True
        return False

    def isMissed(self, y, h):
        if y > (h - 50):
            return True

        return False

    def isWall(self, x1,y1,width, height):
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
        self.player = Player(1)
        self.apple = Apple(1)
        self.count = 0
        self.width = 600
        self.height = 700
        self._game_over = False
        self.w = None
        self.h = None
        self._pause = False
        self._quit = False
        self._times_played = 2
        self.moved = False
        self.win = False
        self.win_image = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.width, self.height), pygame.HWSURFACE)
        self.w, self.h = pygame.display.get_surface().get_size()
        self.width = (self.w/44) - 1
        self.height = (self.h/44) - 1
        pygame.display.set_caption('Wookie Auditor Game')
        self._running = True
        self._image_surf = pygame.image.load("lego2.png").convert()
        self._apple_surf = pygame.image.load("a.png").convert()
        self.win_image = pygame.image.load("winner.png").convert()
        if self.times_played % 2 == 0:
            self._background_image = pygame.image.load("office.png").convert()
        else:
            self._background_image = pygame.image.load("office.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        if self._pause == False:

            if self.moved:
                self.player.update()

                # does auditor hit the wall?
                for i in range(0, self.player.length):
                    if self.game.isWall(self.player.x[0], self.player.y[0], self.w, self.h):
                        if int(self.player.x[0]) < 0:
                            self.player.x[0] = int(self.width) * 45

                        if int(self.player.x[0]) > (int(self.w) - 1):
                            self.player.x[0] = 0

                        if int(self.player.y[0]) < 0:
                            self.player.y[0] = int(self.height) * 45

                        if int(self.player.y[0]) > (int(self.h) - 1):
                            self.player.y[0] = 0
                self.moved = False

            self.apple.update()

            if self.game.isMissed(self.apple.y[0], self.h):
                if int(self.apple.y[0]) > int(self.h):
                    self.apple.y[0] = 0
                    self.apple.x[0] = randint(1,532)
                    self.count = self.count + 1
                    if self.count > 100:
                        self._pause = True
                        self.win = True
                    if int(self.count) % 5 == 0:
                        self.apple.length = self.apple.length + 1

            for i in range(0, self.apple.length):
                if self.game.isCollision(self.apple.x[i], self.apple.y[i], self.player.x[0], self.player.y[0], 62):
                    self._game_over = True
                    self._pause = True
            pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._background_image, [0, 0])
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Conrols Dodged: " + str(self.count), True, (34,139,34))
        self._display_surf.blit(text, [10, 15])

        if self._game_over:
            score_font = pygame.font.SysFont('freesansbold.ttf', 50, True, False)
            score_text = score_font.render("Dodgeg Controls: " + str(self.count) + "!", True, (255, 255, 255))
            textRectScore = score_text.get_rect()
            textRectScore.center = (self.w // 2, self.h // 5)
            self._display_surf.blit(score_text, textRectScore)
            large_font = pygame.font.SysFont('freesansbold.ttf', 45, True, False)
            large_text = large_font.render('Game Over', True, (255, 0, 0))
            textRect = large_text.get_rect()
            textRect.center = (self.w // 2, self.h // 2.25)
            self._display_surf.blit(large_text, textRect)
            l_font = pygame.font.SysFont('freesansbold.ttf', 30, True, False)
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
                self.player.x[0] = randint(1,540)
                self.player.y[0] = 630

                if self.player.direction == 0:
                    self.player.direction = 2
                else:
                    self.player.direction = 0

                self.__init__()
                self.on_init()
                self._game_over = False
                self._pause = False

        if self.win:
            self._display_surf.blit(self.win_image, [0, 0])
            score_font = pygame.font.SysFont('freesansbold.ttf', 25, True, False)
            score_text = score_font.render("Dodgeg Controls: " + str(self.count) + "!", True, (255, 255, 255))
            textRectScore = score_text.get_rect()
            textRectScore.center = (self.w // 2, self.h // 5)
            self._display_surf.blit(score_text, textRectScore)
            large_font = pygame.font.SysFont('freesansbold.ttf', 45, True, False)
            large_text = large_font.render('You Won! Wookie goes surfing!', True, (255, 0, 0))
            textRect = large_text.get_rect()
            textRect.center = (self.w // 2, self.h // 2.25)
            self._display_surf.blit(large_text, textRect)
            l_font = pygame.font.SysFont('freesansbold.ttf', 30, True, False)
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
                self.player.x[0] = randint(1, 540)
                self.player.y[0] = 630

                if self.player.direction == 0:
                    self.player.direction = 2
                else:
                    self.player.direction = 0

                self.__init__()
                self.on_init()
                self.win = False
                self._pause = False

        if self._quit and self._game_over == False:
            large_font = pygame.font.SysFont('freesansbold.ttf', 45, True, False)
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

        if self._pause and self._quit == False and self._game_over == False and self.win == False:
            large_font = pygame.font.SysFont('freesansbold.ttf', 45, True, False)
            large_text = large_font.render('Paused', True, (255, 201, 20))
            textRect = large_text.get_rect()
            textRect.center = (self.w // 2, self.h // 4)
            self._display_surf.blit(large_text, textRect)
            l_font = pygame.font.SysFont('freesansbold.ttf', 30, True, False)
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
                self.moved = True
            if (keys[K_LEFT]):
                self.player.moveLeft()
                self.moved = True
            if (keys[K_ESCAPE]):
                self._quit = True
                self._pause = True
            if (keys[K_SPACE]):
                self._pause = True

            self.on_loop()
            self.on_render()

            if int(self.count) < 5:
                time.sleep(100.0 / 10000.0);
            elif int(self.count) >= 5 and int(self.count) < 10:
                time.sleep(75.0 / 10000.0);
            elif int(self.count) >= 10 and int(self.count) < 20:
                time.sleep(50.0 / 10000.0);
            elif int(self.count) >= 20 and int(self.count) < 30:
                time.sleep(25.0 / 10000.0);
            elif int(self.count) >= 30:
                time.sleep(15.0 / 10000.0);
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()