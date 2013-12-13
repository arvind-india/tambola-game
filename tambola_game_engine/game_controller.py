#
# Tambola / Housie Mobile Game
#

__author__ = 'nitin'

import threading
#import Queue
import time
from os import sys
from random import randint


# This class starts a thread, so that more than one game can be run at a time.
# If number of games begins to cross 100, we'll have to redesign this so that 
# a pool of threads handle the tasks instead.
class GameController(threading.Thread):

    def __init__(self, game_id, seconds): 
        threading.Thread.__init__(self)

        self._game_id = game_id
        self._game_over_status = False

        # 0 = Full House, 1 = Row1, 2 = Row2, 3 = Row3
        # Using ints to avoid 'string' operations
        self._claim_status = {0:0, 1:0, 2:0, 3:0, 4:0}

        self._delay = seconds

    def run(self):
        number_pool = range(1,100)

        for i in range(0,100):
            time.sleep(self._delay)
            count_left = len(number_pool)

            if (self._claim_status[4] != 0):
                print "Full House claimed. Game Over."
                self._game_over_status = True
                break

            if (count_left):
                try:
                    next_num = number_pool.pop(randint(0,count_left-1))
                    sys.stdout.write((str(next_num) + ' '))
                except:
                    print "Popping empty list", sys.exc_info()[0]

            else:
                print("\nNumber pool finished.")
                self._game_over_status = True

    #def __del__():
    #    self.join()
    #def thread_cleanup():
    #    self.join()


    def claim(self, claim_code, player_id):
        if (self._claim_status[claim_code] == 0):
            self._claim_status[claim_code] = player_id
            return 0
        else:
            return 1


    def is_game_over(self):
        return self._game_over_status

# class GameController ends
