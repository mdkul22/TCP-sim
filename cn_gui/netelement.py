__author__ = "VM"
from .. import tcp_header
from tcp_header import header


class Channel_Handler():
    """enacts the channel between receiver and sender and gives
       congestion properties"""

    def __init__(self):
        self.t_frame = 0
        self.t_prop = 0
        self.buffer_size = 0

    def set_tframe(self, x):
        self.t_frame = x

    def set_tprop(self, x):
        self.t_prop = x

    def set_buffer(self, x):
        self.buffer_size = x

    def receive_packet(self, packet):
        """receives packet and handles it"""


class Node():
    """Acts as both sender and receiver and simulates nodes"""

    def __init__(self):

        self.counter = 0
        self.drop = 0
        self.success = 0
        self.spacket = header.Generator().create_packet()

    def send_packet(self, rpacket):

        if(rpacket.tcp_ack == 1):
            self.spacket.sender_ack_seq()

        else:
            self.spacket.init_seq()

        return self.spacket

    def packet_dropped(self, signal):

        if signal == "y":
            self.drop += 1

        return self.drop

    def packet_success(self, signal):

        if signal == "y":
            self.success += 1

        return self.success

    def packet_received(self):

        pass

class decision_maker()
   """ decides if transmitted signal is a success or not """
  def __init__(self):
      
      
def main():
    node_1 = Node()
    node_2 = Node()
    Sys_Handler = Channel_Handler()


if __name__ == "__main__":
    main()
