class Blocks:

	rotation = 0
	x = 0
	y = 0

	def i_block(self, x, y):
		color = (255, 0, 0)	# red
		positions = [(x, y), (x, y-1), (x, y-2), (x, y-3)]	# standard positions for i_block
		return (positions, color)

	def o_block(self, x, y):
		color = (0, 0, 255)	# darkblue
		positions = [(x, y), (x, y-1), (x+1, y-1), (x+1, y)]
		return (positions, color)

	def l_block(self, x, y):
		color = (66, 0, 66)	# purple
		positions = [(x, y), (x+1, y), (x, y-1), (x, y-2)]
		return (positions, color)

	def z_block(self, x, y):
		color = (0, 66, 0)	# greem
		positions = [(x, y), (x+1, y), (x+1, y+1), (x+2, y+1)]
		return (positions, color)

	def t_block(self, x, y):
		color = (66, 33, 0)	# orange
		positions = [(x, y), (x+1, y), (x+1, y-1), (x+2, y)]
		return (positions, color)
