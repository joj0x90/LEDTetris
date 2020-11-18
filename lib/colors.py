class colors:

	def rgbBackground(self, color, text=None):
		# returns a string with escaped color strings, if provided a text, backgroudn color will be set to whichever rgb-color was in first parameter.
		r = color[0]
		g = color[1]
		b = color[2]
		if r>=0 and g>=0 and b>=0 and r<256 and g<256 and b<256:
			# if values are within range
			if text == None:
				return "\033[48;2;"+str(r)+";"+str(g)+";"+str(b)+"m  \033[0m"
			else:
				return "\033[48;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+text+"\033[0m"
		else:
			raise ValueError("value(s) out of range")

	def rgbText(self, color, text=None):
		# returns a string with escaped color strings, which will set the font size of text to provided color in first argument
		r = color[0]
		g = color[1]
		b = color[2]
		if r>=0 and g>=0 and b>=0 and r<256 and g<256 and b<256:
			# if values are within range
			if text != None:
				# if text was provided
				return "\u001b[38;2;"+str(r)+";"+str(g)+";"+str(b)+"m"+text+"\033[0m"
			else:
				raise ValueError("no text given as argument")
		else:
			raise ValueError("value(s) out of range")
