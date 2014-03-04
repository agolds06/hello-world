import pygame, sys, os
from pygame.locals import *
from random import randint

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
                self.rect.topleft = (self.x - self.image_w/2, self.y - self.image_h/2)
                self.rect.bottomright = (self.x + self.image_w/2, self.y + self.image_h/2)

                self.active = active
        def update(self, buttons, speed):

                if buttons['UP']:
                        self.dy = speed*-1
                if buttons['DOWN']:
                        self.dy = speed
                if not (buttons['UP'] or buttons['DOWN']):
                        self.dy = 0
                        
                if buttons['LEFT']:
                        self.dx = speed*-1
                if buttons['RIGHT']:
                        self.dx = speed
                if not (buttons['LEFT'] or buttons['RIGHT']):
                        self.dx = 0
                        
                if (self.x + self.dx <= self.image_w/2) or (self.x + self.dx >= self.screen.get_size()[0]-self.image_w/2):
                        self.dx = 0
                if (self.y + self.dy <= self.image_h/2) or (self.y + self.dy >= self.screen.get_size()[1]-self.image_h/2):
                        self.dy = 0

                self.x += self.dx
                self.y += self.dy

                self.rect.move(self.x,self.y)
                self.rect.topleft = (self.x - self.image_w/2, self.y - self.image_h/2)
                self.rect.bottomright = (self.x + self.image_w/2, self.y + self.image_h/2)

        def draw(self):
                draw_pos = self.image.get_rect().move(self.x-self.image_w/2, self.y-self.image_h/2)
                self.screen.blit(self.image, draw_pos)
                


