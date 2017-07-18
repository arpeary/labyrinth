'''
Created on May 15, 2017
@author: perrya
'''
# line.py
import pygame,random
from graphics import walls

class Line(object):
    """
    A line within a block, holds the following methods and attributes:
    
    Attributes:
        xo,yo: initial coordinate position of the line representing the side
        xf,yf: final coordinate position of the line representing the side
        image: the image that will be displayed on the 3D representation of its wall
    
    Methods:
        __init__: creates the attributes of a line
        draw: draws the line onto a 2D surface
    """
    def __init__(self,initial,final,wall):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/15/17
        # Purpose: initialize attributes of a line
        # Input: self, initial, final, wall
        # Output: attributes for a line
        #######################################################################################
        # lists for random use
        bricks=[walls.brick,walls.cracked]
        bookshelf=[walls.empty,walls.full]
        # attributes
        self.xo=initial[0]  # initial coordinates
        self.yo=initial[1]
        self.xf=final[0]    # final coordinates
        self.yf=final[1]
        if wall=="brick":
            self.image=random.choice(bricks)
        elif wall=="door":
            self.image=walls.door
        elif wall=="bookshelf":
            self.image=random.choice(bookshelf)
        
    def draw(self,surface):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/15/17
        # Purpose: draw line representing a blocks wall onto a surface
        # Input: surface
        # Output: a drawn line on the surface input
        #######################################################################################
        pygame.draw.line(surface,self.color,[self.xo,self.yo],[self.xf,self.yf],1)
