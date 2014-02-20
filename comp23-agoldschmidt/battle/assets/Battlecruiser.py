import pygame, sys, os
from Laser import *
from pygame.locals import *

class Battlecruiser(pygame.sprite.Sprite):
        '''Class for a Battlecruiser'''
        def load_image(self, image):
                try:
                        img = pygame.image.load(image)
                except pygame.error, message:
                        print "Error loading image"
                return img.convert_alpha()

        def __init__(self, screen, image, x_pos, y_pos, dx, dy, active):
                pygame.sprite.Sprite.__init__(self)
                self.screen = screen

                self.image = self.load_image(image)
                self.rect = self.image.get_rect()
                self.x = x_pos
                self.y = y_pos

                self.dx = dx
                self.dy = dy

                self.image_w, self.image_h = self.image.get_size()
                
                self.rect.move(self.x,self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

                self.active = active
        def update(self, buttonDown, direction, speed):

                if buttonDown:
                        if direction == 'UP':
                                self.dy = speed*-1
                        if direction == 'DOWN':
                                self.dy = speed
                        if direction == 'LEFT':
                                self.dx = speed*-1
                        if direction == 'RIGHT':
                                self.dx = speed
                if not buttonDown:
                        if direction == 'UP':
                                self.dy = 0
                        if direction == 'DOWN':
                                self.dy = 0
                        if direction == 'LEFT':
                                self.dx = 0
                        if direction == 'RIGHT':
                                self.dx = 0

                if (self.x + self.dx <= self.image_w/2) or (self.x + self.dx >= self.screen.get_size()[0]-self.image_w/2):
                        self.dx = 0
                if (self.y + self.dy <= self.image_h/2) or (self.y + self.dy >= self.screen.get_size()[1]-self.image_h/2):
                        self.dy = 0

                self.x += self.dx
                self.y += self.dy

                self.rect.move(self.x,self.y)
                self.rect.topleft = (self.x, self.y)
                self.rect.bottomright = (self.x + self.image_w, self.y + self.image_h)

        def draw(self):
                draw_pos = self.image.get_rect().move(self.x-self.image_w/2, self.y-self.image_h/2)
                self.screen.blit(self.image, draw_pos)
                
        
if __name__ == "__main__":
        #CONSTANTS
        FPS = 50
        SCREEN_DIMENSIONS = (800,600)
        SHIP_SPEED = 3
        LASER_SPEED = -6
        BATTLECRUISER = 'battlecruiser.gif'
        LASER = 'laser.gif'
        STAR = 'ram_aras.png'
        BACKGROUND_COLOR = (0,0,0)
        
        #VARIABLES AND INITIALIZATION
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
        pygame.display.set_caption('Battle For Ram Aras')
        clock = pygame.time.Clock()
        counter = 0
        clicked = False

        lasers = []
        bcruiser = Battlecruiser(screen, BATTLECRUISER, 400, 300, 0, 0, True)


        #GAME LOOP
        while True:
                button = ''
                #TICK CLOCK
                time_passed = clock.tick(FPS)

                #HANDLE EVENTS
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == KEYDOWN:
                                clicked = True
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                if event.key == K_UP:
                                        button = 'UP'
                                if event.key == K_DOWN:
                                        button = 'DOWN'
                                if event.key == K_LEFT:
                                        button = 'LEFT'
                                if event.key == K_RIGHT:
                                        button = 'RIGHT'
                                if event.key == K_SPACE:
                                        lasers.append(Laser(screen, LASER, bcruiser.x - bcruiser.image_h/2 + 20, bcruiser.y - 20, 0, LASER_SPEED, True))
                                        lasers.append(Laser(screen, LASER, bcruiser.x + bcruiser.image_h/2 - 20, bcruiser.y - 20, 0, LASER_SPEED, True))
                                        
                        if event.type == KEYUP:
                                if event.key != K_SPACE:
                                        clicked = False
                                if event.key == K_UP:
                                        button = 'UP'
                                if event.key == K_DOWN:
                                        button = 'DOWN'
                                if event.key == K_LEFT:
                                        button = 'LEFT'
                                if event.key == K_RIGHT:
                                        button = 'RIGHT'
                        
                #UPDATE SCREEN
                screen.fill(BACKGROUND_COLOR)

                #UPDATE SPRITES

                for laser in lasers:
                        if laser.offScreen():
                                lasers.remove(laser)
                        else:
                                laser.update()
                                laser.draw()

                bcruiser.update(clicked, button, SHIP_SPEED)
                bcruiser.draw()
                counter += 1

                #FLIP SCREEN
                pygame.display.flip()
