#
# Tambola / Housie Mobile Game
#

__author__ = 'nitin'


#import time
from player_ticket import PlayerTicket


class PlayerInputHandler:

    def __init__(self, game_instance):
        self._game_instance = game_instance

        #Player Id will be sent by Client
        # TODO Need to create player Ids in DB
        self._player_id = 24

        # We may create ticket Id here/Any need of  keeping Ticket record?
        _tkt = PlayerTicket()
        _tkt.print_ticket()

        self.win_status = {0:0, 1:0, 2:0, 3:0, 4:0}

    def worker_thread(self):
        pass # TODO


    #
    # The prints are too verbose right now. These would be removed when the
    # application is hosted on the web server.
    #
    def input_handler(self, key):
        if (key == '0'):
            print "Key Press. ** Client side event. Needn't be sent to server.\n"
        elif (key == '1'):
            status = self._game_instance.claim(int(key), self._player_id)
            if (status == 0):
                print "Congratulations. First line is yours. \
** Correctness to be checked in Client side code.\n"
                self.win_status[1] = 1
            else:
                print "Sorry, First line is already taken"

        elif (key == '2'):
            status = self._game_instance.claim(int(key), self._player_id)
            if (status == 0):
                print "Congratulations. Second line is yours. \
** Correctness to be checked in Client side code.\n"
                self.win_status[2] = 1
            else:
                print "Sorry, Second line is already taken"

        elif (key == '3'):
            status = self._game_instance.claim(int(key), self._player_id)
            if (status == 0):
                print "Congratulations. Third line is yours. \
** Correctness to be checked in Client side code.\n"
                self.win_status[3] = 1
            else:
                print "Sorry, Third line is already taken"

        elif (key == '4'):
            status = self._game_instance.claim(int(key), self._player_id)
            if (status == 0):
                print "Congratulations. Full House is yours. \
** Correctness to be checked in Client side code.\n"
                self.win_status[4] = 1
            else:
                print "Sorry, Full House already claimed."

        else:
            print "Wrong Input. **Input checked in client side -- Can't reach server."


    def get_points(self):
        return self.win_status

# class PlayerInputHandler Ends
