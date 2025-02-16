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


import pygame
import os
import sys
from settings import *



pygame.init()



class Objects_Interactive():
    #def __init__(self,Left=0,Top=0,Width=0,Height=0): #left top width height
    def __init__(self, img, pos,size): #image , position of image and the size
        self.img=img
        self.pos=pos
        self.size=size

        img_transform=pygame.transform.scale(self.img,self.size)#transforming size of image
        screen.blit(img_transform,(self.pos[0],self.pos[1]))

        self.Shape=pygame.rect.Rect((self.pos[0],self.pos[1]),(self.size[0], self.size[1])) #initialising size, this allow for function "check_clicked" to work


    def check_clicked(self):
        if self.Shape.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        #the [0] is needed as theres 3 values LMB,MMB,RMB, we are looking for LMB
            return True
        else:
            return False


