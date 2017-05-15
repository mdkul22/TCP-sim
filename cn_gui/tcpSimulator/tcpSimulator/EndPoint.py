from NetworkElement import NetworkElement
from tcp.Segment import Segment

class EndPoint(NetworkElement):
    networkLayerProtocol = None
    remoteEndpoint = None
    sender = None
    reciever = None

    def __init__(self, simulator = None, name = None, remoteTCPendpoint = None, senderType = None, rcvWindow = None):
        super(EndPoint, self).__init__(simulator, name)
        self.remoteEndpoint = remoteTCPendpoint

        if (senderType == "Tahoe"):
            self.sender = SenderTahoe(self)
        elif (senderType == "Reno"):
            self.sender = SenderReno(self)
        else:
            print "TCPEndpoint.TCPEndpoint -- unknown TCP sender type."
            exit

        receiver = Receiver(self, rcvWindow);

    def setLink(self, adjoiningLink):
        self.networkLayerProtocol = adjoiningLink

    def getRemoteTCPendpoint(self):
        return self.remoteEndpoint

    def getSender(self):
        return sender

    def getLocalRcvWindow(self):
        return reciever.getRcvWindow()

    def timerExpired(self, timerType):
        pass

    def process(self, mode):
        if (mode == 1):
            simulator.checkExpiredTimers(sender)
            sender.send(None)

        elif (mode == 2):
            simulator.checkExpiredTimers(reciever)

    def send (self, source, newDataPkt):
        sender.send(newDataPkt.dataPayload)

    def handle (source, packet):
        # segment = Segment(packet)
        if (segment == None):
            if ((Simulator.currentReportingLevel and Simulator.REPORTING_SENDERS) != 0) or ((Simulator.currentReportingLevel & Simulator.REPORTING_RECEIVERS) != 0):
                print "Endpoint.handle(): unknown packet type"
            return

        if (segment.isAck()):
            reciever.handle(segment)

        if (segment.length > 0):
            reciever.handle(segment)

        def getNetworkLayerProtocol(self):
            return self.networkLayerProtocol
