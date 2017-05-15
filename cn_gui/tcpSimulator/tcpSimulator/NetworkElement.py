class NetworkElement(object):

	# simulator = None
	# name = None
	_lastTimeProcessCalled = 0.0

	def __init__(self, simulator = None, name = None): #lastTimeProcessCalled = 0.0):
		self.simulator = simulator
		self.name = name

	# 
	def getName(self):
		return self.name

	def process(self, mode):
		pass

	def send(self, source, packet):
		pass

	def handle(self, source, packet):
		pass

	def getSimulator(self):
		return self.simulator

# def main():
# 	myNetworkElement = NetworkElement("simulator", "name")
# 	name = myNetworkElement.getName()
# 	sim = myNetworkElement.getSimulator()
# 	print name, sim, NetworkElement._lastTimeProcessCalled

# if __name__ == "__main__":
# 	main()
