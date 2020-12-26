class Body(object):
	def __init__(self, xPos, yPos, width, height):
		self.x = xPos
		self.y = yPos
		self.width = width
		self.height = height

	def changePos(self, xPos, yPos):
		self.x = xPos
		self.y = yPos
