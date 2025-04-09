#Escape game

#importing features------------------
import pygame
import os
import sys
from ButtonClass import Button
from RoomClass import *#Room, room1,room2,room3
import settings
from ArrowClass import Arrow
from instructionScreen import *

pygame.init()


#-------classes and subroutines ------------



def draw_menu(): #drawing the menu and creating buttons that send user to different pages
    command = -1
    img_transform=pygame.transform.scale(settings.living_img,(settings.WIDTH,settings.HEIGHT))#rotation
    settings.screen.blit(img_transform,(0,0))
    #pygame.draw.rect(settings.screen, 'white', [50, 35, 350, 65], 0, 5) #things in backets are left,top,width,height
    #pygame.draw.rect(settings.screen, 'gray', [50, 35, 350, 65], 5, 5)
    txt = settings.cc_font.render('ESCAPE ROOM', True, 'black')
    settings.screen.blit(txt, (100, 50))
    # menu exit button
    Exit = Button('Exit', (settings.WIDTH-1050, 500)) #creating the different buttons
    Exit.draw()
    instruction_button = Button('Instructions', (settings.WIDTH-1050, 450))
    instruction_button.draw()
    start_button = Button('Start', (settings.WIDTH-1050, 400))
    start_button.draw()


    if Exit.check_clicked(): #sends user to different pages depending on which button was pressed
        command = 0 #exit
    if start_button.check_clicked():
        command = 1 #starts the game
    if instruction_button.check_clicked():
        command = 2 #starts the game
    return command


def draw_pause(): #drawing the menu and creating buttons that send user to different pages
    command = -2
    settings.screen.fill('light blue')
    #pygame.draw.rect(settings.screen, 'white', [50, 35, 350, 65], 0, 5) #things in backets are left,top,width,height
    #pygame.draw.rect(settings.screen, 'gray', [50, 35, 350, 65], 5, 5)
    txt = settings.cc_font.render('Pause Menu', True, 'black')
    settings.screen.blit(txt, (100, 50))
    # menu exit button
    Exit2 = Button('Exit Game', (settings.WIDTH-500, 500)) #creating the different buttons
    Exit2.draw()
    OpenScreen_btn = Button('Back to Opening Screen', (settings.WIDTH-500, 450))
    OpenScreen_btn.draw()
    start_button = Button('Back to Game', (settings.WIDTH-500, 400))
    start_button.draw()


    if Exit2.check_clicked(): #sends user to different pages depending on which button was pressed
        command = 0 #exit
    if start_button.check_clicked():
        command = 3 #starts the game
    if OpenScreen_btn.check_clicked():
        command = 2 #brings user back to opening screen
    return command



def instruction_page():
    command=2
    txt = settings.cc_font.render('Instruction', True, 'black')
    txt2 = settings.font.render('Aim of the game is to escape the room using Left Mouse Button to interact with the room', True, 'black')
    txt3 = settings.font.render('Some puzzles may require you to type in answers using keyboard', True, 'black')
    txt4 = settings.font.render('Each room has an objective pertaining to that room for you to complete', True, 'black')
    txt5 = settings.font.render('If you want to pause the game at any point, press the space bar', True, 'black')
    settings.screen.blit(txt, (100, 50))
    settings.screen.blit(txt2, (100, 100))
    settings.screen.blit(txt3, (100, 200))
    settings.screen.blit(txt4, (100, 300))
    settings.screen.blit(txt5, (100, 400))
    OpenScreen_btn = Button('Back to Opening Screen', (settings.WIDTH-500, 450))
    OpenScreen_btn.draw()

    if OpenScreen_btn.check_clicked():
        command = 1 #brings user back to opening screen
    return command

# USEREVENTS are just integers
# you can only have like 31 of them or something arbitrarily low
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 1000)    # sets timer with USEREVENT and delay in milliseconds
timer_font = pygame.font.Font(None, 38)
timer_sec = 60
timer_text = timer_font.render("02:00", True, (0, 0, 0))

game_paused=False


#-------------main game---------------
run = True

