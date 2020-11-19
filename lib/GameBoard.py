from lib import Matrix
from lib import colors
from lib import Blocks

class gameboard:

	mat = []
	X = 0
	Y = 0
	color = colors.colors()
	blocks = Blocks.Blocks()

	def __init__(self, x, y, mode=0):
		self.mat = Matrix.matrix(x, y, mode)
		self.X = x
		self.Y = y
		self.mat.VERBOSE = False


	def getMatrix(self):
		# returns the pixel matrix
		return self.mat

	def setPixel(self, x, y, color):
		# sets the pixel at coordinate (x, y) to color
		r = color[0]
		g = color[1]
		b = color[2]
		if r>=0 and g>=0 and b>=0 and r<256 and g<256 and b<256:
			self.mat.setPixel(x, y, color)
		else:
			raise ValueError("value(s) out of range")

	def setBlock(self, x, y, block):
		if x>=0 and y>=0 and x<self.mat.Xmax and y<self.mat.Ymax:

			if self.mat.VERBOSE:
				print("new "+str(block)+": ("+str(x)+", "+str(y)+")")

			if block == 'i_block':
				object = self.blocks.i_block(x, y)
				for px in range(len(object[0])):
					self.setPixel(object[0][px][0], object[0][px][1], object[1])
			elif block == 'l_block':
				object = self.blocks.l_block(x, y)
				for px in range(len(object[0])):
					self.setPixel(object[0][px][0], object[0][px][1], object[1])
			elif block == 'z_block':
				object = self.blocks.z_block(x, y)
				for px in range(len(object[0])):
					self.setPixel(object[0][px][0], object[0][px][1], object[1])
			elif block == 'o_block':
				object = self.blocks.o_block(x, y)
				for px in range(len(object[0])):
					self.setPixel(object[0][px][0], object[0][px][1], object[1])
			elif block == 't_block':
				object = self.blocks.t_block(x, y)
				for px in range(len(object[0])):
					self.setPixel(object[0][px][0], object[0][px][1], object[1])
			else:
				raise ValueError("'"+str(block)+ "' is no block")
		else:
			raise ValueError("value(s) out of range")
