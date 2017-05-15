class TimerSimulated(object):
    def __init__(self, callback, type, time):
        self.callback = callback
        self.type = type
        self.setTime(time)

    def getTime(self):
        return self.time
    
    def setTime(self, time):
        self.time = time
