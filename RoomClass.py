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


#room class
import pygame
import os
import sys
import settings
from ObjectsClass import Objects_Interactive
import ButtonClass
from ArrowClass import Arrow

pygame.init()



#def draw_MENUBUTTON():
 #   menu_btn = ButtonClass.Button('Main Menu', (settings.WIDTH-200, 10)) #draws menu button in game, allows user to return to menu
  #  menu_btn.draw()
   # menu = menu_btn.check_clicked()
    #return menu

class Room():
    def __init__(self,size=(0,0), image="unknown"): #standard room attributes
        self.size=size #size of background
        self.image=image


    def draw_inventory(self): #inventory in each room is drawn
        pygame.draw.rect(settings.screen, 'grey', [settings.WIDTH-200, 40, 200, 650], 0, 5)
        pygame.draw.rect(settings.screen, 'dark gray', [settings.WIDTH-200, 40, 200,650], 5, 5)

        if settings.object_state[2]==True:
            reward=Objects_Interactive(settings.KeyYellow_img,[1000,270],[50,50]) # this is to true when puzzle1 has correctly been answered, shows up in invenotry
        if settings.object_state[0]==True: #the object goes to the inventory, this is the key from the cupboard
            key=Objects_Interactive(settings.KeyBlue_img,[930,100],[50,50]) #coords that change once area has been clicked
        if settings.object_state[4]==True: #in order for tv remote to be drawn in inventory in different rooms
            TVremote=Objects_Interactive(settings.TVremote_img,[1000,170],[50,50])
        if settings.object_state[9]==True: #in order for fingerprint scanner to be drawn in inventory in different rooms
            reward2=Objects_Interactive(settings.scan2_img,[930,220],[50,50])

#================ room 1: living room ================================

class room1(Room): #1st room
    def __init__(self,office_img):
        super().__init__(size=(900,530),image=office_img) #uses parent class
        office_transform=pygame.transform.scale(self.image,self.size)#rotation
        settings.screen.blit(office_transform,(0,40))
        objectiveText= settings.font.render("Objectives: Find Key, Solve Secret Code", True, 'black')
        settings.screen.blit(objectiveText, (10, 10))

    def Safe(self):
        #global slide_check
        if settings.object_state[1]== False: #if the state is false, it is not in the inventory, from here we could also makek it not appear in room2
            safe=Objects_Interactive(settings.safe_img,[400,480],[50,50]) #left top width height
            settings.slide_check=0 #changes the global value slide check
            if safe.check_clicked(): #checking that if the area is clicked then it outputs true, this is also known as object 2
                settings.object_state[1]=True # the object has been clicked on and will disappear

        else:
            settings.slide_check=3


def KeyBlue():
    if settings.object_state[0]== False: #if the state is false, it is not in the inventory, from here we could also makek it not appear in room2
        settings.object_state[0]=True #the object goes to the inventory
    else:

        exit

def TVdraw():
    TV=Objects_Interactive(settings.TV_img,[400,325],[140,100])
    if settings.object_state[4]==True and TV.check_clicked(): #if user has obtained the TV remote and clicked the TV
        Code1= settings.font.render("OAY___", True, 'white') #displays the code to safe
        settings.screen.blit(Code1, (420, 350))
        #settings.main_menu = draw_MENUBUTTON()
        settings.object_state[7]=True
    else:
        TV=Objects_Interactive(settings.TV_img,[400,325],[140,100]) #redraws the TV




def CloseLiving(): #door to the living, when clicked will open
    if settings.object_state[5]==False: #living room cabinet door closed
        doorL=Objects_Interactive(settings.living_door,[812,212],[63,304]) #left top width height
        #doorL=Objects_Interactive(settings.living_door,[300,212],[63,304])
        if doorL.check_clicked()==True:
            settings.object_state[5]=True #living room cabinet open
    else:
        exit
#================ room 3: the door ================================

