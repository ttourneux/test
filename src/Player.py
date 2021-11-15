import pygame
import random

# Models are called Sprites

# Controller => Sprites => Surface => Rectangle


class Player(pygame.sprite.Sprite):

    def __init__(self):
        '''
        Summary: this allows us to place player at their starting position
        args : NA
        return: NA
        '''
    
        super().__init__()  # initializes the sprite library
        self.health = 3
        self.direction = 'R'
        # required by sprite
        self.image = pygame.image.load('assets/hero.png').convert_alpha()
        self.rect = self.image.get_rect()  # rectangle
        self.rect.inflate_ip(-25, -25)
        self.speed = 10
        self.rect.x = 450
        self.rect.y = 500

    def move(self, direction):
        '''
        Summary: this allows the player to move
        args : NA
        return: NA
        '''
        if direction == "L":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def fight(self, opponent):
        '''
        Summary: this decides the fight result
        args : NA
        return: bool: whether the player wins the fight
        '''
        # 1/3 chance of winning
        return not bool(random.randrange(3))
