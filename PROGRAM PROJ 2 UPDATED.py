#Escape game

#importing features------------------
import pygame
import os
import sys

pygame.init()

#----------importing images
living_img=pygame.image.load(r"D:\FOLDER FOR USB\SCHOOL\python - a level\pygame\images\living room.jpg")
arrow_img=pygame.image.load(r"D:\FOLDER FOR USB\SCHOOL\python - a level\pygame\images\arrow.jpg")
door_img=pygame.image.load(r"D:\FOLDER FOR USB\SCHOOL\python - a level\pygame\images\closedDoor.jpg")
kitchen_img=pygame.image.load(r"D:\FOLDER FOR USB\SCHOOL\python - a level\pygame\images\kitchen.jpg")
safe_img=pygame.image.load(r"D:\FOLDER FOR USB\SCHOOL\python - a level\pygame\images\safe.jpg")
pencil_img=pygame.image.load(r"D:\FOLDER FOR USB\SCHOOL\python - a level\pygame\images\pencil.jpg")
key_img=pygame.image.load(r"D:\FOLDER FOR USB\SCHOOL\python - a level\pygame\images\key.jpg")

#-------------initialising variables ---------------
WIDTH = 1100 #dimensions
HEIGHT = 550
fps = 60
timer = pygame.time.Clock()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('MAIN MENU')
main_menu = True
font = pygame.font.Font(None, 24)
font3= pygame.font.Font(None,50)
menu_command = 0 #which slide it is on
slide_check=0
secs=2
mins=2
object_state= [False,False,False] # potentially o3 objects and their states kinda like true or false, not or in inventory
user_ip = '' #change these variables =========================================================================3333333333333333333333333333
text_box = pygame.Rect(400,300,80,60)
active = False
color = pygame.Color('black')
codeAnswer=False


#-------classes and subroutines ------------
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


def draw_menu(): #drawing the menu and creating buttons that send user to different pages
    command = -1
    img_transform=pygame.transform.scale(living_img,(WIDTH,HEIGHT))#rotation
    screen.blit(img_transform,(0,0))
    pygame.draw.rect(screen, 'white', [50, 35, 350, 65], 0, 5) #things in backets are left,top,width,height
    pygame.draw.rect(screen, 'gray', [50, 35, 350, 65], 5, 5)
    txt = font3.render('CYBER ESCAPE', True, 'black')
    screen.blit(txt, (100, 50))
    # menu exit button
    menu = Button('Exit', (WIDTH-300, 500)) #creating the different buttons
    menu.draw()
    start_button = Button('Start', (WIDTH-300, 350))
    start_button.draw()
    button2 = Button('Button 2', (WIDTH-300, 400))
    button2.draw()
    button3 = Button('Button 3', (WIDTH-300, 450))
    button3.draw()

    if menu.check_clicked(): #sends user to different pages depending on which button was pressed
        command = 0 #exit
    if start_button.check_clicked():
        command = 1 #starts the game
    if button2.check_clicked():
        command = 2 #not yet established functionality
    if button3.check_clicked():
        command = 3
    return command


def draw_MENUBUTTON():
    menu_btn = Button('Main Menu', (WIDTH-200, 10)) #draws menu button in game, allows user to return to menu
    menu_btn.draw()
    menu = menu_btn.check_clicked()
    return menu

class Room():
    def __init__(self,size=(0,0), image="unknown"): #standard room attributes
        self.size=size #size of background
        self.image=image

    def draw_inventory(self): #inventory in each room is drawn
        pygame.draw.rect(screen, 'grey', [WIDTH-200, 80, 200, 650], 0, 5)
        pygame.draw.rect(screen, 'dark gray', [WIDTH-200, 80, 200,650], 5, 5)

        if object_state[2]==True:
            reward=Objects_Interactive(key_img,[600,100],[50,50]) # this is to true when puzzle1 has correctly been answered, shows up in invenotry
        if object_state[0]==True: #the object goes to the inventory
            pencil=Objects_Interactive(pencil_img,[740,80],[50,50]) #coords that change once area has been clicked






