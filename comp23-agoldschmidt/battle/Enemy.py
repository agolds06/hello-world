import pygame, sys, os
from pygame.locals import *
from random import randint

class Enemy(pygame.sprite.Sprite):
    '''Enemy Class'''
    def load_image(self, image):
        try:
            img = pygame.image.load(image)
        except pygame.error, message:
            print "Unable to load image"
        return img.convert_alpha()

    def __init__(self, screen, image, x, y, dx, dy, active):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        self.image = self.load_image(image)

        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

        self.image_w, self.image_h = self.image.get_size()

        self.rect = self.image.get_rect()
        
        self.rect.move(self.x, self.y)
        self.rect.topleft = (self.x - self.image_w/2, self.y - self.image_h/2)
        self.rect.bottomright = (self.x + self.image_w/2, self.y + self.image_h/2)

        self.active = active
        self.timeSinceHit = 0

    def update(self):
        if (self.x + self.dx <= self.image_w) or (self.x + self.dx > self.screen.get_size()[0] - self.image_w):
            self.dx *= -1
        if (self.y + self.dy <= self.image_h) or (self.y + self.dy > self.screen.get_size()[1] - self.image_h):
            self.dy *= -1

        self.x += self.dx
        self.y += self.dy

        self.rect.move(self.x,self.y)
        self.rect.topleft = (self.x - self.image_w/2, self.y - self.image_h/2)
        self.rect.bottomright = (self.x + self.image_w/2, self.y + self.image_h/2)

    def draw(self):
        draw_pos = self.image.get_rect().move(self.x - self.image_w/2, self.y - self.image_h/2)
        self.screen.blit(self.image, draw_pos)

                    
if __name__ == "__main__":
    #CONSTANTS
    FPS = 50
    SCREEN_DIMENSIONS = (800,600)
    MAX_SPEED = 7
    ENEMY = 'assets/mutalisk.gif'
    BACKGROUND_COLOR = (255,255,255)
    NUM_ENEMIES = 10

    #VARIABLES AND INITIALIZATION
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
    pygame.display.set_caption('Enemy Mode')
    clock = pygame.time.Clock()
    enemies = []
    for i in range(0,NUM_ENEMIES):
        enemies.append(Enemy(screen, ENEMY, randint(200,400), randint(200,400), randint(1,MAX_SPEED), randint(1,MAX_SPEED), True))

    pygame.display.flip()

    #GAME LOOP

    while True:
        time_passed = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(BACKGROUND_COLOR)
        
        for enemy in enemies:
            enemy.draw()
            enemy.update()

        
        pygame.display.flip()
