from pygame.locals import *
import pygame
import time
from random import randint

class Ball:
    x = 0
    y = 0
    step = 44
    direction = 4

    updateCountMax = 2
    updateCount = 0

    def __init__(self):
        # initial positions, no collision.
        self.x = (15 * 44)
        self.y = randint(7,8) * 44
        self.direction = 4

    def update(self):
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
            # update position of head of snake
            if self.direction == 0:
                self.x = self.x + (self.step / 2)
                self.y = self.y - self.step
            if self.direction == 1:
                self.x = self.x + (self.step/2)
                self.y = self.y + self.step
            if self.direction == 2:
                self.x = self.x - (self.step/2)
                self.y = self.y - self.step
            if self.direction == 3:
                self.y = self.y + self.step
                self.x = self.x - (self.step/2)
            if self.direction == 4:
                self.y = self.y + self.step
            if self.direction == 5:
                self.y = self.y - self.step
            self.updateCount = 0

    def moveUpRight(self):
        self.direction = 0

    def moveDownRight(self):
        self.direction = 1

    def moveUpLeft(self):
        self.direction = 2

    def moveDownLeft(self):
        self.direction = 3

    def moveUp(self):
        self.direction = 5

    def moveDown(self):
        self.direction = 4

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))


class Player:
    x = 0
    y = 0
    step = 68
    direction = 0
    length = 10

    updateCountMax = 2
    updateCount = 0

    def __init__(self):

        self.x = 15 * 44
        self.y = 16 *44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            if self.direction == 0:
                self.x = self.x + self.step
            if self.direction == 1:
                self.x = self.x - self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class PlayerTwo:
    x = 0
    y = 0
    step = 44
    direction = 0
    length = 10

    updateCountMax = 2
    updateCount = 0

    def __init__(self):

        self.x = 15 * 44
        self.y = 0 * 44

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            if self.direction == 0:
                self.x = self.x + self.step
            if self.direction == 1:
                self.x = self.x - self.step

            self.updateCount = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class Game:

    def isCollision(self,x1,y1,x2,y2,bsize, bheight):
        if x1 >= x2 and x1 <= x2 + bsize or x2 >= x1 and x2 <= x1 + bsize:
            if y1 >= y2 and y1 <= y2 + bheight or y2 >= y1 and y2 <= y1 + bheight:
                return True
        return False

    def isMissed(self, y1, y2):
        if y1 == y2:
            return True
        return False

    def isTopWall(self, y):
        if y < 44:
            return True
        return False

    def isBottomWall(self, y, h):
        if y > (h - 88):
            return True
        return False

    def isLeftWall(self, x):
        if x < 0:
            return True
        return False

    def isRightWall(self, x, w):
        if x > (w - 44):
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
    playerTwo = 0
    ball = 0
    score1 = 0
    score2 = 0
    w = 0
    h = 0
    width = 0
    height = 0
    times_played = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._image_surf2 = None
        self._background_image = None
        self._ball_surf = None
        self._text = None
        self.game = Game()
        self.player = Player()
        self.playerTwo = PlayerTwo()
        self.ball = Ball()
        self.score1 = 0
        self.score2 = 0
        self.width = 0
        self.height = 0
        self._game_over = False
        self.w = None
        self.h = None
        self._pause = False
        self._quit = False
        self._times_played = 2
        self.moved = False
        self.movedTwo = False
        self.one_won = False
        self.two_won = False

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.w, self.h = pygame.display.get_surface().get_size()
        self.width = (self.w/44) - 1
        self.height = (self.h/44) - 1
        pygame.display.set_caption('Snake Game')
        self._running = True
        self._image_surf = pygame.image.load("lego_tennis1.png").convert()
        self._image_surf2 = pygame.image.load("lego_tennis2.png").convert()
        self._ball_surf = pygame.image.load("ball.png").convert()
        if self.times_played % 2 == 0:
            self._background_image = pygame.image.load("tennis.png").convert()
        else:
            self._background_image = pygame.image.load("tennis.png").convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        if self._pause == False:
            self.ball.update()

            if self.game.isTopWall(self.ball.y):
                if self.game.isCollision(self.ball.x, self.ball.y, self.playerTwo.x, self.playerTwo.y, 68, 44):
                    if self.playerTwo.direction == 0:
                        self.ball.moveDownRight()
                    if self.playerTwo.direction == 1:
                        self.ball.moveDownLeft()
                else:
                    self.score1 = self.score1 + 1
                    self.one_won = True

            if self.game.isBottomWall(self.ball.y, self.h):
                if self.game.isCollision(self.ball.x, self.ball.y, self.player.x, self.player.y, 68, 44):
                    if self.player.direction == 1:
                        self.ball.moveUpLeft()
                    if self.player.direction == 0:
                        self.ball.moveUpRight()
                else:
                    self.score2 = self.score2 + 1
                    self.two_won = True

            if self.game.isLeftWall(self.ball.x):
                if self.ball.direction == 2:
                    self.ball.moveUpRight()
                if self.ball.direction == 3:
                    self.ball.moveDownRight()

            if self.game.isRightWall(self.ball.x, self.w):
                if self.ball.direction == 0:
                    self.ball.moveUpLeft()
                if self.ball.direction == 1:
                    self.ball.moveDownLeft()

            if self.moved:
                self.player.update()

                if self.game.isWall(self.player.x, self.player.y, self.w, self.h):
                    if int(self.player.x) < 0:
                        self.player.x = 44

                    if int(self.player.x) > (int(self.w) - 44):
                        self.player.x = (self.w - 44)

                self.moved = False

            if self.movedTwo:
                self.playerTwo.update()

                # does player hit the wall?
                if self.game.isWall(self.playerTwo.x, self.playerTwo.y, self.w, self.h):
                    if int(self.playerTwo.x) < 0:
                        self.playerTwo.x = 44

                    if int(self.playerTwo.x) > (int(self.w) - 44):
                        self.playerTwo.x = (self.w - 44)

                self.movedTwo = False

            pass

    def on_render(self):
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(self._background_image, [0, 0])
        self.player.draw(self._display_surf, self._image_surf)
        self.playerTwo.draw(self._display_surf, self._image_surf2)
        self.ball.draw(self._display_surf, self._ball_surf)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text1 = font.render("Player One: " + str(self.score1), True, (0,0,0))
        text2 = font.render("Player Two: " + str(self.score2), True, (255,255,255))
        self._display_surf.blit(text1, [5, 5])
        self._display_surf.blit(text2, [5, 35])

        if self.one_won:
            self.ball.x = 15 * 44
            self.ball.y = randint(7, 8) * 44
            self.ball.direction = 4
            self.player.x = 15 * 44
            self.playerTwo.x = 15 * 44
            score_font = pygame.font.SysFont('freesansbold.ttf', 125, True, False)
            score_text = score_font.render("Player One won a point!", True, (255, 201, 20))
            textRectScore = score_text.get_rect()
            textRectScore.center = (self.w // 2, self.h // 2)
            self._display_surf.blit(score_text, textRectScore)
            pygame.display.flip()
            time.sleep(2)
            self.one_won = False

        if self.two_won:
            self.ball.x = 15 * 44
            self.ball.y = randint(7, 8) * 44
            self.ball.direction = 5
            self.player.x = 15 * 44
            self.playerTwo.x = 15 * 44
            score_font = pygame.font.SysFont('freesansbold.ttf', 125, True, False)
            score_text = score_font.render("Player Two won a point!", True, (255, 201, 20))
            textRectScore = score_text.get_rect()
            textRectScore.center = (self.w // 2, self.h // 2)
            self._display_surf.blit(score_text, textRectScore)
            pygame.display.flip()
            time.sleep(2)
            self.two_won = False

        if self._game_over:
            score_font = pygame.font.SysFont('freesansbold.ttf', 125, True, False)
            score_text = score_font.render("Game, Set and Match!", True, (255, 255, 255))
            textRectScore = score_text.get_rect()
            textRectScore.center = (self.w // 2, self.h // 5)
            self._display_surf.blit(score_text, textRectScore)
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
                self.player.x = 15 * 44
                self.playerTwo.x = 15 * 44

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
                self.moved = True
            if (keys[K_LEFT]):
                self.player.moveLeft()
                self.moved = True
            if (keys[K_d]):
                self.playerTwo.moveRight()
                self.movedTwo = True
            if (keys[K_a]):
                self.playerTwo.moveLeft()
                self.movedTwo = True
            if (keys[K_ESCAPE]):
                self._quit = True
                self._pause = True
            if (keys[K_SPACE]):
                self._pause = True

            self.on_loop()
            self.on_render()

            time.sleep(100.0 / 10000.0);

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()