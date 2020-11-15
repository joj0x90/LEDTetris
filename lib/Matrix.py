class matrix:
	### FLAGS ###
	VERBOSE = True

	Xmax = 0
	Ymax = 0
	mode = 0

	adresses = []
	pixel = []

	def __init__(self, x, y, mode=0):
		# mode -> order of the data line (see README.txt)
		if mode==1 or mode==0:
			if x>0 and y>0:
				self.Xmax = x
				self.Ymax = y
				self.mode = mode
				self.initArray()

	def printMatrix(self, matrix=None):
		# prints Matrix to console
		if matrix == None:
			# if no matrox was given, print the pixel as default
			matrix = self.pixel
		if self.VERBOSE:
			# if verbose it prints the max x and max y
			print("X: "+str(len(matrix))+" Y: "+str(len(matrix[0])))
		for y in range(len(matrix)):
			print("[ ", end="")
			for x in range(len(matrix[y])):
				num = matrix[y][x]
				if(num < 10):
					print("   "+str(num), end="")
				elif(num < 100):
					print("  "+str(num), end="")
				else:
					print(" "+str(num), end="")
			print("]")

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
				new_row.append(0);
			self.pixel.append(new_row)

	def invert_horizontally(self, y):
		# inverts the given row of the adresses array in horizontal direction
		if y>0 and y<self.Ymax:
			row = self.adresses[y]
			new_row = list(reversed(row))
			self.adresses[y] = new_row

	def invert_vertical(self):
		# inverts the adresses array in vertical direction
		new_adresses = list(reversed(self.adresses))
		self.adresses = new_adresses

	def getAdr(self, x, y):
		# returns Adress of LED at x and y coordinates
		if(x>0 and x<self.Xmax and y>0 and y<self.Ymax):
			return self.adresses[y][x]
