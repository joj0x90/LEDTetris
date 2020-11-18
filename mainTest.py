#!/usr/bin/python

from lib import GameBoard
from lib import LEDs
import board
import neopixel

PIN = board.D18		# GPIO18
ORDER = neopixel.RGB
X = 8
Y = 15

gBoard = GameBoard.gameboard(X, Y)
m = gBoard.getMatrix()
leds = LEDs.LEDs(m)
leds.wait(0.5)
leds.all_off()

print(m.toString())
#gBoard.setPixel(5, 7, (255, 0, 0))
gBoard.setBlock(0, 5, 'i_block')
print(m.toString())
gBoard.setBlock(1, 3, 'o_block')
print(m.toString())
gBoard.setBlock(2, 6, 'l_block')
print(m.toString())
gBoard.setBlock(3, 3, 'z_block')
print(m.toString())
gBoard.setBlock(4, 10, 't_block')
print(m.toString())

#mat = Matrix.matrix(X, Y)
#mat.invert_horizontally(3)
#mat.printMatrix()
#mat.invert_vertical()
#for y in range(mat.Ymax):
#	mat.invert_horizontally(y)
#print("\n\ninverted:")
#mat.printMatrix(mat.adresses)

#print("("+str(5)+", "+str(10)+") = "+str(mat.getAdr(5, 10)))

#pixels = neopixel.NeoPixel(PIN, X*Y, brightness = 0.1, auto_write=False,  pixel_order=ORDER)
#pixels.fill((255, 0, 0))
#pixels[mat.getAdr(5, 10)] = (0, 0, 0)
#pixels.show()