class room3(Room): #room that you can escape from
    def __init__(self,image):
        super().__init__(size=(300,450),image=settings.bgYellow)
        transformBg=pygame.transform.scale(settings.bgYellow,(900,550))
        settings.screen.blit(transformBg,(0,30)) #the yellow background

        #settings.screen.blit(door_transform,(100,78)) # the door image


        objectiveText= settings.font.render("Objectives: Escape the room, Decode the message", True, 'black')
        settings.screen.blit(objectiveText, (10, 10))

    def Door(self):
        Door=Objects_Interactive(settings.door_img,[100,70],[self.size[0],self.size[1]])#img, position and size
        if Door.check_clicked() and settings.object_state[9]==True and settings.object_state[2]==True: #if door has been clicked and fingerprint is
            #in the inventory and the golden key is in the inventory
                settings.object_state[6]=True



def Scanner(): #fingerprint scanner
    scan=Objects_Interactive(settings.scan_img,[300,370],[50,50])#img, position and size
    if scan.check_clicked(): #if fingerprint scanner has been clicked and receive finger print from puzzle
        exit
def hole(): #key hole
    keyhole=Objects_Interactive(settings.keyhole_img,[260,370],[20,30])#img, position and size
    if keyhole.check_clicked(): #if fingerprint scanner has been clicked and receive finger print from puzzle
        exit
#================room 2: kitchen ================================

class room2(Room): #this is the kitchen room to the right
    def __init__(self,door_img):
        super().__init__(size=(900,530),image=settings.kitchen_img)
        kitchen_transform=pygame.transform.scale(self.image,self.size)#scales
        settings.screen.blit(kitchen_transform,(0,40)) #draws the kitchen room
        objectiveText= settings.font.render("Objectives: Unlock Padlock, Solve the image puzzle, Find secret message", True, 'black')
        settings.screen.blit(objectiveText, (10, 10))
    def Remote(self):
        if settings.object_state[3]==True: # cabinet door in kitchen open
            settings.screen.fill("light blue") #need to redraw the screen to remove previous tv remote image
            kitchen=room2(settings.kitchen_img)
            TVremote=Objects_Interactive(settings.TVremote_img,[375,115],[50,50])# it draws the tv remote once kitchen door cabinet opens
            kitchen.draw_inventory()
            #settings.main_menu = draw_MENUBUTTON()
            if TVremote.check_clicked()==True:
                settings.object_state[4]=True #object appears

#this may be redundant unsure yet
        if settings.object_state[4]==True: #if the object has been clicked
            settings.screen.fill("light blue") #need to redraw the screen to remove previous tv remote image
            kitchen=room2(settings.kitchen_img)
            kitchen.draw_inventory()
            #settings.main_menu = draw_MENUBUTTON()
        else:
            settings.slide_check=1
def QRfull():
    if settings.object_state[8]== False: #if the state is false, it is not in the inventory, from here we could also makek it not appear in room2
        QRbox=Objects_Interactive(settings.QR_img,[750,100],[50,50]) #left top width height
        settings.slide_check=4 #changes the global value slide check
        if QRbox.check_clicked(): #checking that if the area is clicked then it outputs true, this is also known as object 2
            settings.object_state[8]=True # the object has been clicked on and will disappear
            settings.slide_check=1

def CloseKitchen(): #door to the kitchen, when clicked will open
    if settings.object_state[3]==False: #kitchcen cabinet door closed
        doorK=Objects_Interactive(settings.kitchen_door,[375,115],[50,125]) #left top width height
        if doorK.check_clicked()==True:
            settings.object_state[3]=True #kitchen cabinet open

    else:
        exit

def Padlock():#padlock drawing
        padlock=Objects_Interactive(settings.padlock_img,[400,170],[30,50])
        if settings.object_state[0]==True and padlock.check_clicked(): #if user has obtained the key
            settings.object_state[3]=True #then the kitchen cabinet will open
            settings.screen.fill("light blue") #need to redraw the screen to remove previous tv padlock image
            kitchen=room2(settings.kitchen_img)
            kitchen.draw_inventory()
            #settings.main_menu = draw_MENUBUTTON()
        else:
            doorK=Objects_Interactive(settings.kitchen_door,[375,115],[50,125]) #left top width height
            padlock=Objects_Interactive(settings.padlock_img,[400,170],[30,50])# it draws the padlock unless it has been clicked and user has key

