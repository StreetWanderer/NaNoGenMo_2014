import random
from PIL import Image
import enchant

def main(image):
	output = ''
	d = enchant.Dict("en_US")
	novel = open('novel.txt', 'wb+')
	imgSrc = Image.open(image)
	rect = centerRect(imgSrc.size, (224, 224))
	print rect
	img = imgSrc.crop(rect)
	img = img.convert('CMYK')

	size = img.size #Get the width and hight of the image for iterating over
	print img.size

	for x in xrange(0,size[0]):
		for y in xrange(0,size[1]):
			
			pixel = img.getpixel((x,y))
			word = ''
			for color in pixel:
				char = arduino_map(color, 0, 256, 65, 122)
				word += unichr(char)

			output += correctedWord(word, d)
			output += getDelimiter(0.1, 0.4, 0.7)
			
			#ouput = formatSentence(output)

		print "loop ", x ," of ", size[0]
		novel.write(output)
		output = ''

	novel.close()
	return true;
	
def arduino_map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def centerRect(img_size, target_size):
	left = img_size[0]/2 - target_size[0]/2
	upper = img_size[1]/2 - target_size[1]/2
	right = left + target_size[0]
	lower = upper + target_size[1]
	return (left, upper, right, lower)

def formatSentence(sentence):
	sentence = sentence.lower()


def correctedWord(word, d):
	suggest = d.suggest(word)
	if len(suggest) > 0:
		return random.choice(suggest)
	else:
		return word

def getDelimiter(sentenceChance, newLineChance, chapterChance):
	delimiter = ' '
	
	if random.random() < sentenceChance:
		delimiter = '. '
		if random.random() <= newLineChance:
			delimiter = '\n'
			if random.random() <= chapterChance:
				delimiter += '\n'

	return delimiter
		


main('nyan_cat.jpg')