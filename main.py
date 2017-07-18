'''
Created on May 15, 2017
@author: perrya
'''
# main.py
import pygame,logic,torch,sound,titles
from graphics import color
# dimensions
SCREEN_WIDTH,SCREEN_HEIGHT=800,600
# --- INITIALIZE THE GAME ---
# - PyGame logic
pygame.init()
resolution=(SCREEN_WIDTH,SCREEN_HEIGHT)
screen=pygame.display.set_mode(resolution)
pygame.display.set_caption("Labyrinth")
clock=pygame.time.Clock()
# - Game Logic
debug=False
gamestate=1
currentlevelno=0
currentlevel=logic.levellist[currentlevelno]
start_ticks=pygame.time.get_ticks()
# create the torch sprite
light = torch.Torch(screen)
light.load("data/image/torch.png", 150, 375, 3)
light.position = 520,250
group = pygame.sprite.Group()
group.add(light)
# --- MAIN IN/OUTPUT LOOP ---
while not gamestate==0:
    ticks = (pygame.time.get_ticks() / 6)
    if gamestate==1:
        menu_items = ('Press B To Begin', '', 'Press Q to Quit')
        gm = titles.Menu(screen, menu_items)
        gm.run()
        gamestate=2
    if gamestate==2:
        menu_items = ('LABYRINTH',
                       'Rayquaza Programming',
                       " ", "INSTRUCTIONS:",
                        "Use the arrow keys to move around the map",
                        "Find the exits before time runs out!",
                        "Progress through each level,",
                         "Escape to Freedom!")
        gm = titles.Screen(screen, menu_items)
        gm.run()
        gamestate=3
    if gamestate==3:
        start_ticks=pygame.time.get_ticks()
        gamestate=4
    if gamestate==4:
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if seconds>480:
            gamestate=5
        if currentlevel.check_if_exit():
            gamestate=3
            sound.stop_music()
            sound.play_door()
            screen.fill(color.BLACK)
            pygame.display.flip()
            pygame.time.wait(3000)
            currentlevelno+=1
            if currentlevelno==logic.maxlevels:
                gamestate=6
                currentlevelno=logic.maxlevels-1
            currentlevel=logic.levellist[currentlevelno]
            logic.player1.x,logic.player1.y=currentlevel.start
        logic.game(currentlevel)
        logic.draw(currentlevel,screen,seconds,debug)
        group.update(ticks)
        group.draw(screen)
    for event in pygame.event.get():
        logic.handle_inputs(logic.player1,event)
        if event.type==pygame.QUIT:
            gamestate=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                gamestate=0
            if event.key==pygame.K_BACKQUOTE:
                debug=not debug
    if gamestate==5:
        menu_items = ('Game Over', 'Better luck next time!')
        gm = titles.Screen(screen, menu_items)
        gm.run()
        gamestate=0
    if gamestate==6:
        menu_items = ('You Escaped!','')
        gm = titles.Screen(screen, menu_items)
        gm.run()
        gamestate=0
    # update screen and set frame rate
    clock.tick(20)
    pygame.display.flip()

pygame.quit()