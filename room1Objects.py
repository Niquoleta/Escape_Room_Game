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

#room 1 objects
import settings


def Pencil():

    if object_state[0]== False: #if the state is false, it is not in the inventory, from here we could also makek it not appear in room2
        pencil=Objects_Interactive(pencil_img,[60,60],[50,50]) #left top width height
        if pencil.check_clicked(): #checking that if the area is clicked then it outputs true, this is also known as object 1
            pencil=Objects_Interactive(pencil_img,[740,80],[50,50]) #coords that change once area has been clicked
            object_state[0]=True #the object goes to the inventory

    else:
        pencil=Objects_Interactive(pencil_img,[740,80],[50,50]) # should not disappear

def Safe():
    global slide_check
    if object_state[1]== False: #if the state is false, it is not in the inventory, from here we could also makek it not appear in room2
        safe=Objects_Interactive(safe_img,[550,100],[50,50]) #left top width height
        slide_check=0
        if safe.check_clicked(): #checking that if the area is clicked then it outputs true, this is also known as object 2
            object_state[1]=True # the object has been clicked on and will disappear
            return True
    #else:
    #    self.slide_check=3
    #    PuzzleOne=Puzzle1(100,100,400,400)
