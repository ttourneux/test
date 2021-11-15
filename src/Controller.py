from src import Player
from src import Enemy
from src import Projectile

import pygame
import random


class Controller:

    def __init__(self):
        #configure pygame]
        # setup pygame data
        '''
        Summary: configues pygame, allows us to setup necessary data for running the game
        args : n/a
        return: n/a
      
        '''

        self.window_width = 900         
        self.window_height = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.background = pygame.Surface((self.window_width, self.window_height))
        self.background.fill((0, 0, 0))
        # held keys act like repeated strike
        pygame.key.set_repeat(50, 500)

        #create modle objects
        self.player = Player.Player()
        self.enemies = pygame.sprite.Group()
        for e in range(3):
            self.enemies.add(Enemy.Enemy(e*100, self.window_width))

        self.projectiles = pygame.sprite.Group()
        # cast existing groups to a tuple to add them together with other sprites and make a new group
        self.all_sprites = pygame.sprite.Group(tuple(self.enemies) + (self.player,))

    def mainloop(self):

        '''
        Summary: configues pygame, allows us to setup necessary data for running the game. Note: each loop is only one frame!
        args : n/a
        return: n/a
        
        '''

        while True:  # one time through the loop is one frame (picture)
            # check for events

          

            self.eventloop()

            # update models
            self.enemies.update()
            self.projectiles.update()

            # collisions
            fight = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if fight:
                for enemy in fight:
                    if self.player.fight(enemy):
                        enemy.kill()
                    else:
                        self.player.health -= 1

            bullets = pygame.sprite.groupcollide(self.enemies, self.projectiles, False, True)
            if bullets:
                for enemy in bullets:
                    enemy.pause()

            # end the program
            if self.player.health == 0:
                return

            # redraw
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)
            self.projectiles.draw(self.screen)

            # update the screen
            pygame.display.flip()

    # OPTIONAL: put the event loop in a seperate method just to break up the mainloop()
    def eventloop(self):

        '''
        Summary: handles events that occur within the game. Used to later pass back into mainloop
        args : n/a
        return: n/a  
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move("L")
                if event.key == pygame.K_RIGHT:
                    self.player.move("R")
                if event.key == pygame.K_SPACE:
                    if len(self.projectiles.sprites()) <= 5:
                        p = Projectile.Projectile(self.window_width)
                        pos = self.player.rect.midright
                        p.rect.x = pos[0]
                        p.rect.y = pos[1]
                        self.projectiles.add(p)
                        self.all_sprites(p)
                    else:
                        print("can't shoot", len(self.projectiles.sprites()))
