'''
Created on May 15, 2017
@author: perrya
'''
# player.py
import math,ray,block

class Player(object):
    """
    A player within a level, holds the following methods and attributes:
    
    Attributes:
        x,y: coordinate position of a player
        x_old,y_old: previous coordinate position of a player
        motion: the movement of a player (forward 1, backward -1, still 0)
        vel: velocity of a player
        rotation: the turning of a player (right 1, left -1, still 0)
        omega: the rotational velocity of a player
        direction: the angle a player is facing
        fov: the field of view in degrees of a player
        rays: a list of the rays a player projects
    
    Methods:
        __init__: creates the attributes of a player
        update: updates a player and its rays, called each frame
        collision: determines if a player is colliding with an element in a level
        movement: determines movement based on the attributes changed by the user
    """
    def __init__(self,coords,fov=80):
        #######################################################################################
        # Programmer Name: Alec 
        # Date: 5/15/17
        # Purpose: initialize variables
        # Input: self, coords, fov
        # Output: attributes for object
        #######################################################################################
        # center position
        self.x,self.y=coords[0],coords[1]  
        # last center position 
        self.x_old=self.y_old=0
        self.motion=0       # represents movement (-1,0,1)
        self.vel=0          # actual speed of player
        self.rotation=0     # represents rotation (-1,0,1)
        self.omega=0        # actual rotational speed
        self.direction=90   # direction the player is facing
        self.fov=fov        # field of view in degrees
        self.rays=[]        # list of the rays a player projects
        
    def update(self,element_list,fov_step=2):    
        #######################################################################################
        # Programmer Name: Alec 
        # Date: 5/15/17
        # Purpose: update attributes of a player
        # Input: self, element_list, fov_step
        # Output: updated attributes for object
        #######################################################################################
        # movement/collision
        self.movement()  
        for element in element_list:
            self.collision(element)
        # rays
        self.rays=[]
        start=self.direction-(self.fov/2)
        for i in range(0,self.fov+fov_step,fov_step):
            cast_ray=ray.Ray(i,self,500,start+i,element_list)
            self.rays.append(cast_ray)
        
    def collision(self,element):
        #######################################################################################
        # Programmer Name: Alec 
        # Date: 5/19/17
        # Purpose: check for collision with elements in a level
        # Input: self, element
        # Output: updated coordinates outside of collided elements
        #######################################################################################
        # find boundaries of the box
        element_top,element_bot=element.y,element.y+block.Block.LENGTH
        element_left,element_right=element.x,element.x+block.Block.LENGTH
        # is player inside element?
        if self.x<=element_right+1 and self.x>=element_left-1 and self.y>=element_top-1 and self.y<=element_bot+1:
            # vertical collision
            if self.x_old<=element_right+1 and self.x_old>=element_left-1:
                if self.y>=element.c[1]:
                    self.y=element_bot+2
                elif self.y<element.c[1]:
                    self.y=element_top-2
            # horizontal collision
            if self.y_old>=element_top-1 and self.y_old<=element_bot+1:
                if self.x<=element.c[0]:
                    self.x=element_left-2
                elif self.x>element.c[0]:
                    self.x=element_right+2
    
    def movement(self):
        #######################################################################################
        # Programmer Name: Alec 
        # Date: 5/15/17
        # Purpose: determines movement of a player
        # Input: self 
        # Output: updated attributes for player
        #######################################################################################
        # 1D movement
        # accelerate the player if +/- movement
        if self.vel>-5 and self.motion==1:
            self.vel-=1
        elif self.vel<5 and self.motion==-1:
            self.vel+=1
        # decelerate the player if no movement
        elif self.vel<0 and self.motion==0:
            self.vel+=.5
        elif self.vel>0 and self.motion==0:
            self.vel-=.5
        # rotation
        # accelerate the player if rotating
        if self.omega>-9 and self.rotation==1:
            self.omega-=1
        elif self.omega<9 and self.rotation==-1:
            self.omega+=1
        # decelerate the player if no rotation
        elif self.omega<0 and self.rotation==0:
            self.omega+=1
        elif self.omega>0 and self.rotation==0:
            self.omega-=1
        # correct angle
        self.direction+=self.omega
        if self.direction>360:
            self.direction-=360
        if self.direction<0:
            self.direction+=360
        # remember last position
        self.x_old,self.y_old=self.x,self.y
        # calculate actual x/y movement
        delta_x=self.vel*math.cos(math.radians(self.direction))
        delta_y=self.vel*math.sin(math.radians(self.direction))
        self.x+=delta_x
        self.y+=delta_y