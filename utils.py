import random

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