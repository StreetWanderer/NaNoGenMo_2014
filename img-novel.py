from PIL import Image

def main(image):
	output = ''
	novel = open('novel.txt', 'wb+')
	img = Image.open(image)

	img = img.convert('CMYK')

	size = img.size #Get the width and hight of the image for iterating over
	
	for x in xrange(0,size[0]):
		for y in xrange(0,size[1]):
			
			pixel = img.getpixel((x,y))
			
			for color in pixel:
				char = arduino_map(color, 0, 256, 65, 122)
				output += unichr(char)
			
			output += ' '
		#output += '\n'
		novel.write(output.encode('ascii'))
		output = ''

	novel.close()
	
def arduino_map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
	

	'''
	for line in img:
		bLine = bytearray(line)
		output += bLine
		
		for char in bLine:
			try:
				output += str(unichr(char))
			except Exception, e:
				output += ' '
		'''
			

	
	



main('glitched.jpg')