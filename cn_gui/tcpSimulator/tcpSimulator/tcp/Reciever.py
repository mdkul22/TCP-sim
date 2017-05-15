from EndPoint import EndPoint
from TimedComponent import TimedComponent

class Reciever(TimedComponent):
    delayedACKtimer = None
    delayedACKtimerHandle = None
    maxRcvWindowSize = 65536
    currentRcvWindow = 0
    rcvBuffer = []
    cumulativeACK = None
    lastByteRecvd = -1
    nextByteExpected = 0

    def __init__(self, localTCPendpoint = None, rcvWindowSize = None):
        self.localEndpoint = localTCPendpoint
        self.maxRcvWindowSize = rcvWindowSize
        self.currentRcvWindow = self.maxRcvWindowSize
        delayedACKtimer = TimerSimulated(self, 2, 0.0)

    def getRcvWindow(self):
        return self.currentRcvWindow;

    def timerExpired(self, timerType):
        self.delayedACKtimerHandle = None
        self.sendCumulativeAcknowledgement()

    def sendCumulativeAcknowledgement(self):
        if (self.delayedACKtimerHandle != None):
            try:
                self.localEndpoint.getSimulator().cancelTimeout(self.delayedACKtimerHandle)
            except(Exception):
                # I DON'T KNOW WHAT TO DO HERE
                pass

        if (self.cumulativeACK != None):
            self.localEndpoint.getNetworkLayerProtocol().send(self.localEndpoint, self.cumulativeACK)
            self.cumulativeACK = None

    def handle(self, segment):
        if (segment.inError):
            return

        if (segment.dataSequenceNumber == self.nextByteExpected):
            self.nextByteExpected = segment.dataSequenceNumber + segment.length

            if (self.rcvBuffer.isEmpty()):
                self.lastByteRecvd = segment.dataSequenceNumber + segment.length - 1
            else:
                checkBufferedSegments()

            if (self.cumulativeACK == None):
                self.cumulativeACK = Segment(self.localEndpoint.getRemoteTCPendpoint(), self.currentRcvWindow, self.nextByteExpected)
                self.cumulativeACK.timestamp = segment.timestamp;
                self.delayedACKtimer.setTime(self.localEndpoint.getSimulator().getCurrentTime())
                try:
                    self.delayedACKtimerHandle = self.localEndpoint.getSimulator().setTimeoutAt(delayedACKtimer)
                except(Exception):
                    # I DON'T KNOW WHAT TO DO HERE
                    pass
            else:
                self.cumulativeACK.rcvWindow = self.currentRcvWindow
                self.cumulativeACK.setAckSequenceNumber(nextByteExpected)
                self.cumulativeACK.timestamp = segment.timestamp
        else:
            self.sendCumulativeAcknowledgement()
            self.localEndpoint.getNetworkLayerProtocol().send(self.localEndpoint, self.handleOutOfSequenceSegment(segment))

        if ((Simulator.currentReportingLevel and Simulator.REPORTING_RECEIVERS) != 0):
            print "Reciever" + "\t" + "lastByteRecvd=" + self.lastByteRecvd + "\t" + "nextByteExpected=" + self.nextByteExpected + "\t" + "currentRcvWindow="+ self.currentRcvWindow

    def handleOutOfSequenceSegment(self, segment):
        outOfOrderSeg = segment
        self.rcvBuffer.add(outOfOrderSeg)

        self.lastByteRecvd = max(self.lastByteRecvd, outOfOrderSeg.dataSequenceNumber + outOfOrderSeg.length - 1)

        self.currentRcvWindow = self.maxRcvWindowSize - (self.lastByteRecvd - self.nextByteExpected)

        return Segment(self.localEndpoint.getRemoteTCPendpoint(), self.currentRcvWindow, -1, None, self.nextByteExpected)

    def checkBufferedSegments(self):
        self.rcvBuffer.sort()
        bufferedItems = self.rcvBuffer.copy()
        
        counter = 0
        while(not(bufferedItem)):
            seg = bufferedItems[counter]

            if (seg.dataSequenceNumber == self.nextByteExpected):
                self.nextByteExpected = seg.dataSequenceNumber + seg.length
                self.currentRcvWindow = self.maxRcvWindowSize - (self.lastByteRecvd - self.nextByteExpected)
                counter = counter + 1;
            else:
                break
