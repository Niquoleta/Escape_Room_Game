#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      weron
#
# Created:     01/02/2024
# Copyright:   (c) weron 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#arrow class
import pygame
import os
import sys
from settings import *

pygame.init()

class Arrow(): #the arrow button
    def __init__(self,pos,rotate,img):
        self.pos=pos
        self.rotate=rotate
        self.arrow= pygame.rect.Rect((self.pos[0], self.pos[1]), (50, 50))
        self.img=img



    def draw(self): #draw an arrow
        self.img=pygame.transform.rotate(self.img,self.rotate) #rotates it
        arrow_transform=pygame.transform.scale(self.img,(50,50)) #scales image

        screen.blit(arrow_transform,(self.pos[0],self.pos[1])) #the self is the coords, but by using rect it takes top left corner i think and thats what the coords are


    def check(self):
        if self.arrow.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False