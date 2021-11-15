import pygame

# Models are called Sprites

# Controller => Sprites => Surface => Rectangle


class Projectile(pygame.sprite.Sprite):

    def __init__(self, limit):
        super().__init__()  # initializes the sprite library
        # required by sprite
        '''
        Summary: This allows us to create a projectile that allows us to shoot at the enemy objects
        args : int: start at the player and checks to see if projectile is off screen. When off screen kills projectile
        return: N/A
        
        '''


        self.image = pygame.image.load('assets/projectile.png').convert_alpha()
        self.rect = self.image.get_rect()  # rectangle
        self.limit = limit
        self.speed = 10

    # hook -
    # update method allows model updates that aren't base on events
    def update(self):
        '''
        Summary: updates projectiles since they are not based on events
        args : n/a
        return: n/a
        
        '''

        self.rect.y -= self.speed

        # check if we are outside the screen
        if self.rect.y > self.limit:
            self.kill()
