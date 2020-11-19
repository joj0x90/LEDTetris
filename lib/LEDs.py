import neopixel
import time
import board

class LEDs:

	PIN = board.D18
	MAT = None
	BRIGHTNESS = 0.1
	ORDER = None

	def __init__ (self, mat, pin=board.D18, brightness=0.1, order=neopixel.RGB):
		self.MAT = mat
		self.PIN = pin
		self.BRIGHTNESS = brightness
		self.ORDER = order
		self.pixels = neopixel.NeoPixel(self.PIN, self.MAT.Xmax*self.MAT.Ymax, auto_write=False, pixel_order=self.ORDER)
		self.pixels.fill((255, 255, 255))
		self.pixels.show()


	def all_off(self):
		self.pixels.fill((0, 0, 0))
		self.pixels.show()

	def wait(self, duration):
		time.sleep(duration)
