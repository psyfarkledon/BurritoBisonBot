from pydoc import cli
from time import sleep
from pyautogui import *

#Class for handling coordinates
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y



        
        




#Figures out who the launcher is
def launcher():
    while True:
        if locateOnScreen(f"assets/bison_launch.png", grayscale=True, confidence=0.5) != None:
            print("bison")
            return "bison"
        elif locateOnScreen(f"assets/pineapple_launch.png", grayscale=True, confidence=0.5) != None:
            print("Pianeapple")
            return "pineapple"
        elif locateOnScreen(f"assets/bird_launch.png", grayscale=True, confidence=0.5) != None:
            print("bird")
            return "bird"
        else:
            print("Not yet")

#figures out which boss
def launch(a,b):
    moveTo(a.x, a.y) 

    dragTo(b.x, b.y, 0.5, button='left')


def shop(Xs, Ys, upgradesX, pay_btn ):

    #in miliseconds
    time_between_purchases = 500
    time_between_purchases /= 1000

    #Buys any bison upgrades it can afford
    moveTo(upgradesX, Ys[0])
    click(button="left")
    for x in Xs:
        for y in Ys:
            moveTo(x, y)
            sleep(time_between_purchases)
            click(button="left")
            click(button="left")
            sleep(time_between_purchases)
            click(button="left")
            click(button="left")
            moveTo(pay_btn[0], pay_btn[1])
            click(button="left")
            click(button="left")
            sleep(time_between_purchases)
            click(button="left")
            click(button="left")
            sleep(time_between_purchases)
            click(button="left")
            click(button="left")

    #Gummy Upgrades
    moveTo(upgradesX, Ys[1])
    sleep(time_between_purchases)
    click(button="left")
    sleep(time_between_purchases)
    for upgrade in [[2,0], [0,1], [2,1], [3,1], [0,2], [1,2]]:
        sleep(time_between_purchases)
        moveTo(Xs[upgrade[0]], Ys[upgrade[1]])
        click(button="left")
        sleep(time_between_purchases)
        moveTo(pay_btn[0], pay_btn[1])
        click(button="left")
        sleep(time_between_purchases)
    
    #Boss Upgrades
    moveTo(upgradesX, Ys[2])
    click(button="left")
    
    sleep(time_between_purchases)
    moveTo(Xs[0], Ys[0])
    sleep(time_between_purchases)
    click(button="left")
    sleep(time_between_purchases)
    moveTo(pay_btn[0], pay_btn[1])
    click(button="left")
    sleep(time_between_purchases)

    sleep(time_between_purchases)
    moveTo(Xs[1], Ys[0])
    click(button="left")
    sleep(time_between_purchases)
    moveTo(pay_btn[0], pay_btn[1])
    click(button="left")
    sleep(time_between_purchases)


    
    

    #PINATA IGNORE FOR NOW
    # x = shop_btn = locateOnScreen(f"assets/pinata.png", grayscale=True, confidence=0.6)
    # if shop_btn != None:
    #     sleep(2)
    #     moveTo(shop_btn[0], shop_btn[1])
    #     click(button="left")
    # x = None
    # while x == None:
    #     x = shop_btn = locateOnScreen(f"assets/pinata.png", grayscale=True, confidence=0.6)

    # sleep(2)
    # moveTo(shop_btn[0], shop_btn[1])
    # click(button="left")

    # for i in range(9):
    #     click(button="left")
    #     sleep(0.5)

    # sleep(5)

    # for i in pinata_x:
    #     moveTo(i,pinata_y)
    #     click(button="left")
    #     sleep(1)
    # sleep(1)
    # click(button="left")

#when the shop is entered it tries to buy everything
# def shop():

#     workX = top_left.x
#     workY = top_left.y

#     workX += width*initial_move_right
#     workY += height*initial_move_down
#     moveTo(workX,workY)
#     sleep(1)

#     for i in range(4):
#         for i in range(4):
#             workX += upgrade_to_upgrade_right*width
#             moveTo(workX,workY)
#             sleep(1)
#         workY += upgrade_to_upgrade_down*height
#         workX = top_left.x + (initial_move_right*width)