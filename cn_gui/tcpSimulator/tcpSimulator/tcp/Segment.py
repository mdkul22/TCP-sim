from NetworkElement import NetworkElement
from Packet import Packet
import sys

class Segment(Packet):
    dataSequenceNumber = 0
    ackSequenceNumber = 0
    isAck = 0
    rcvWindow = 0
    timestamp = -1

    def __init__(self, destinationAddr, rcvWindow, seqNum = -1, dataPayload = None, ackSeqNum = -1):
        super(Segment, self).__init__(destinationAddr, dataPayload)
        self.rcvWindow = rcvWindow
        self.dataSequenceNumber = seqNum
        self.ackSequenceNumber = ackSeqNum
        self.isAck = (ackSeqNum >= 0)
        self.ordinalNum = (self.dataSequenceNumber / Sender.MSS) + (self.dataSequenceNumber % Sender.MSS) + 1
        self.ordinalNumAck = (self.ackSequenceNumber / Sender.MSS) + (self.ackSequenceNumber % Sender.MSS) + 1

        def setAckSequenceNumber(self, ackSequenceNumber):
            self.ackSequenceNumber = ackSequenceNumber
            self.ordinalNumAck = (ackSequenceNumber / Sender.MSS) + (ackSequenceNumber % Sender.MSS) + 1

    # Prints the Acknowledgement and Segment number. Use for debugging.
    def __str__ (self):
        print "Segment # " + str(ordinalNum)

        if isAck:
            identifierAck = "ACK # " + str(ordinalNumAck)
            print identifierAck

def main():
	mySegment = Segment("127.0.0.1", 100)
	print mySegment.getDestinationAddress()
	print mySegment.rcvWindow
	print mySegment.dataSequenceNumber
	print mySegment.getDataPayLoad()
	print mySegment.ackSequenceNumber

if __name__ == "__main__":
	main()
