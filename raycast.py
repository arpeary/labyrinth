'''
Created on May 20, 2017
@author: perrya
'''
# raycast.py
import math,pygame
from graphics import color

class Column(object):
    """
    A vertical 2D image scaled to represent a 3D portion of a line a ray intersects with
    to give the illusion of part of a wall to the player, holds the following methods
    and attributes:
    
    Attributes:
        number: the number representing the order of a column in a players vision
        image: the scales and cropped image representing the wall seen by the ray
        distance: the distance the wall is from a player
    
    Methods:
        __init__: creates the attributes of a column
        darken_image: dims the image based on the distance a column is from a player
    """
    def __init__(self,ray):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: to create the attributes and the image of a column
        # Input: self, ray
        # Output: attributes of the ray
        #######################################################################################
        # localize variables
        side=ray.side
        img=side.image
        distance=ray.distance*math.cos(math.radians(ray.player.direction-ray.angle))
        height=img.get_height()
        width=img.get_width()
        # scale image based on distance
        scale=round((((distance+50))/45),3)    
        new_img=pygame.transform.scale(img,(int(width//(scale)),int(height//scale)))
        height=new_img.get_height()
        width=new_img.get_width()
        space=(width-height)//2
        # determine portion of image seen by ray
        if side.xf==side.xo:
            cut=math.fabs(ray.yi-side.yo)
        if side.yf==side.yo:
            cut=math.fabs(side.xo-ray.xi)
        cut=(cut*height)/50    # convert to size of image
        # create attributes
        self.number=ray.number
        self.image=new_img.subsurface(cut-10+space,0,20,height).convert_alpha()
        self.distance=ray.distance
        self.darken_image()
    
    def darken_image(self):
        #######################################################################################
        # Programmer Name: Alec
        # Date: 5/20/17
        # Purpose: dim the column based on its distance from the player
        # Input: self 
        # Output: dimmed image attribute
        #######################################################################################
        dark=pygame.Surface((self.image.get_width(),self.image.get_height()), flags=pygame.SRCALPHA)
        if 0.5*self.distance>255:
            self.distance=127
        dark.fill((int(0.5*self.distance),int(0.5*self.distance),int(0.5*self.distance),0))
        self.image.blit(dark,(0,0),special_flags=pygame.BLEND_RGBA_SUB)

def find_intersect(ray,element_list):
    #######################################################################################
    # Programmer Name: Alec
    # Date: 5/20/17
    # Purpose: find the coordinates of the closest intersection to a player
    # Input: ray, element_list
    # Output: xi, yi, side or None, None, None
    #######################################################################################
    intersects=[]                   # start with empty list
    xi=yi=None
    # for each element check for a ray collision with each line
    for element in element_list:    
        sides=element.sides
        slope=math.tan(math.radians(ray.angle))
        b=ray.yo-(slope*ray.xo)
        i=None
        for side in sides:
            if side.yo==side.yf:    # if vertical collision
                try:    
                    x=(side.yo-b)/slope
                except ZeroDivisionError:
                    x=None  
                if x:
                    if (x>=side.xo and x<=side.xf) or (x<side.xo and x>side.xf):
                        i=(x,side.yo,side)
            if side.xo==side.xf:    # if horizontal collision
                y=side.xo*slope+b
                if (y>=side.yo and y<=side.yf) or (y<=side.yo and y>=side.yf):
                    i=(side.xo,y,side)
            if i:                   # check if its in front of player
                if ray.player.direction>=135 and ray.player.direction<=225 and i[0]>=ray.xo:
                    continue
                if (ray.player.direction<=45 or ray.player.direction>=315) and i[0]<=ray.xo:
                    continue
                if ray.player.direction>=45 and ray.player.direction<=135 and i[1]<=ray.yo:
                    continue
                elif ray.player.direction<=315 and ray.player.direction>=225 and i[1]>=ray.yo:
                    continue
                intersects.append(i)
    # determine closest intersect from list
    ray.distance=ray.length
    if intersects:
        for i in intersects:
            d=math.sqrt((i[0]-ray.xo)**2+(i[1]-ray.yo)**2)
            if d<=ray.distance:
                ray.distance=d
                xi,yi,side=i[0],i[1],i[2]
        return xi,yi,side
    else:
        return None,None,None
    
def draw_screen(column_list,surface):
    #######################################################################################
    # Programmer Name: Alec
    # Date: 5/20/17
    # Purpose: draws each column onto the screen based on its distance to the player
    # Input: column_list, surface
    # Output: drawn images of each column on the surface
    #######################################################################################
    pygame.draw.rect(surface,color.BLACK,(0,0,800,300))
    pygame.draw.rect(surface,(40,40,40),(0,300,800,300))
    column_list.sort(key = lambda x: x.number,reverse=True)
    for column in column_list:
        surface.blit(column.image,(int(column.number*10-5),
                                   int(surface.get_height()//2-column.image.get_height()//2)))
        
        
        
        
        
        