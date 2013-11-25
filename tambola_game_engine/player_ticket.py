from os import sys


#Global Variables
_ticket_array = [0 for x in range(0,30)]

class PlayerTicket:

    global _ticket_array

    def __init__(self):
        # TODO using a Hard coded ticket right now for test
        _ticket_array[0] = 1
        _ticket_array[3] = 33
        _ticket_array[6] = 61
        _ticket_array[9] = 92
        _ticket_array[11] = 14
        _ticket_array[12] = 22
        _ticket_array[15] = 51
        _ticket_array[18] = 85
        _ticket_array[22] = 28
        _ticket_array[24] = 47
        _ticket_array[29] = 99

    def print_ticket(self):
        print "-" * 45
        for i in range(0,3):
            for j in range(1,10):
                ticket_line = "%3d" %_ticket_array[(i*10 + j)] + " |"
                sys.stdout.write (ticket_line)
            print "\n"
        print "-" * 45 + "\n"

# class PlayerTicket ends
