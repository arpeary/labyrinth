'''
Created on May 20, 2017
@author: perrya
'''
# graphics.py
import pygame

class color(object):
    """
    A class used to utilize dot notation for ease of
    access to color tuples for use with pygame:
    
    Class Attributes:
        BLACK: the color BLACK        WHITE: the color WHITE
        RED: the color RED            ORANGE: the color ORANGE
        YELLOW: the color YELLOW      GREEN: the color GREEN
        BLUE: the color BLUE          VIOLET: the color VIOLET
    """
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    RED=(209,0,0)
    ORANGE=(255,102,34)
    YELLOW=(255,218,33)
    GREEN=(0,155,0)
    BLUE=(17,51,204)
    VIOLET=(51,0,68)


class walls(object):
    """
    A class used to utilize dot notation for ease of
    access to images for walls on each block:
    
    Class Attributes:
        brick: a stone brick wall
        cracked: a cracked stone brick wall
        door: a stone brick wall with a door in it
        empty: an empty bookshelf
        full: a bookshelf with books
    """
    brick=pygame.image.load("data/image/brick.png")
    cracked=pygame.image.load("data/image/brickcracked.png")
    door=pygame.image.load("data/image/door.png")
    empty=pygame.image.load("data/image/emptybookshelf.png")
    full=pygame.image.load("data/image/fullbookshelf.png")