#================ Puzzles ================================

def Puzzle1(left,top,width,height):

    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN: #checks for if mouse clicked the text box to type in
            if settings.text_box.collidepoint(events.pos):
                settings.active = True #means if the box glows red
            else:
                settings.active = False#box region hasnt been clicked
        if events.type == pygame.KEYDOWN: #if any keyboard buttons have been clicked
            if settings.active: #red tex box

                if events.key == pygame.K_BACKSPACE: #deleting letters
                    settings.user_ip = settings.user_ip[:-1] #slice the string, removed the last character
                else:
                    settings.user_ip += events.unicode #allows to continue typing



    #settings.screen.fill('light blue') #refreshes the page
    InstructionRect=pygame.Rect(left,top, width, height)  #setting rectangles features
    pygame.draw.rect(settings.screen, "light gray",InstructionRect,0, 5) #drawing rectangle
    Instructions = settings.font.render("Input the secret code (all caps)", True, 'black')

    if settings.active:
        color = pygame.Color('red') #highlights the box, letting the user know to type
    else:
        color = pygame.Color('black')
    pygame.draw.rect(settings.screen,color, settings.text_box,4) #draws the box
    surf = settings.font.render(settings.user_ip,True,'black')
    settings.text_box.w = max(100, surf.get_width()+10) # this increases width of box, instead of text going out of the box area

    close = ButtonClass.Button('Close', (10, 10))
    close.draw()
    if close.check_clicked(): #sends user to different pages depending on which button was pressed
        settings.slide_check=0 #close instruction code square
        settings.object_state[1]= False

    if settings.user_ip=="SECURE": #if user types in the code correctly they will receive an item
        reward1=Objects_Interactive(settings.key_img,[950,130],[50,50])
        settings.object_state[2]=True


    inventory=Room()
    inventory.draw_inventory() #redraws the inventory

    settings.screen.blit(Instructions, (200, 100))
    settings.screen.blit(surf, (settings.text_box.x +5 , settings.text_box.y +5))

def RotateImg(rotate):
    if rotate>=270:
        rotate=0
    else:
        rotate=int(rotate+90)

    return rotate

def Puzzle2():
    settings.screen.fill('light blue') #refreshes the page
    Instructions = settings.font.render("Rotate the image using mouse", True, 'black')
    QR1=Arrow((500,100),settings.rotate1,settings.QR1_img) #position and rotation and image
    QR1.draw()
    QR2=Arrow((550,100),settings.rotate2,settings.QR2_img) #using the arrow class as it has a rotation function
    QR2.draw()
    QR3=Arrow((500,150),settings.rotate3,settings.QR3_img)
    QR3.draw()
    QR4=Arrow((550,150),settings.rotate4,settings.QR4_img)
    QR4.draw()

    closeButton = ButtonClass.Button('Close', (10, 10))
    closeButton.draw()
    if closeButton.check_clicked(): #sends user to different pages depending on which button was pressed
        settings.slide_check=4 #closes puzzle and brings back to kitchen room
        settings.object_state[8]=False

    if QR1.check():
        settings.rotate1=RotateImg(settings.rotate1)


        #settings.rotate1=settings.rotate1+90 #rotating the puzzles when clicked
    if QR2.check():
        settings.rotate2=RotateImg(settings.rotate2)

       #settings.rotate2=settings.rotate2+90

    if QR3.check():
        #settings.rotate3=settings.rotate3+90
        settings.rotate3=RotateImg(settings.rotate3)

    if QR4.check():
        #settings.rotate4=settings.rotate4+90
        settings.rotate4=RotateImg(settings.rotate4)


    inventory=Room()
    inventory.draw_inventory() #redraws the inventory
    if settings.rotate1==0 and settings.rotate2==0 and settings.rotate3==0 and settings.rotate4==0: #if the puzzle is in the correct positiong
        reward2=Objects_Interactive(settings.scan2_img,[930,220],[50,50])
        settings.object_state[9]=True

    settings.screen.blit(Instructions, (200, 100))

