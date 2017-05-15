# import tcp.Sender
from Endpoint import EndPoint
# from Router import Router
from Link import Link

class Simulator(object):
    REPORTING_SIMULATOR = 1 << 1
    REPORTING_LINKS = 1 << 2
    REPORTING_ROUTERS = 1 << 3
    REPORTING_SENDERS = 1 << 4
    REPORTING_RECEIVERS = 1 << 5
    REPORTING_RTO_ESTIMATE = 1 << 6
    currentReportingLevel = REPORTING_SIMULATOR | REPORTING_LINKS | REPORTING_ROUTERS | REPORTING_SENDERS
    TOTAL_DATA_LENGTH = 1000000
    senderEndpt = None
    receiverEndpt = None
    router = None
    link1 = None
    link2 = None
    currentTime = 1.0
    timers = []

    def __init__(self, tcpSenderVersion, bufferSize, rcvWindow):
        tcpReceiverVersion = "Tahoe"
        print "================================================================\n" + "          Running TCP " + tcpSenderVersion_ + " sender  (and " + tcpReceiverVersion_ + " receiver).\n"

        try:
            self.senderEndpt = Endpoint(self, "sender", None, tcpSenderVersion, rcvWindow)
            self.receiverEndpt = EndPoint(self, "reciever", self.senderEndpt, tcpReceiverVersion, rcvWindow)
            self.senderEndpt.setRemoteTCPendpoint(setRemoteTCPendpoint)
        except(Exception):
            pass # Decide what to do later
            return

        self.router = Router(self, "router", bufferSize)

        self.link1 = Link(self, "link1", senderEndpt, router, 0.001, 0.001)

        self.link2 = Link(self, "link2", receiverEndpt, router, 0.01, 0.001)

        self.senderEndpt.setLink(link1)
        self.receiverEndpt.setLink(link2)

        self.router.addForwardingTableEntry(senderEndpt, link1)
        self.router.addForwardingTableEntry(receiverEndpt, link2)