#============== plan here ###############-33333333333333333333333333333333333333333333333333333333333333-
#basically create an input text box for user to put paSSWORD IN
#also only unlock next room if that password is correct or unlcock key
#puzzle 1 is the text box
#puzlle 2 :
#puzzle 3/4 is finding the key




class room1(Room): #1st room
    def __init__(self,office_img):
        super().__init__(size=(900,530),image=office_img) #uses parent class
        #office_rect=office_img.get_rect()
        office_transform=pygame.transform.scale(self.image,self.size)#rotation
        screen.blit(office_transform,(0,40))
        objectiveText= font.render("Objectives: Find Key, Solve Secret Code", True, 'black')
        screen.blit(objectiveText, (10, 10))

        if object_state[0]== False: #if the state is false, it is not in the inventory, from here we could also makek it not appear in room2
            pencil=Objects_Interactive(pencil_img,[60,60],[50,50]) #left top width height
            if pencil.check_clicked(): #checking that if the area is clicked then it outputs true, this is also known as object 1
                pencil=Objects_Interactive(pencil_img,[740,80],[50,50]) #coords that change once area has been clicked
                object_state[0]=True #the object goes to the inventory

        else:
            pencil=Objects_Interactive(pencil_img,[740,80],[50,50]) # should not disappear

        if object_state[1]== False: #if the state is false, it is not in the inventory, from here we could also makek it not appear in room2
            safe=Objects_Interactive(safe_img,[550,100],[50,50]) #left top width height
            if safe.check_clicked(): #checking that if the area is clicked then it outputs true, this is also known as object 2
                object_state[1]=True # the object has been clicked on and will disappear
        else:
            global slide_check
            slide_check=3




class room3(Room): #room that you can escape from
    def __init__(self,door_img):
        super().__init__(size=(741,650),image=door_img)
        door_rect=door_img.get_rect()
        door_transform=pygame.transform.scale(self.image,self.size)
        screen.blit(door_transform,(door_rect))
        objectiveText= font.render("Objectives: Escape the room", True, 'black')
        screen.blit(objectiveText, (10, 10))

class room2(Room): #this is the kitchen room to the right
    def __init__(self,door_img):
        super().__init__(size=(900,530),image=kitchen_img)
        kitchen_transform=pygame.transform.scale(self.image,self.size)#rotation
        screen.blit(kitchen_transform,(0,40))
        objectiveText= font.render("Objectives: Find Key, Solve Secret Code", True, 'black')
        screen.blit(objectiveText, (10, 10))

class Arrow(): #the arrow button
    def __init__(self,pos,rotate):
        self.pos=pos
        self.rotate=rotate
        self.arrow= pygame.rect.Rect((self.pos[0], self.pos[1]), (50, 50))



    def draw(self): #draw an arrow
        global arrow_img #brings the img of arrow
        img=arrow_img
         #creates a rectangle of img

        img=pygame.transform.rotate(img,self.rotate) #rotates it
        arrow_transform=pygame.transform.scale(img,(50,50)) #scales image

        screen.blit(arrow_transform,(self.pos[0],self.pos[1])) #the self is the coords, but by using rect it takes top left corner i think and thats what the coords are


    def check(self):
        if self.arrow.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

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



    def state_object():
        #if coords are here for particular object idk do somehti

#class Object1(Objects_Interactive):
 #   def __init__(self):
        exit #add my own prolly image)
        #super().__init__(Left=180,Top=50,Width=50,Height=50) #overwrites superclass
        #if Square.check.clicked==True:
# maybe try to somehow create a state of the object

