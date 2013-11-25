import sys  # Only needed for argv[], can be removed later
import threading
#import Queue
from player_input_handler import PlayerInputHandler
from game_controller import GameController


# display_points is only for the console, won't be used on web server
def display_points(win_status):

    print "\nYou won: "
    if win_status[1] == 1: print "Row 1 \t"
    if win_status[2] == 1: print "Row 2 \t"
    if win_status[3] == 1: print "Row 3 \t"
    if win_status[4] == 1: print "Full House"
    
    print "Your total points are <to be done: fetch from database>"
    # win_status would be sent to the client instead of this function


if __name__ == '__main__':

    try:
        _delay = float(sys.argv[1])
    except IndexError:
        print "\nStarting with default delay of 500 milliseconds"
        _delay = 0.5


    # Login Sequence
    # TODO Check Switch Case
    logged_in = False
    while logged_in == False:
        print "\n1. Login \n2. SignUp"
        choice = raw_input()

        if (choice == '1'):
            print "Enter username:"
            username = raw_input()
            print "(Login verification to be added.)\n"
            #if User exists in DB, login or pop msg.            
            logged_in = True

        elif (choice == '2'):
            print "Sign Up facility to be added."
            continue
        else:
            print "Wrong Input."  # can put try/except with loop instead
            continue

    print "While playing the game:\nto cross a number that's available \
on your ticket - press 0, \nto claim: Row 1 press 1, Row 2 - press 2, \
Row 3 - press 3, Full House - press 4.\n"
    print "Press any key when ready."
    raw_input()

    # The game is played inside the following loop 
    while True:
        print '\n1. Play Game\n2. Claim Gift\n3. Exit'
        choice = raw_input()

        if (choice == '1'):
            pass
        elif (choice == '2'):
            print "Claim functionality not supported yet"
            continue
        elif (choice == '3'):
            break
        else:
            print "Wrong Input"  # can put try/except with loop instead
            continue

        # TODO Use with to control context

        game_id = 24  # TODO This has to be generated and used in DB
        game_session = GameController(game_id, _delay) # STARTS new thread
        #print "#####", game_session

        player_handler = PlayerInputHandler(game_session)
        player_handler_thread = threading.Thread(target=player_handler.worker_thread)
        player_handler_thread.start()

        #print "+++++", player_handler_thread

        print "Starting Game\n"
        game_session.start()

        while (game_session.is_game_over() == False):
            #time.sleep(5) # Debug code
            # if tkt_claimed from KB, call GamController.keyPress
            key = raw_input()

            if (game_session.is_game_over() == False):
                player_handler.input_handler(key)


        # Current Game Over

        win_status = player_handler.get_points()
        #print win_status

        # Update DB with total points
        #point_status = fetch points from db and send to Client/Display function

        # display() only used for current console code, remove in web server
        display_points(win_status)

        game_session.join()
        player_handler_thread.join()


    print "Exiting Daemon."

