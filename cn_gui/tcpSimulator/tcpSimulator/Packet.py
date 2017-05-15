from NetworkElement import NetworkElement

class Packet(object):

	inError = False

	def __init__(self, destinationAddress, dataPayLoad):
		self.destinationAddress = destinationAddress
		self.dataPayLoad = dataPayLoad
		self.length = dataPayLoad if (dataPayLoad != None) else 0

	def getDestinationAddress(self):
		return self.destinationAddress

	def getDataPayLoad(self):
		return self.dataPayLoad

# def main():
# 	myPacket = Packet("127.0.0.1", 100)
# 	destinationAddress = myPacket.getDestinationAddress()
# 	dataPayLoad = myPacket.getDataPayLoad()
# 	print destinationAddress, dataPayLoad, Packet.inError

# if __name__ == "__main__":
# 	main()