def Puzzle1(left,top,width,height): #made it into a class but unsure
    #def __init__(self,left, top, width, height):
    global active
    global user_ip
    global slide_check #needs to take the global variables and change them, in order to retain the change globally



    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN: #checks for if mouse clicked the text box to type in
            if text_box.collidepoint(events.pos):
                active = True #means if the box glows red
            else:
                active = False#box region hasnt been clicked
        if events.type == pygame.KEYDOWN: #if any keyboard buttons have been clicked
            if active: #red tex box

                if events.key == pygame.K_BACKSPACE: #deleting letters
                    user_ip = user_ip[:-1] #slice the string, removed the last character
                else:
                    user_ip += events.unicode #allows to continue typing
        #if user_ip == str(876):
          #  exit

            #need to render a correct screen---------------
            #also display text like dont leave your code in the open


    screen.fill('light blue') #refreshes the page
    InstructionRect=pygame.Rect(left,top, width, height)  #setting rectangles features
    pygame.draw.rect(screen, "light gray",InstructionRect,0, 5) #drawing rectangle
    Instructions = font.render("Input the secret code", True, 'black')

    if active:
        color = pygame.Color('red') #highlights the box, letting the user know to type
    else:
        color = pygame.Color('black')
    pygame.draw.rect(screen,color, text_box,4) #draws the box
    surf = font.render(user_ip,True,'black')
    text_box.w = max(100, surf.get_width()+10) # this increases width of box, instead of text going out of the box area

    close = Button('Close', (10, 10))
    close.draw()
    if close.check_clicked(): #sends user to different pages depending on which button was pressed
        slide_check=0 #close instruction code square
        object_state[1]= False

    if user_ip=="hello": #if user types in the code correctly they will receive an item
        reward1=Objects_Interactive(key_img,[740,80],[50,50])
        object_state[2]=True



    inventory=Room()
    inventory.draw_inventory()

    screen.blit(Instructions, (200, 100))
    screen.blit(surf, (text_box.x +5 , text_box.y +5))

        #make text box in invenotry active



#-------------main game---------------
run = True
while run:
    screen.fill('light blue')
    timer.tick(fps)

    if main_menu:
        menu_command = draw_menu() #condition that the menu is being drawn
        if menu_command != -1:
            main_menu = False

        if menu_command ==0: #closes MENUUUU, user clicked 0
            run=False

    else:
        main_menu = draw_MENUBUTTON() #draws the 1st room,
        #it has to be called main_menu in order to draw and allow user to click main menu button

        if menu_command==1: #this checks the if its in game state or menu
            if slide_check==0: #this checks the state of which room the game is e.g room 1 or room2

                living_room=room1(living_img) #checks which arrow was clicked, this sends user to room 1, this is the living room
                living_room.draw_inventory() #draws inventory

                left=Arrow((0,100),270) #draws left and right arrows
                left.draw()
                right=Arrow((690,100),90)
                right.draw()

                if left.check(): # this sends user to room 3, the room that allows you to escape
                    slide_check=2 #its called room 3 as there previously was a room2, it was removed

                if right.check():
                    slide_check=4

            if slide_check==2: # if this isnt included the door image flashes and disappears, also draws the next room
                door=room3(door_img)
                door.draw_inventory()
                right=Arrow((690,400),90)
                right.draw()

                if right.check():
                    slide_check=0

            if slide_check==4: #this is the kitchen
                kitchen=room2(kitchen_img) #checks which arrow was clicked, this sends user to room 1, this is the living room
                kitchen.draw_inventory()
                left=Arrow((0,100),270) #draws left arrow
                left.draw()

                if left.check(): # this sends user to living room
                    slide_check=0

            if slide_check==3: #this will be the puzzle on the computer
                PuzzleOne=Puzzle1(100,100,400,400)




            #if LEFT2.check(): #brings user back to original room
            #    slide_check=0

    #countdown initiated
    #text=pygame.font.SysFont("Arial",32).render("{}:{}".format(mins,secs), True,(255,255,255),(0,0,0))
    #text_rect=text.get_rect()
    #screen.blit(text,text_rect)

    #while not(mins==0 and secs==0): #needed a stopping cause else program produces error
    #    secs=secs-1 #the actual countdown
    #    if secs==0:
    #        secs=60
    #        mins=mins-1
    #    text=pygame.font.SysFont("Arial",32).render("{}:{}".format(mins,secs), True,(255,255,255),(0,0,0))
    #    text_rect=text.get_rect()
    #    screen.blit(text,text_rect)
    #    pygame.time.delay(300) #slow down the timer
    #    pygame.display.update()
    #else:
    #    print("Stop")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()