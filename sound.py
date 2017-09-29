'''
Created on May 16, 2017
@author: hamret
'''
# sound.py
import pygame
pygame.mixer.init()

footsteps = pygame.mixer.Sound('data/sound/footsteps loop.wav')
torch = pygame.mixer.Sound('data/sound/torch sound effect.wav')
door = pygame.mixer.Sound('data/sound/door.wav')
pygame.mixer.music.load('data/sound/ambience.wav')

def play_music():
    #######################################################################################
    # Programmer Name: Thomas
    # Date: 5/16/17
    # Purpose: plays background music
    # Input: None
    # Output: game music
    #######################################################################################
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)

def stop_music():
    #######################################################################################
    # Programmer Name: Thomas
    # Date: 5/16/17
    # Purpose: stops background music
    # Input: None
    # Output: stopped game music
    #######################################################################################
    pygame.mixer.music.stop()

def play_door():
    #######################################################################################
    # Programmer Name: Thomas
    # Date: 5/16/17
    # Purpose: plays door sound
    # Input: None
    # Output: door sound
    #######################################################################################
    door.play()

def play_footsteps():
    #######################################################################################
    # Programmer Name: Thomas
    # Date: 5/16/17
    # Purpose: plays footsteps
    # Input: None
    # Output: footstep sound
    #######################################################################################
    footsteps.play(-1)

def stop_footsteps():
    #######################################################################################
    # Programmer Name: Thomas
    # Date: 5/16/17
    # Purpose: plays background music
    # Input: None
    # Output: stop footstep sound
    #######################################################################################
    footsteps.stop()