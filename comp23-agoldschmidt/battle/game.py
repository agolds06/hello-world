import pygame, sys, os
from pygame.locals import *
from Battlecruiser import *
from Laser import *
from Enemy import *
from Scroller import *

def reflect(sprite1, sprite2):
        if sprite1.dx > 0 and sprite2.dx < 0:
                sprite1.x -= 1
                sprite1.dx *= -1
                sprite2.x += 1
                sprite2.dx *= -1
        if sprite1.dy > 0 and sprite2.dy < 0:
                sprite1.y -= 1
                sprite1.dy *= -1
                sprite2.y -= 1
                sprite2.dy *= -1
        if sprite1.dx > 0 and sprite2.dx > 0 and sprite1.dx > sprite2.dx:
                sprite1.x += 1
                sprite2.x -= 1
                sprite2.dx *= -1
        if sprite1.dy > 0 and sprite2.dy > 0 and sprite1.dy > sprite2.dy:
                sprite1.y += 1
                sprite2.y -= 1
                sprite2.dy *= -1
        if sprite1.dx < 0 and sprite2.dx < 0 and sprite1.dx < sprite2.dx:
                sprite1.x -= 1
                sprite2.x += 1
                sprite2.dx *= -1
        if sprite1.dy < 0 and sprite2.dy < 0 and sprite1.dy < sprite2.dy:
                sprite1.y -= 1
                sprite2.y += 1
                sprite2.dy *= -1

def gameOver(screen, score, bcruiser):
        loop = True
        try:
                sound = pygame.mixer.Sound("assets/death_explode.wav")
                sound.play()
        except pygame.error, message:
                pass
        screen.fill((255,255,255))
        back = screen
        screen.blit(back, (0,0))
        font = pygame.font.Font(None, 40)
        text = font.render("GAME OVER", 1, (255,0,0))
        scr = font.render ("FINAL SCORE: " + str(score), 1, (255,0,0))
        replay = font.render("HIT ENTER/RETURN TO PLAY AGAIN", 1, (255,0,0))
        while loop == True:
                for event in pygame.event.get():
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                if event.key == K_RETURN:
                                        loop = False
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                screen.fill((0,0,0))
                screen.blit(back, (0,0))
                screen.blit(text, (300,200))
                screen.blit(scr, (270,250))
                screen.blit(replay, (150,300))
                pygame.display.flip()
        bcruiser.active = True
        
        return 0

if __name__ == "__main__":
        #CONSTANTS
        FPS = 50
        SCREEN_DIMENSIONS = (800,600)
        SHIP_SPEED = 4
        LASER_SPEED = 7
        BATTLECRUISER = 'assets/battlecruiser.gif'
        LASER = 'assets/laser.gif'
        STAR = 'assets/ram_aras.png'
        ENEMY = 'assets/mutalisk.gif'
        BACKGROUND_COLOR = (0,0,0)
        SCROLL_SPEED = -1
        MAX_AMMO = 20
        NUM_ENEMIES = 7
        ENEMY_SPEED = 5
        
        #VARIABLES AND INITIALIZATION
        pygame.init()
        screen = pygame.display.set_mode(SCREEN_DIMENSIONS)
        pygame.display.set_caption('Battle For Ram Aras')
        clock = pygame.time.Clock()
        counter = 20
#        intro_screen(screen)
        buttons = {'UP': False, 'DOWN': False, 'LEFT': False, 'RIGHT': False, 'SPACE': False}
        lasers = []
        bcruiser = Battlecruiser(screen, BATTLECRUISER, 200, 300, 0, 0, True)
        enemies = []
        enemies.append(Enemy(screen, ENEMY, randint(400, 730), randint(70, 530), randint(1,ENEMY_SPEED), randint(1, ENEMY_SPEED), True))


        background = []
        background.append(Scroller(screen, SCROLL_SPEED))
        score = 0

        font = pygame.font.Font(None, 36)
#        text = font.render("AMMO: " + str(counter), 1, (255,0,0))
        cooldown = 10
#        cool = font.render("COOLDOWN: " + str(cooldown), 1, (255,0,0))
        scr = font.render("SCORE: " + str(score), 1, (255,0,0))
