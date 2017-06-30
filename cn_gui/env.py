import random as r
from math import floor
from time import sleep


class Sender():

    def __init__(self):

        self.packet = 0
        self.count = 0

    def send_packet(self):

        sleep(floor(r.uniform(1, 10)))
        self.packet = floor(r.uniform(0, 15))
        self.count += 1
        return self.packet

    def log_print(self):

        print(self.count)


class Channel():

    def __init__(self):

        self.buffer = []

    def receive_packet(self, sender_packet):

        self.buffer.append(sender_packet)

    def send_to_rx(self):

        return self.buffer.pop()


class Receiver():

    def __init__(self):

        self.store = []
        self.count = 0

    def rx_packet(self, received):

        self.count += 1
        self.store.append(received)

    def log_print(self):
#        print(self.store)
        print(str(self.count) + 'r')

if __name__ == "__main__":
    x = Channel()
    y = Sender()
    z = Receiver()

    while True:	
        #sleep(floor(r.uniform(1, 10)))
        x.receive_packet(y.send_packet())
    	y.log_print()
    	z.rx_packet(x.send_to_rx())
    	z.log_print()
