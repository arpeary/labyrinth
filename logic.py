'''
Created on May 20, 2017
@author: perrya
'''
# logic.py
import raycast,pygame,player,level,sound
# variables for game loop
player1=player.Player([125,125])                # the player
levellist=[level.Level("level1.txt",player1),   # list of levels in the game
           level.Level("level2.txt",player1),
           level.Level("level3.txt",player1)]
maxlevels=len(levellist)                        # number of levels
font=pygame.font.SysFont('timesnewroman',38,True,False)    # font for printing

def print_text(font,x,y,text,surface,color=(255,255,255)):
    #######################################################################################
    # Used from in class code
    #######################################################################################
    imgText=font.render(text,True,color)
    surface.blit(imgText,(x,y))

def game(level):
    #######################################################################################
    # Programmer Name: Alec
    # Date: 5/20/17
    # Purpose: handles the logic for in-game needs
    # Input: level
    # Output: updated attributes and information on elements, player, and rays inside level
    #######################################################################################
    # localize attributes from current level
    player=level.player                     # the player
    element_list=level.element_list         # all elements
    # determine active elements
    level.active_element_list=[]            # clear the list of active elements
    for element in element_list:
        if element.is_active(player):
            level.active_element_list.append(element)
    # update the player
    player.update(element_list)   # the player's collisions and rays
        
def draw(level,surface,seconds,debug=False):
    #######################################################################################
    # Programmer Name: Alec
    # Date: 5/20/17
    # Purpose: handles drawing all visible game logic onto the surface
    # Input: level, surface, seconds, debug
    # Output: all drawn images representing a 3D first person view and mini-map if debug
    #######################################################################################
    # localize variables
    player=level.player
    column_list=[]
    for ray in player.rays: # create columns for each ray
        if ray.xi:
            col=raycast.Column(ray)
            column_list.append(col)
    # sort columns from farthest to player to closest
    raycast.draw_screen(column_list,surface)
    # print seconds left
    print_text(font,700,5,str(int(480-int(seconds))//60)+":"+str((480-int(seconds))%60),
               surface)
    # then draw the map
    if debug:
        level.minimap.draw(surface)
    
def handle_inputs(player,event):
    #######################################################################################
    # Programmer Name: Alec
    # Date: 5/20/17
    # Purpose: handle inputs from the user
    # Input: player, event
    # Output: adjusted attributes for the player and sound
    #######################################################################################
    keymap=[pygame.K_UP,pygame.K_DOWN]
    sound.play_music()
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
            player.motion=-1
        elif event.key==pygame.K_DOWN:
            player.motion=1
        if event.key==pygame.K_LEFT:
            player.rotation=1
        elif event.key==pygame.K_RIGHT:
            player.rotation=-1
        if event.key in keymap:
            sound.play_footsteps()
    elif event.type==pygame.KEYUP:
        if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
            player.motion=0
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            player.rotation=0
        if event.key in keymap:
            sound.stop_footsteps()
            