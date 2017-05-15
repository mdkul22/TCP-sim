# import Simulator

class RTOEstimator(object):
    alphaShift = 3
    betaShift = 2
    stdDevMultShift = 2
    maxTimeoutInterval = 240.0
    estimatedRTT_init = 0
    deviationRTT_init = 12
    timeoutInterval_init = 6.0
    tickDuration = 1.0
    estimatedRTT = 0
    devRTT = 0
    timeoutInterval = maxTimeoutInterval
    backoff = 1

    def __init__(self, tick, estimRTT_init = 0, deviatRTT_init = 12, baseRTT_init = 6.0, maxRTO = 240.0):
        if (tick > 0.0):
            self.tickDuration = tick

        if (estimRTT_init >= 0.0):
            self.estimatedRTT = int(estimRTT_init / self.tickDuration)

        if(deviatRTT_init >= 0.0):
            self.devRTT = int(deviatRTT_init / self.tickDuration)

        if (baseRTT_init >= 0.0):
            self.timeoutInterval = baseRTT_init

        if (maxRTO > 0.0) and (maxRTO <= 240.0):
            self.maxTimeoutInterval = maxRTO / self.tickDuration

    def updateRTT(self, currentTime, timestamp):
        if (timestamp < 0):
            return

        backoff = 1

        sampleRTT = int((currentTime - timestamp) / self.tickDuration + 0.5)
        
        if (sampleRTT < 1):
            sampleRTT = 1

        if (self.estimatedRTT != 0):
            err = sampleRTT - self.estimatedRTT;
            estimatedRTT = (err >> alphaShift)

            if (err < 0):
                err = ~err

            delta = err - self.devRTT
            devRTT = (delta >> betaShift)

        else:
            self.estimatedRTT = sampleRTT
            devRTT = sampleRTT >> 1

        self.timeoutInterval = self.estimatedRTT + max(self.tickDuration, (self.devRTT << self.stdDevMultShift))

        if (self.timeoutInterval < 1.0):
            self.timeoutInterval = 1.0

        self.timeoutInterval *= self.tickDuration

        if ((Simulator.currentReportingLevel and Simulator.REPORTING_RTO_ESTIMATE) != 0.0):
            print "RTT UPDATE:  (sampleRTT = " + sampleRTT + ", estimatedRTT = " + estimatedRTT + ", devRTT = " + devRTT + ", timeoutInterval = " + timeoutInterval + ", backoff = " + backoff + ")"

    def timerBackoff(self):
        if (self.timeoutInterval < self.maxTimeoutInterval):
            self.backoff <<= 1

        if ((Simulator.currentReportingLevel and Simulator.REPORTING_RTO_ESTIMATE) != 0):
            print "TIMEOUT: timer backoff to " + self.backoff + " times"