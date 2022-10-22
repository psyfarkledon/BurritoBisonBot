from pydoc import cli
from time import sleep
from pyautogui import *
from Coordinate import Coordinate

class Screen():
    def __init__(self, picture):

        #Loops until it finds the screen it looks for
        find_screen = None
        while find_screen == None:
            print("Looking for screen")
            find_screen = locateOnScreen(f"assets/{picture}.png", grayscale=True, confidence=0.5)

        self.whichLauncher = "burrito"

        self.width = find_screen[2]
        self.height = find_screen[3]

        #CORNER COORDINATES
        self.top_left = Coordinate(find_screen[0],find_screen[1])
        self.top_right = Coordinate(self.top_left.x+self.width, self.top_left.y)
        self.bottom_left = Coordinate(self.top_left.x, self.top_left.y+self.height)
        self.bottom_right = Coordinate(self.top_left.x+self.width, self.top_left.y+self.height)

        #SHOP COORDINATES
        self.pay_btn = Coordinate(int(self.top_left.x + (self.width*0.63)), int(self.top_left.y + (self.height* 0.64)))
        self.shop_play_btn = Coordinate(int(self.bottom_right.x - (self.width * 0.095)), int(self.bottom_right.y - (self.height * 0.134)))

        self.pinata_cards_columns = [
            int(self.top_left.x + (self.width * 0.20)),
            int(self.top_left.x + (self.width * 0.28)),
            int(self.top_left.x + (self.width * 0.36)),
            int(self.top_left.x + (self.width * 0.44))
        ]

        self.pinata_cards_rows = [
            int(self.top_left.y + (self.height * 0.27)),
            int(self.top_left.y + (self.height * 0.46)),
            int(self.top_left.y + (self.height * 0.65)),
            int(self.top_left.y + (self.height * 0.84)),
        ]

        self.bison_upgrades = Coordinate(int(self.top_left.x + (self.width * 0.10)), self.pinata_cards_rows[0])
        self.gummy_upgrades = Coordinate(int(self.top_left.x + (self.width * 0.10)), self.pinata_cards_rows[1])
        self.boss_upgrades = Coordinate(int(self.top_left.x + (self.width * 0.10)), self.pinata_cards_rows[2])
        
        self.gummy_upgrade_coordinates = [
            Coordinate(self.pinata_cards_columns[2], self.pinata_cards_rows[0]),
            Coordinate(self.pinata_cards_columns[0], self.pinata_cards_rows[1]),
            Coordinate(self.pinata_cards_columns[1], self.pinata_cards_rows[1]),
            Coordinate(self.pinata_cards_columns[2], self.pinata_cards_rows[1]),
            Coordinate(self.pinata_cards_columns[3], self.pinata_cards_rows[1]),
            Coordinate(self.pinata_cards_columns[0], self.pinata_cards_rows[2]),
            Coordinate(self.pinata_cards_columns[1], self.pinata_cards_rows[2]),
        ]

        self.pinata = Coordinate(self.top_left.x + (self.width * 0.58), self.top_left.y + (self.height * 0.87))
        self.pinata_xbtn = Coordinate(self.top_left.x + (self.width * 0.44), self.top_left.y + (self.height * 0.89))
        
        #LAUNCH COORDINATES

        #Drag from point start to point end and release to launch
        self.drag_point_start = Coordinate(int(self.top_left.x + (self.width * 0.28)), int(self.top_left.y + (self.height * 0.80)))
        self.drag_point_end = Coordinate(int(self.top_left.x + (self.width * 0.05)), int(self.top_left.y + (self.height * 0.80)))

        #Will move across the screen by a percentage of the screen each cycle.
        self.click_increment = int(self.width*0.10)
        self.click_increment_y = int((self.height*0.65) + self.top_left.y)

        print("Screen Configured Properly")

    #when game is opened for the first time this gets you to your first launch
    def new_game(self):
        for i in range(4):
            click(button="left")
            sleep(0.25)

    #checks if the game needs to be stopped based on mouse position
    def stop_game(self):
        if position()[0] < self.top_left.x or position()[0] > self.bottom_right.x or position()[1] < self.top_left.y or position()[1] > self.bottom_right.y:
            return True

    #every 3rd run this will look for a play button
    def end_of_run(self, i):
        if i == 3:
            if locateOnScreen(f"assets/play_btn.png", grayscale=True, confidence=0.5) != None:
                return True
        else:
            return False

    #figures out which launcher 
    def find_launcher(self):
        while True:
            if locateOnScreen(f"assets/bison_launch.png", grayscale=True, confidence=0.5) != None:
                print("Launcher is Bison")
                self.whichLauncher = "bison"
                return "bison"
            elif locateOnScreen(f"assets/pineapple_launch.png", grayscale=True, confidence=0.5) != None:
                print("Launcher is Pineapple Girl")
                self.whichLauncher = "pineapple"
                return "pineapple"
            elif locateOnScreen(f"assets/bird_launch.png", grayscale=True, confidence=0.5) != None:
                print("Launcher is Bird Man")
                self.whichLauncher = "bird"
                return "bird"
            else:
                print("Can't find launcher")

    #Determines launcher and launches character
    def launch(self):
        launcher = self.find_launcher()
        moveTo(self.drag_point_start.x, self.drag_point_start.y) 
        dragTo(self.drag_point_end.x, self.drag_point_end.y, 0.5, button='left')
        return launcher

    #Cycles through upgrades and buys anything it can afford    
    def shop(self):

        #Bison Upgrades
        moveTo(self.bison_upgrades.x, self.bison_upgrades.y)
        click(button="left")
        sleep(0.5)

        #loops through upgrades
        for y in self.pinata_cards_rows:
            for x in self.pinata_cards_columns:
                moveTo(x,y)
                click(button="left")
                sleep(0.5)
                moveTo(self.pay_btn.x, self.pay_btn.y)
                click(button="left")
                sleep(0.5)

        # #Gummy Bear upgrades
        moveTo(self.gummy_upgrades.x, self.gummy_upgrades.y) #Move to the gummy bear card and clicks
        click(button="left")
        sleep(0.5)

        for coor in self.gummy_upgrade_coordinates:
            moveTo(coor.x,coor.y)
            click(button="left")
            sleep(0.5)
            moveTo(self.pay_btn.x, self.pay_btn.y)
            click(button="left")
            sleep(0.5)

        #Boss upgrades
        moveTo(self.boss_upgrades.x, self.boss_upgrades.y) #moves to boss card and clicks
        click(button="left")
        sleep(0.5)

        #Only purchase upgrade for gumball
        #TODO
        for i in range(2):
            moveTo(self.pinata_cards_columns[i], self.pinata_cards_rows[0])
            click(button="left")
            sleep(0.5)
            moveTo(self.pay_btn.x, self.pay_btn.y)
            click(button="left")
            sleep(0.5)

        #Collect Pinata
        moveTo(self.pinata.x, self.pinata.y)
        click(button="left")
        sleep(2)
        moveTo(self.pinata_xbtn.x, self.pinata_xbtn.y)
        sleep(3)
        click(button="left")

        for i in range(15):
            click(button="left")
            sleep(0.25)
        sleep(2)

        for i in range(9):
            moveTo(self.top_left.x + ((i+1) * self.click_increment), self.click_increment_y)
            click(button="left")
            sleep(0.5)

        sleep(3)
        click(button="left")

        moveTo(self.shop_play_btn.x, self.shop_play_btn.y)
        click(button="left")



    def refresh_page(self):
        x = None
        while x == None:
            x = locateOnScreen(f"assets/refresh_btn.png", grayscale=True, confidence=0.8)
        
        moveTo(x[0], x[1])
        click(button="left")