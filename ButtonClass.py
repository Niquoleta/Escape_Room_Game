#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      weron
#
# Created:     30/01/2024
# Copyright:   (c) weron 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#button
import pygame
import os
import sys
from settings import *

pygame.init()

class Button:
    def __init__(self, txt, pos):
        self.text = txt #specific text given as a parameter
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40)) #takes left,top,width and height
        #the 0 and 1 is index, using the given parameters (coordinates from code calling it)

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5) #takes surface, colour the previous measurements and fills the box
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5) #outlines the button, 260 and 40 is height and width
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        #checks if condition of mouse has been clicked
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            #the [0] is needed as theres 3 values LMB,MMB,RMB, we are looking for LMB
            return True
        else:
            return False

