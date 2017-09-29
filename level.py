'''
Created on May 20, 2017
@author: perrya
'''
# level.py
import pygame,math,block
from graphics import color

class Level(object):
    """
    An object holding the information on itself and the elements within it,
    has the following methods and attributes:
    
    Attributes:
        element_list: list of the elements within the level
        player: the player in the level
        minimap: an object of that maps minimap
        height: the length of the level
        exit: the top left coordinates of the exit block of the level
        start: the center of the starting block of the level
    
    Methods:
        __init__: creates the attributes of a level
        create_minimap: creates a minimap object of the level
        check_if_exit: checks if the player is within the exit square of the level
        load: loads the list of elements and their locations from a file
        
    """
    def __init__(self,filename,player):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: initializes attributes for a level
        # Input: self, filename, player
        # Output: attributes for a level
        #######################################################################################
        self.element_list=[]            # a list of the elements within
        self.player=player              # the player within the level
        self.minimap=None               # the level's mini-map
        self.height=0                   # length of level
        self.exit=None                  # top left location of exit square
        self.start=[]                   # middle of starting location square
        # load and create mini-map
        self.load(filename)
        self.create_minimap(10,10,(self.height,self.height),100)
        
    def create_minimap(self,x,y,dimensions,alpha):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: creates a minimap object of a level
        # Input: self, x, y, dimensions, alpha
        # Output: minimap object as level attribute
        #######################################################################################
        self.minimap=Minimap(self,x,y,dimensions,alpha)
    
    def check_if_exit(self):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: checks if the player is inside a level's exit square
        # Input: self
        # Output: boolean
        #######################################################################################
        if self.player.x>self.exit[0] and self.player.x<self.exit[0]+50:
            if self.player.y>self.exit[1] and self.player.y<self.exit[1]+50:
                return True
        return False
    
    def load(self,filename):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: to load the level's elements from a file
        # Input: self, filename
        # Output: element_list attribute, height attribute
        #######################################################################################
        file=open("data/level/"+filename,"r")   # open file
        lines=file.readlines()                  # list of lines
        pos=[0,0]                               # origin position
        for line in lines:                      # for each line go through each character:
            for char in line:                       # for each character: 
                if char=="#":                           # determine the block it creates
                    b=block.Block(self.player,(pos),"brick")
                    self.element_list.append(b)
                elif char=="D":
                    self.exit=[pos[0],pos[1]]
                elif char=="F":
                    b=block.Block(self.player,(pos),"door")
                    self.element_list.append(b)
                elif char=="B":
                    b=block.Block(self.player,(pos),"bookshelf")
                    self.element_list.append(b)
                elif char=="S":
                    self.start=[pos[0]+25,pos[1]+25]
                pos[0]+=50              # move the x position for the next block
            pos[0]=0                    # reset x coordinate
            pos[1]+=50                  # move the y position for the next row
        self.height=pos[1]              # assign the height as the final y position
        file.close()                    # close the file
        
class Minimap(object):
    """
    An object holding the information on how to draw a minimap
    representing the level's layout, includes methods and attributes:
    
    Attributes:
        level: the level a minimap represents
        x,y: the top left coordinates of a map on the screen
        dimensions: the dimensions of the level
        dim: the final dimensions of a map on screen
        alpha: the transparency of a map
    
    Methods:
        __init__: creates the attributes of a minimap
        
    """
    def __init__(self,lev,x,y,dim,alp):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: initialize attributes for a map
        # Input: self, lev, x, y, dim, alp
        # Output: attributes for a map
        #######################################################################################
        self.level=lev          # the level
        self.x,self.y=x,y       # top left coordinates
        self.dimensions=dim     # dimensions of the level
        self.dim=(600,600)      # final dimensions of map
        self.alpha=alp          # transparency of the map
    
    def draw_player(self,surface,player):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: draw the player and a line representing its direction on the map
        # Input: self, surface, player
        # Output: a drawn circle and line representing the player on the map
        #######################################################################################
        # draw the player's rays
        for ray in player.rays:
            if ray.xi:  # if intersect, draw the intersecting ray
                pygame.draw.line(surface,(0,255,0),(ray.xo,ray.yo),(ray.xi,ray.yi),2)
            else:       # or draw the full ray
                pygame.draw.line(surface,color.BLACK,(ray.xo,ray.yo),(ray.xf,ray.yf))
        # draw player circle and direction arrow
        end_ray=(10*math.cos(math.radians(player.direction))+ray.xo,
                 10*math.sin(math.radians(player.direction))+ray.yo)
        pygame.draw.line(surface,color.RED,[int(player.x),int(player.y)],end_ray,2)
        pygame.draw.circle(surface,color.BLACK,[int(player.x),int(player.y)],5)
        
    def draw_element(self,surface,element):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: draw an element on the surface
        # Input: self, surface, element
        # Output: a drawn element on the surface
        #######################################################################################
        # determine element's color by its active method
        for side in element.sides:
            if element.is_active(self.level.player):
                c=color.GREEN
            else:
                c=(255,200,200)
            pygame.draw.line(surface,c,[side.xo,side.yo],[side.xf,side.yf],1)
    
    def draw(self,surface):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: draw the whole minimap on the screen
        # Input: self, surface
        # Output: a drawn minimap on the screen in its desired location
        #######################################################################################
        minimap=pygame.Surface(self.dimensions)     # surface to draw by scale of level
        minimap.fill(color.WHITE)                   # fill the surface
        for element in self.level.element_list:     # draw each element
            self.draw_element(minimap,element)
        self.draw_player(minimap,self.level.player) # draw the player
        scaled_minimap=pygame.transform.smoothscale(minimap,(self.dim)) # scale the map down
        scaled_minimap.set_alpha(self.alpha)                            # set transparency
        surface.blit(scaled_minimap,(self.x,self.y))                    # draw to surface
        