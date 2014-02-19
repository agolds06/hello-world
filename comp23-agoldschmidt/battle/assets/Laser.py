import pygame, sys, os
from pygame.locals import *

class Laser(pygame.sprite.Sprite):
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

                #BACKGROUND MUSIC
                try:
                        sound = pygame.mixer.Sound("laser.wav")
                        sound.play()
                except pygame.error, message:
                        pass
                
        def update(self):
                self.x += self.dx
                self.y += self.dy

        def draw(self):
                draw_pos = self.image.get_rect().move(self.x-self.image_w/2, self.y-self.image_h/2)
                self.screen.blit(self.image, draw_pos)

        def offScreen(self):
                if (self.x + self.dx <= 0) or (self.x + self.dx >= self.screen.get_size()[0]+self.image_w/2):
                        return True
                if (self.y + self.dy <= 0) or (self.y + self.dy >= self.screen.get_size()[1]+self.image_h/2):
                        return True
                return False
