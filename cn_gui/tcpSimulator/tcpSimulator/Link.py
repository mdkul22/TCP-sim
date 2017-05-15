from NetworkElement import NetworkElement

class Link(NetworkElement):

	transmissionTime = 0.0
	propagationTime = 0.0

	node1 = None
	node2 = None

	packetsFromN1toN2 = None
	packetDelaysN1toN2 = None

	packetsFromN2toN1 = None
	packetDelaysN2toN1 = None

	lastTimeProcessCalledMode1 = 0.0
	lastTimeProcessCalledMode2 = 0.0

	def __init__(self, simulator, name, node1, node2, transmissionTime, propagationTime):
		# self.simulator = simulator
		# self.name = name
		super(Link, self).__init__(simulator, name)
		self.node1 = node1
		self.node2 = node2
		self.transmissionTime = transmissionTime
		self.propagationTime = propagationTime

	def getTransmissionTime():
		return self.transmissionTime

	def setTransmissionTime(self, transmissionTime_):
		self.transmissionTime = transmissionTime_

	def getPropagationTime():
		return propagationTime

	def setPropagationTime(self, propagationTime_):
		self.propagationTime = propagationTime_

	def send(self, source, packet):
		if (node1 == source):
			self.enqueueNewPacket(packetsFromN1toN, packetDelaysN1toN2, packet)
		elif (node2 == source):
			self.enqueueNewPacket(packetsFromN2toN1, packetDelaysN2toN1, packet)
		else:
			print "Link.send() --- PANIC --- impossible packet source!?"

	def process(mode):
		if (mode == 0):
			if (packetsFromN1toN2):
				deliverArrivedPackets(packetsFromN1toN2, packetDelaysN1toN2, node2, lastTimeProcessCalled)
			
			if (packetsFromN2toN1):
				deliverArrivedPackets(packetsFromN2toN1, packetDelaysN2toN1, node1, lastTimeProcessCalled)
			
			lastTimeProcessCalled = self.getSimulator().getCurrentTime()

		if (mode == 1):
			if (packetsFromN1toN2):
				deliverArrivedPackets(packetsFromN1toN2, packetDelaysN1toN2, node2, lastTimeProcessCalledMode1)

				lastTimeProcessCalledMode1 = self.getSimulator().getCurrentTime()

		if (mode == 2):
			if (packetsFromN2toN1):
				deliverArrivedPackets(packetsFromN2toN1, packetDelaysN2toN1, node1, lastTimeProcessCalledMode2)
				
				lastTimeProcessCalledMode2 = self.getSimulator().getCurrentTime()

	# Link does not handle incoming packets, so this method does nothing
	def handle(dummySource, dummyPacket):
		print "Link.handle():  PANIC -- how did we get here ?!?!?"

	def enqueueNewPacket(packets, packetDelays, packet):
		idx = len(packets)
		packets.append(packet)

		if ((idx == 0) or (packetDelays[idx - 1] < propagationTime + transmissionTime)):
			packetDelays[idx] = propagationTime + transmissionTime
		else:
			packetDelays[idx] = packetDelays[idx - 1]

	def deliverArrivedPacket(packets, packetDelays, node, lastTimeProcessCalled):
		pass

#def main():
#	myLink = Link("simulator", "name", "node1", "node2", 0.0, 0.0)
#	simulator = myLink.transmissionTime
#	print simulator
#	print myLink.getSimulator()

#if __name__ == "__main__":
#	main()
