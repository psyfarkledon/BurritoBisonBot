from Screen import Screen
from time import sleep
from pyautogui import *

run = True


while run:
    refresh = False

    #Screen Class that configures the screen. It preloads a lot of data and does many calculations to save time while looping
    screen = Screen("screen_2")
    #Moves to play button and clicks
    moveTo(screen.shop_play_btn.x, screen.shop_play_btn.y)
    click(button="left")    

    #It takes a few seconds for the screen to load up
    sleep(3)

    #checks if this is the first time the game has been loaded up
    if locateOnScreen(f"assets/new_game.png", grayscale=True, confidence=0.5) != None:
            screen.new_game()
            sleep(2)
    else:
        moveTo(screen.shop_play_btn.x, screen.shop_play_btn.y)
        click(button="left")
        sleep(2)


    #After so many runs the browser needs to refresh. the game freezes if it's been running to long
    run_counter = 0

    #Loops for every run
    while not refresh:
        current_launcher = screen.launch() 
        click_counter = 0 #used to index array with many coordinates to click in many places on screen
        check_for_play_btn = 0 #number of times game has checked for play btn and has returned false
        click_frequency = 1 #How fast the screen is clicked
        end_run = False #boolean is true if it's the end of the run

        refresh_counter = 1

        #Loops until run is over
        while not end_run:
            #moves to a new part of the screen and clicks
            moveTo(screen.top_left.x + (screen.click_increment * refresh_counter), screen.click_increment_y)
            click(button="left")
            click_counter += 1
            
            #Checks if it's time to check for the play button
            if screen.end_of_run(check_for_play_btn):
                
                end_run = True #if play btn is found it means it's time to end the loop

                #every 3rd run bot goes to shop
                if run_counter == 3:
                    #reset the counter
                    run_counter = 0
                    x = locateOnScreen(f"assets/shop_icon.png", grayscale=True, confidence=0.5)
                    moveTo(x[0], x[1])
                    click(button="left")
                    sleep(3)
                    screen.shop()
                    sleep(2)
                    screen.launch()
                #else press the play button for the next run
                else:
                    run_counter += 1
                    x = locateOnScreen(f"assets/play_btn.png", grayscale=True, confidence=0.5)
                    moveTo(x[0], x[1])
                    sleep(2)
                    click(button="left")
                    sleep(3)
                    screen.launch()
                
            sleep(click_frequency)

            #if mouse is outside desired area the bot will stop
            if screen.stop_game():
                end_run = True
                refresh = True
                run = False

            #checks if level has gone on for more than 200 clicks. if it has it refreshes the page
            refresh_counter = 1 if refresh_counter == 8 else refresh_counter + 1
            #check for play button manager
            check_for_play_btn = 0 if check_for_play_btn == 3 else check_for_play_btn + 1

            if refresh_counter == 200:
                refresh = True
                screen.refresh_page()
                sleep(20)
                



        

        

        


