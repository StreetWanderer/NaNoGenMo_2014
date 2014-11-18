from PIL import Image
import enchant
import utils

def main(image, dest_file, language):
	#init all
	output = ''
	d = enchant.Dict(language)
	novel = open(dest_file, 'wb+')
	imgSrc = Image.open(image)
	#get center of image
	rect = utils.centerRect(imgSrc.size, (224, 224))
	print rect
	img = imgSrc.crop(rect)
	img = img.convert('CMYK')

	size = img.size #Get the width and height of the image for iterating over
	print img.size

	#generate novel by iterating over pixels
	for x in xrange(0,size[0]):
		for y in xrange(0,size[1]):
			
			pixel = img.getpixel((x,y))
			word = ''
			for color in pixel:
				char = utils.arduino_map(color, 0, 256, 65, 122)
				word += unichr(char)

			output += utils.correctedWord(word, d)
			output += utils.getDelimiter(0.1, 0.4, 0.3)
			
		output = utils.formatSentence(output)
		print "loop ", x ," of ", size[0]
		novel.write(output)
		output = ''

	novel.close()
	return True;



main('nyan_cat.jpg', 'novel.txt', 'en_US')