#        screen.blit(text, (10,10))
#        screen.blit(cool, (250,10))
        screen.blit(scr, (500,10))
        
        pygame.display.flip()
        reloadTime = 0
        #GAME LOOP
        while True:
                button = ''
                #TICK CLOCK
                time_passed = clock.tick(FPS)
                reloadTime += 1
                if cooldown < 10 and reloadTime%2 == 0:
                        cooldown += 1
                if counter < MAX_AMMO and reloadTime%20 == 0:
                        counter += 1
                #HANDLE EVENTS
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                        pygame.quit()
                                        sys.exit()
                                if event.key == K_UP:
                                        buttons['UP'] = True
                                        buttons['DOWN'] = False
                                if event.key == K_DOWN:
                                        buttons['DOWN'] = True
                                        buttons['UP'] = False
                                if event.key == K_LEFT:
                                        buttons['LEFT'] = True
                                        buttons['RIGHT'] = False
                                if event.key == K_RIGHT:
                                        buttons['RIGHT'] = True
                                        buttons['LEFT'] = False
                                if event.key == K_SPACE:
                                        buttons['SPACE'] = True
                        if event.type == KEYUP:
                                if event.key == K_UP:
                                        buttons['UP'] = False
                                if event.key == K_DOWN:
                                        buttons['DOWN'] = False
                                if event.key == K_LEFT:
                                        buttons['LEFT'] = False
                                if event.key == K_RIGHT:
                                        buttons['RIGHT'] = False
                                if event.key == K_SPACE:
                                        buttons['SPACE'] = False

                if buttons['SPACE'] and counter > 0 and cooldown == 10:
                        lasers.append(Laser(screen, LASER, bcruiser.x + bcruiser.image_w/2 - 15, bcruiser.y - 20, 0, -1*LASER_SPEED, True))
                        lasers.append(Laser(screen, LASER, bcruiser.x - bcruiser.image_w/2 + 15, bcruiser.y - 20,0, -1*LASER_SPEED, True))

                        counter -= 1
                        cooldown = 0
                                      

                #ADD ENEMIES
                if enemies == [] or (reloadTime%200 == 0 and len(enemies) < NUM_ENEMIES):
                        enemies.append(Enemy(screen, ENEMY, randint(80, 530), randint(80, 300), randint(1,ENEMY_SPEED), randint(1,ENEMY_SPEED), True))
                                                
                #COLLISION DETECTION
                                                
                for enemy in enemies:
                        if enemy.active == False:
                                if enemy.timeSinceHit == 5:
                                        enemies.remove(enemy)
                                else:
                                        enemy.timeSinceHit += 1
                for laser in lasers:
                        for enemy in enemies:
                                if pygame.sprite.collide_rect(laser, enemy) and laser.active:
                                        enemy.dx = 0
                                        if enemy.active:
                                                score += 100
                                        enemy.dy = 0
                                        enemy.active = False
                                        laser.explode()
                                        laser.active = False
                                        laser.dx = 0
                        if laser.active == False:
                                if laser.timeSinceHit == 5:                                
                                        lasers.remove(laser)
                                else:
                                        laser.timeSinceHit += 1
                                                
                for enemy1 in enemies:
                        for enemy2 in enemies:
                                if enemy1 != enemy2 and pygame.sprite.collide_rect(enemy1,enemy2):
                                        reflect(enemy1, enemy2)

                for enemy in enemies:
                        if pygame.sprite.collide_rect(enemy, bcruiser) and bcruiser.active:
                                bcruiser.active = False
                                enemies = []
                                lasers = []
                                bcruiser.x = 200
                                bcruiser.y = 300
                                bcruiser.dx = 0
                                bcruiser.dy = 0
                                for button in buttons:
                                        buttons[button] = False
                                score = gameOver(screen,score, bcruiser)
                                background = []
                                background.append(Scroller(screen, SCROLL_SPEED))
                #UPDATE SCREEN
                screen.fill(BACKGROUND_COLOR)
                #UPDATE SPRITES
                for clip in background:
                        if not clip.update():
                                score = gameOver(screen, score, bcruiser)
                                background = []
                                background.append(Scroller(screen, SCROLL_SPEED))
                        clip.draw()

                for enemy in enemies:
                        enemy.update()
                        enemy.draw()

                for laser in lasers:
                        if laser.offScreen():
                                lasers.remove(laser)
                        else:
                                laser.update()
                                laser.draw()

                
                bcruiser.update(buttons, SHIP_SPEED)
                bcruiser.draw()

#                text = font.render("AMMO: " + str(counter), 1, (255,0,0))
#                cool = font.render("COOLDOWN: " + str(cooldown), 1, (255,0,0))
                scr = font.render("SCORE: " + str(score), 1, (255,0,0))
#                screen.blit(text, (10,10))
#                screen.blit(cool, (250,10))
                screen.blit(scr, (500,10))

                #FLIP SCREEN
                pygame.display.flip()
