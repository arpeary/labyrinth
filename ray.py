'''
Created on May 15, 2017
@author: perrya
'''
# ray.py
import math,raycast

class Ray(object):
    """
    A ray representing a part of the players point of view,
    holds the following methods and attributes:
    
    Attributes:
        number: the number representing the order of a ray in a players vision
        xo,yo: initial coordinate position of a ray representing vision
        xf,yf: final coordinate position of a ray representing vision
        xi,yi: intersecting coordinate position of the line with
        angle: the angle a ray is pointing
        length: length of the ray, or distance the player sees
        distance: the distance an intersect is from from a player
        side: the line a ray is intersecting
        player: the player casting the ray
    
    Methods:
        __init__: creates the attributes of a ray
    """
    def __init__(self,number,player,length,angle,active_element_list):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/15/17
        # Purpose: create attributes of the player
        # Input: self, number, player, length, angle, active_element_list
        # Output: attributes for the ray
        #######################################################################################
        self.number=number                  # order of the column on the screen
        self.xo,self.yo=player.x,player.y   # initial point
        self.angle=angle                    # angle
        self.length=length                  # length of ray
        self.distance=None                  # distance of intersect from the character
        self.side=None                      # side of the element intersected
        self.player=player                  # the character casting the ray
        # calculate the final points of the ray
        self.xf,self.yf=[self.xo+self.length*math.cos(math.radians(self.angle)),
                         self.yo+self.length*math.sin(math.radians(self.angle))]
        # calculate the intersecting point of the ray
        self.xi,self.yi,self.side=raycast.find_intersect(self,active_element_list)
        