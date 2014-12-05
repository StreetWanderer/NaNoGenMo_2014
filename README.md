NaNoGenMo 2014
==============
A small tentative at novel generation using an image as the novel inspiration.

Created in reply to dariusk's [NaNoGenMo 2014](https://github.com/dariusk/NaNoGenMo-2014).

[About this entry] (https://github.com/dariusk/NaNoGenMo-2014/issues/69)

About the code
---

**TL;DR** : The script takes an image file, extract CMYK color for each pixel and convert that into words using a dictionary.  
&nbsp;  
The script opens the given image file (here it's nyan_cat.jpg) using Pillow. This Python lib allows me to open the jpg image and access the pixel datas.  
First thing is to crop the image to limit the number of pixels included in the novel to around 50k. Right after that, Pillow converts the image to CMYK to get 4 numbers per pixel.  
Each number is then converted to a letter thanks to a remap of the values on the ascii grid and converted to letters with [unichr](https://docs.python.org/2/library/functions.html#unichr).  
This creates 4 letters words that are fed to PyEnchant who gives the closest word it can find in the dictionary.  
After that (it's the part I'm not satisfied with at all) I randomly add a delimiter (either '. ', ' ', '.\n') after the word to create some variety in the text structure.  
Every sentence is then formated to be all lowercase except the first character (too look more like a sentence) and written to a text file.  
Once the script runs out of pixels you get a novel in the text file.  

Improvements
----
* Fix the random delimiters and uses image datas (i.e. colors changes) to define which delimiter to use.
* Use an other dictionary to find words  (more powerful and with more vocabulary)
* Overall speed


Dependencies
---
* [Pillow](https://pillow.readthedocs.org/)
* [PyEnchant](http://pythonhosted.org/pyenchant/)
