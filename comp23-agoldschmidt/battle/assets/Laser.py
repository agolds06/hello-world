import pygame, sys, os
from pygame.locals import *
from random import randint

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

if __name__ == "__main__":

        #CONSTANTS
        SCREEN_DIMENSIONS = (800,600)
        FPS = 50
        MAX_LASER_SPEED = 10
        LASER = 'laser.gif'
        BACKGROUND_COLOR = (0,0,0)
        #VARIABLES AND INITIALIZATION
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
        pygame.display.set_caption('Lasers')
        clock = pygame.time.Clock()
        lasers = []
        lasers = pygame.sprite.Group()
        

        #GAME LOOP
        while True:
                time_passed = clock.tick(FPS)

                # Add a new laser at random x-coordinate with random speed
                lasers.add(Laser(screen, LASER, randint(1, 750), 550, 0, randint(1, 10) * -1, False))

                # Event handling here (to quit)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        elif event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()					

                # Redraw the background
                screen.fill(BACKGROUND_COLOR)

                # Update and redraw all sprites
                for laser in lasers:
                        if laser.offScreen():
                                lasers.remove(laser)
                        laser.update()
                        laser.draw()

                # Draw the sprites
                pygame.display.update()
