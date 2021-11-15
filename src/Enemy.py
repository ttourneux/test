import pygame
import random
# Models are called Sprites

# Controller => Sprites => Surface => Rectangle


class Enemy(pygame.sprite.Sprite):

    def __init__(self, start, window_width ):
        '''
        Summary: this allows us to place enemies at their starting position and make sure they don't go out of the window 
        args : int: start is the x coordinate of where the enemy should start, int: window_width is the parameter that allows you to make the enemy turn around when it starts to leave the page
        return: NA       
        '''
        super().__init__()  # initializes the sprite library
        # required by sprite
        self.image = pygame.image.load('assets/enemy.png').convert_alpha()
        self.rect = self.image.get_rect()  # rectangle
        self.rect.x = start
        self.rect.y = 100
        self.dir = 'L'
        #  print("window_width:",window_width)
        #print("start_range:",start_range)
        self.range = window_width
        self.paused = 0

    def pause(self):
        '''
        Summary: allows us to set how long an enemy is paused for
        args: NA 
        return: NA 
        '''
        self.paused = 50  # number of frames enemy will be paused
    # hook -
    # update method allows model updates that aren't base on events

    def update(self):

        '''
        summary: what happens each time the screen is redrawn. Enemies move left and right and each time they get to the right side of the screen they move down
        Args: NA 
        return: NA 
        '''
        if self.paused > 0:
            self.paused -= 1
        else:
            if self.rect.x >= self.range:
                self.rect.x -= 1
                self.rect.y += 100
                self.dir = 'L'
            elif self.rect.x <= 0:
                self.rect.x += 1
                self.dir = 'R'
            else:
                if self.dir == 'R':
                    self.rect.x += 1
                else:
                    self.rect.x -= 1
