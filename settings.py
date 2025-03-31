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

#def init():

import pygame
import os
import sys

pygame.init()

#-------------initialising variables ---------------
#----global variables -----

#CONSTANTS
WIDTH = 1100 #dimensions
HEIGHT = 550
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('MAIN MENU')
main_menu = True
font = pygame.font.Font(None, 24)
font3= pygame.font.Font(None,50)
secs=2
mins=2
color = pygame.Color('black')
text_box = pygame.Rect(400,300,80,60)
pause_menu= True #false means the pause menu is not being displayed
cc_font= pygame.font.Font( "Blaec-Regular.ttf",40)

#--------- non constants --------
#objects and their states
object_state= [False,False,False,False,False,False,False,False,False,False] # [0] = false means the blue key is not in invetnory, [1] = true it loads up puzzle 1, [2] true is the key to the puzzle shows up in inventory, [3] false is door in kitchen is closed
#[4] false means tv remote doesnt not appear, [5] false is the door in the living room is closed, [6] is the you win screen, [7] true means TV text appears
#[8] if state is False the QR code is drawn else puzzle two appears, [9] keeps the finger scan in inventory

#--- non constant
user_ip = '' #change these variables names =================
active = False
codeAnswer=False
menu_command = 0 #0 means menu is being drawn else its in game state
pause_command=-1
slide_check=0 #which room/puzzle is being drawn
rotate1=90 #when square is clicked the puzzle will rotate
rotate2=270
rotate3=180
rotate4=270

#==========images=============
KeyBlue_img=pygame.image.load(os.path.join("images", "key3.png")).convert_alpha()
KeyYellow_img = pygame.image.load(os.path.join("images", "key2.png")).convert_alpha()
safe_img = pygame.image.load(os.path.join("images", "safe2.png")).convert_alpha()
living_img = pygame.image.load(os.path.join("images", "living room open.jpg")).convert_alpha()
living_door = pygame.image.load(os.path.join("images", "doorLivingRoom.jpg")).convert_alpha()
arrow_img = pygame.image.load(os.path.join("images", "arrow2.png")).convert_alpha()
door_img = pygame.image.load(os.path.join("images", "doorNew.png")).convert_alpha()
kitchen_img = pygame.image.load(os.path.join("images", "kitchen open.jpg")).convert()
kitchen_door = pygame.image.load(os.path.join("images", "doorToKitchen.jpg")).convert()
key_img = pygame.image.load(os.path.join("images", "key2.png")).convert_alpha()
tvremote_img = pygame.image.load(os.path.join("images", "tvremote.png")).convert_alpha()
bgYellow_img = pygame.image.load(os.path.join("images", "backgroundYellow.jpg")).convert_alpha()
padlock_img = pygame.image.load(os.path.join("images", "padlock.png")).convert_alpha()

TV_img = pygame.image.load(os.path.join("images", "TV.png")).convert_alpha()
scan_img = pygame.image.load(os.path.join("images", "fingerprint scan4.png")).convert_alpha()
scan2_img = pygame.image.load(os.path.join("images", "fingerprint scan3.png")).convert_alpha()
keyhole_img = pygame.image.load(os.path.join("images", "keyhole.png")).convert_alpha()
cipher_img = pygame.image.load(os.path.join("images", "cipher.png")).convert_alpha()
poster_img = pygame.image.load(os.path.join("images", "poster.png")).convert_alpha()
frame_img = pygame.image.load(os.path.join("images", "frame2.png")).convert_alpha()

QR_img = pygame.image.load(os.path.join("images", "puzzle2.png")).convert_alpha()
QR1_img = pygame.image.load(os.path.join("images", "part1.png")).convert_alpha()
QR2_img = pygame.image.load(os.path.join("images", "part3.png")).convert_alpha()
QR3_img = pygame.image.load(os.path.join("images", "part2.png")).convert_alpha()
QR4_img = pygame.image.load(os.path.join("images", "part4.png")).convert_alpha()
# image 1-4, top left to bottom right
#==============

