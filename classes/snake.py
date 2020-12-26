from classes.body import Body

class Snake(object):
	def __init__(self, headX, headY):
		self.headX = headX
		self.headY = headY
		self.height = 10
		self.width = 10
		self.bodyNodes = []
		self.bodyNodes.append( Body(self.headX, self.headY, 10, 10) )

	def appendFood(self ,xPos, yPos):
		self.bodyNodes.append( Body(xPos, yPos, 10, 10) )