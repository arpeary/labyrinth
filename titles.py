'''
Created on May 20, 2017

@author: hamret, terminellad
'''
import pygame
 
pygame.init()
 
 
class Screen():
    """
    An object for the information on a screen:
    
    Attributes:
        screen: the screen being drawn on
        scr_width, scr_height: the width and height of the screen
        bg: the background image
        clock: the time
        items: a list of items to be drawn on screen
        font1: the font
        font_color: the color of the font
    
    Methods:
        __init__: creates the attributes of a screen
        run: runs the logic behind the screen
        
    """
    def __init__(self, screen, items, bg_color=(0,0,0), font="timesnewroman",
                  font_size1=38, font_color=(220, 220, 220)):
        #######################################################################################
        # Programmer Name: Thomas, Dante
        # Date: 5/20/17
        # Purpose: initializes attributes for a screen
        # Input: self, screen, items , bg_color, font, font_size1, font_color
        # Output: attributes for a screen
        #######################################################################################
        # initialize variables
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        # load background image
        self.bg = pygame.image.load("data/image/darkbackgroundpng.png").convert_alpha()
        self.bg = pygame.transform.smoothscale(self.bg, (800,600))
        self.clock = pygame.time.Clock()
 
        self.items = items
        self.font1 = pygame.font.SysFont(font, font_size1)
        self.font_color = font_color
 
        self.items = []
        for index, item in enumerate(items):
            # creates menu list format
            label = self.font1.render(item, 1, font_color)
 
            width = label.get_rect().width
            height = label.get_rect().height
 
            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height
            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
 
            self.items.append([item, label, (width, height), (posx, posy)])
 
    def run(self):
        #######################################################################################
        # Programmer Name: Thomas, Dante
        # Date: 5/20/17
        # Purpose: runs the logic for the screen
        # Input: self
        # Output: a screen logic and output loop
        #######################################################################################
        mainloop = True
        while mainloop:

            self.clock.tick(50)
 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                    mainloop = False
 

            self.screen.blit(self.bg,(0,0))
            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))
 
            pygame.display.flip()
            
class Menu(Screen):
    """
    An object inherited from screen to be a menu:
    
    Attributes (from screen):
        screen: the screen being drawn on
        scr_width, scr_height: the width and height of the screen
        bg: the background image
        clock: the time
        items: a list of items to be drawn on screen
        font1: the font
        font_color: the color of the font
    
    Methods:
        __init__:(from screen) creates the attributes of a screen
        run: runs the logic behind the screen
        
    """
    def run(self):
        #######################################################################################
        # Programmer Name: Thomas, Dante
        # Date: 5/20/17
        # Purpose: runs the logic for the menu
        # Input: self
        # Output: a menu logic and output loop
        #######################################################################################
        intro = True
        while intro:

            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        intro = False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()

            self.screen.blit(self.bg, (0, 0))

            for name, label, (width, height), (posx, posy) in self.items:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()
