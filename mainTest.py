#!/usr/bin/python

from lib import Matrix
import board
import neopixel

PIN = board.D18		# GPIO18
ORDER = neopixel.RGB
X = 8
Y = 15

mat = Matrix.matrix(X, Y)
#mat.invert_horizontally(3)
mat.printMatrix()
#mat.invert_vertical()
for y in range(mat.Ymax):
	mat.invert_horizontally(y)
print("\n\ninverted:")
mat.printMatrix(mat.adresses)

print("("+str(5)+", "+str(10)+") = "+str(mat.getAdr(5, 10)))

pixels = neopixel.NeoPixel(PIN, X*Y, brightness = 0.1, auto_write=False,  pixel_order=ORDER)
#pixels.fill((255, 0, 0))
pixels[mat.getAdr(5, 10)] = (0, 0, 0)
pixels.show()