class main(run):
    while run:

        settings.screen.fill('light blue')
        settings.timer.tick(settings.fps)

        if settings.main_menu: #true or false
            settings.menu_command = draw_menu() #condition that the opening screen is being drawn
            if settings.menu_command != -1:
                settings.main_menu = False #condition menu is not being drawn

            if settings.menu_command ==0: #closes MENUUUU, user clicked 0
                run=False


        else:


            if game_paused==False and settings.menu_command==1: #this checks the if its in game state or menu

                if settings.slide_check==0: #this checks the state of which room the game is e.g room 1 or room2
                    living_room=room1(settings.living_img) #checks which arrow was clicked, this sends user to room 1, this is the living room
                    living_room.draw_inventory() #draws inventory
                    living_room.Safe()


                    left=Arrow((0,100),180,settings.arrow_img) #draws left and right arrows
                    left.draw()
                    right=Arrow((850,100),0,settings.arrow_img)
                    right.draw()

                    if settings.object_state[5]==True: #draws the key once cupboard in living room is open
                        KeyBlue()

                    ClosedLiving=CloseLiving()
                    TVdraw()

                    pygame.display.flip
                    if left.check(): # this sends user to room 3, the room that allows you to escape
                        settings.slide_check=2 #its called room 3 as there previously was a room2, it was removed, this is where the escape door is

                    if right.check():
                        settings.slide_check=4 # this is where the kitchen is

                    if settings.object_state[7]==True:
                        Code1= settings.font.render("OAY___", True, 'white') #displays the code to safe
                        settings.screen.blit(Code1, (420, 350))
                        #settings.main_menu = draw_PAUSEBUTTON()


                if settings.slide_check==2: # if this isnt included the door image flashes and disappears, also draws the next room
                    bg=room3(settings.bgYellow)
                    bg.draw_inventory()
                    bg.Door()

                    poster=pygame.transform.rotate(settings.poster_img,345) #rotates it

                    poster_transform=pygame.transform.scale(poster,(140,150)) #scales the image of the poster
                    cipher_transform=pygame.transform.scale(settings.cipher_img,(200,200)) #scales the image of the cipher


                    settings.screen.blit(poster_transform,(700,300))
                    settings.screen.blit(cipher_transform,(550,120))


                    right=Arrow((850,150),0,settings.arrow_img)
                    right.draw()
                    Scanner()
                    hole()

                    if right.check():
                        settings.slide_check=0

                if settings.slide_check==4: #this is the kitchen
                    kitchen=room2(settings.kitchen_img) #checks which arrow was clicked, this sends user to the kitchen
                    Padlock()
                    kitchen.draw_inventory()
                    kitchen.Remote()
                    left=Arrow((0,150),180,settings.arrow_img) #draws left arrow
                    left.draw()
                    QRcode=QRfull()
                    frame_transform=pygame.transform.scale(settings.frame_img,(90,60)) #scales the image of the cipher
                    CodeText= settings.font.render("___QNA", True, 'black')

                    settings.screen.blit(frame_transform,(500,308))
                    settings.screen.blit(CodeText, (515, 345))
                    if left.check(): # this sends user to living room
                        settings.slide_check=0

                if settings.slide_check==3: #this will be the safe puzzle
                    PuzzleOne=Puzzle1(100,100,400,400)

                if settings.object_state[6]==True:
                    settings.screen.fill("light blue")
                    winText= settings.font.render("YOU WIN", True, 'black')
                    settings.screen.blit(winText, (100, 100))

                if settings.slide_check==1: #this is puzzle 2
                    PuzzleTwo=Puzzle2()


                if settings.slide_check==5:
                    settings.screen.fill("light blue")
                    loseText= settings.font.render("YOU LOSE, better luck next time", True, 'black')
                    settings.screen.blit(loseText, (100, 100))

            if settings.menu_command==2: # this includes the instructions
                instruction_command=instruction_page()
                if instruction_command!=2:
                    settings.main_menu=True




            if game_paused==True:

                settings.pause_command=draw_pause()
                if settings.pause_command != -2: #stops drawing the pause screen
                    settings.pause_menu=False

                if settings.pause_command ==0: #this kills the game
                    run = False

                if settings.pause_command==2:
                    settings.main_menu=True #brings user back to opening screen
                    game_paused=False

                if settings.pause_command==3: #takes user into game state
                    game_paused=False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == timer and settings.menu_command==1:    # checks for timer event
                if timer_sec > 0:
                    timer_sec =timer_sec-1
                    timer_text = timer_font.render("00:%02d" % timer_sec, True, (0, 0, 0))
                if timer_sec==0:
                    settings.slide_check=5
                    exit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
                    settings.screen.blit(timer_text,(300,20))




        pygame.display.flip()
    pygame.quit()