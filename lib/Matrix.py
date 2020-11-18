from lib import colors

class matrix:
	### FLAGS ###
	VERBOSE = True

	Xmax = 0
	Ymax = 0
	mode = 0

	adresses = []
	pixel = []
	color = colors.colors()

	def __init__(self, x, y, mode=0):
		# mode -> order of the data line (see README.txt)
		if mode==1 or mode==0:
			if x>0 and y>0:
				self.Xmax = x
				self.Ymax = y
				self.mode = mode
				self.initArray()
			else:
				raise ValueError("value(s) out of range")
		else:
			raise ValueError("value(s) out of range")

	def toString(self, matrix=None):
		# returns a string, of the Matrix, ready to print on the console.
		if matrix == None:
			# if no matrix was given, use the pixel Matrix
			matrix = self.pixel
		string = ""
		if self.VERBOSE:
			# if verbose it will concatenate the String with the max values for x and y
			string += "X: "+str(len(matrix))+" Y: "+str(len(matrix[0]))+"\n"
		for y in range(len(matrix)):
			string += "["
			for x in range(len(matrix[y])):
				num = matrix[y][x]
				if matrix == self.pixel:
					string += self.color.rgbBackground(num)
				else:
					if(num < 10):
						string += "   "+str(num)
					elif(num < 100):
						string += "  "+str(num)
					else:
						string += " "+str(num)
			string += "]\n"
		return string

	def initArray(self):
		# initializes the Adresses-array according to given x, y and mode variables
		if self.mode == 0:
			# data line is ordered like a snake
			for y in range(self.Ymax):
				row = []
				if y % 2 == 0:
					# even rows
					for x in range(self.Xmax):
						row.append(y*self.Xmax+x)
				else:
					# uneven rows
					for x in range(self.Xmax):
						row.append(y*self.Xmax+(self.Xmax-x)-1)
				self.adresses.append(row)
		else:
			# data line starts at begin of each row
			for y in range(self.Ymax):
				row = []
				for x in range(self.Xmax):
					row.append(y*self.Xmax+x)
				self.adresses.append(row)

		for yi in range(self.Ymax):
			new_row = []
			for xi in range(self.Xmax):
				new_row.append((10, 10, 10));
			self.pixel.append(new_row)

	def invert_horizontally(self, y):
		# inverts the given row of the adresses array in horizontal direction
		if y>0 and y<self.Ymax:
			row = self.adresses[y]
			new_row = list(reversed(row))
			self.adresses[y] = new_row
		else:
			raise ValueError("value(s) out of range")

	def invert_vertical(self):
		# inverts the adresses array in vertical direction
		new_adresses = list(reversed(self.adresses))
		self.adresses = new_adresses

	def getAdr(self, x, y):
		# returns Adress of LED at x and y coordinates
		if(x>0 and x<self.Xmax and y>0 and y<self.Ymax):
			return self.adresses[y][x]
		else:
			raise ValueError("value(s) out of range")

	def getPixels(self):
		# returns the pixel matrix
		return self.pixel

	def setPixel(self, x, y, color):
		if x<0 or y<0 or x>self.Xmax-1 or y>self.Ymax-1:
			raise ValueError("value(s) "+str(x)+" or "+str(y)+" out of range")
		r = color[0]
		g = color[1]
		b = color[2]
		if r>=0 and g>=0 and b>=0 and r<256 and g<256 and b<256:
			self.pixel[y][x] = color
		else:
			raise ValueError("value(s) out of range")
