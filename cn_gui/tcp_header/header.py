from struct import *
from collections import namedtuple
import random

class Generator():

    def __init__(self):

        self.tcp_source = 1234
        self.tcp_dest = 80
        self.tcp_seq = 0
        self.tcp_ack_seq = 0
        self.tcp_hlen = 5
        # tcp flags
        self.tcp_urg = 0
        self.tcp_ack = 0
        self.tcp_psh = 0
        self.tcp_rst = 0
        self.tcp_syn = 1
        self.tcp_fin = 0
        # others
        self.tcp_window_size = 10
        self.tcp_checksum = 0
        self.tcp_urg_ptr = 0
        self.tcp_offset_res = (self.tcp_hlen << 4) + 0
        self.tcp_flags = self.tcp_urg + (self.tcp_ack << 1) + (self.tcp_psh << 2) + (self.tcp_rst << 3) + (self.tcp_syn<<4) + (self.tcp_fin<<5)

    def set_ack(self):
        self.tcp_ack = 1

    def sender_ack_seq(self):
        self.tcp_ack_seq = self.tcp_seq + 1

    def fin_activate(self):
        self.tcp_fin = 1

    def init_seq(self):
        self.tcp_ack = random.randint(100, 10000)

    def create_packet(self):
        return pack('HHLLBBH', self.tcp_source, self.tcp_dest, self.tcp_seq,
             self.tcp_ack_seq, self.tcp_offset_res, self.tcp_flags, self.tcp_window_size) + pack('H', self.tcp_checksum)


def main():
    packet = Generator().create_packet()
    print(packet)

if __name__ == '__main__':
    main()