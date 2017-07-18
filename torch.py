'''
Created on May 22, 2017

@author: hamret
'''
import pygame
class Torch(pygame.sprite.Sprite):
    """
    An object derived from a sprite class to display a moving sprite
    in a secure position with getters and setters, has:
    
    Attributes:
        master_image: the image of the sprite sheet
        frame: the current frame the sprite is showing
        old_frame: the last from the sprite displays
        frame_width: the width of each frame
        frame_height: the height of each frame
        first_frame: the first frame in the loop
        last_frame: the last frame in the loop
        columns: the number of columns in the sprite sheet
        last_time: the last time
    Properties:
        X: the top left x coordinate
        Y: the top left y coordinate
        position: the coordinates of the top left corner
    Methods:
        __init__: creates the attributes of a torch
        load: loads the sprite sheet into the object
        update: updates the sprite to the correct frame
        
    """
    def __init__(self, target):
        #######################################################################################
        # Programmer Name: Thomas 
        # Date: 5/22/17
        # Purpose: initialize variables
        # Input: self, target
        # Output: attributes for object
        #######################################################################################
        pygame.sprite.Sprite.__init__(self)  # extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
    # X property
    def getx(self):
        return self.rect.x
    def setx(self, value):
        self.rect.x = value
    X = property(getx, setx)
    # Y property
    def _gety(self):
        return self.rect.y
    def _sety(self, value):
        self.rect.y = value
    Y = property(_gety, _sety)
    # position property
    def _getpos(self):
        return self.rect.topleft
    def _setpos(self, pos):
        self.rect.topleft = pos
    position = property(_getpos, _setpos)
    def load(self, filename, width, height, columns):
        #######################################################################################
        # Programmer Name: Thomas 
        # Date: 5/22/17
        # Purpose: loads the sprite sheet into attributes
        # Input: self, filename, width, height, columns
        # Output: attributes for object
        #######################################################################################
        self.master_image = pygame.image.load(filename)
        self.frame_width = width
        self.frame_height = height
        self.rect = pygame.Rect(0, 0, width, height)
        self.columns = columns
        # try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1
    def update(self, current_time, rate=30):
        #######################################################################################
        # Programmer Name: Thomas 
        # Date: 5/22/17
        # Purpose: updates the sprite to display the correct frame
        # Input: self, current_time, rate
        # Output: attributes for object
        #######################################################################################
        # update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
        # build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame