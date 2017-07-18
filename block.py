'''
Created on May 15, 2017
@author: perrya
'''
# block.py
import line
from graphics import color

class Block(object):
    """
    A block within a level, holds the following methods and attributes:
    
    Attributes:
        x,y: coordinate position of a block
        c : center coordinate of a block
        sides: a list containing each side of the block
        
    Class Attribute:
        LENGTH: constant length of each side in pixels
    
    Methods:
        __init__: creates the attributes of a block
        draw: draws each side of a block
        is_active: determines if a block is in view of a player
    """
    # class constant
    LENGTH=50
    def __init__(self,player,coords,wall):
        #######################################################################################
        # Programmer Name: Alec 
        # Date: 5/15/17
        # Purpose: initializes attributes of a block
        # Input: self, player, coords, wall
        # Output: attributes of the object
        #######################################################################################
        self.x=coords[0]        # top left coordinate
        self.y=coords[1]
        length=Block.LENGTH     # localized length of each side
        self.c=(self.x+length//2,self.y+length//2)
        # create each side in the side list
        self.sides=[line.Line([self.x+length,self.y],[self.x,self.y],wall),                  # north
                    line.Line([self.x,self.y+length],[self.x+length,self.y+length],wall),    # south
                    line.Line([self.x,self.y],[self.x,self.y+length],wall),                  # west
                    line.Line([self.x+length,self.y+length],[self.x+length,self.y],wall)]    # east
        
    def draw(self,surface):
        #######################################################################################
        # Programmer Name: Alec 
        # Date: 5/15/17
        # Purpose: draws each side of the block
        # Input: self, surface
        # Output: 1D sides drawn, representing a block, on to a 2D surface 
        #######################################################################################
        # draw each side
        for side in self.sides:
            if self.active:
                side.color=color.GREEN
            else:
                side.color=(255,200,200)
            side.draw(surface)
        
    def is_active(self,player):
        #######################################################################################
        # Programmer Name: Alec 
        # Date: 5/18/17
        # Purpose: determines if a block is in view of a player
        # Input: self, player
        # Output: boolean attribute self.active
        #######################################################################################
        length=Block.LENGTH
        if (player.direction>=315 or player.direction<45) and self.x+length+1>=player.x:
            return True
        if player.direction>=135 and player.direction<225 and self.x-1<=player.x:
            self.active=True
            return True
        if player.direction>=45 and player.direction<135 and self.y+length+1>=player.y:
            self.active=True
            return True
        if player.direction>=225 and player.direction<315 and self.y-1<=player.y:
            self.active=True
            return True
        self.active=False