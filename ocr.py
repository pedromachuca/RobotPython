#-*- coding: utf8 -*-

import pytesseract
import cv2
import numpy as np
from PIL import Image, ImageEnhance

def resolve(img):

	#test contrast enhancer
	#contrast_enhancer = ImageEnhance.Contrast(img)
	#pil_enhanced_image = contrast_enhancer.enhance(2)
	#enhanced_image = np.asarray(pil_enhanced_image)
	#r, g, b = cv2.split(enhanced_image)
	#enhanced_image = cv2.merge([b, g, r])

	#convert the image to gray scale
	#imgray = cv2.cvtColor(np.asarray(enhanced_image),cv2.COLOR_BGR2GRAY)

	#use tesseract to find the image
	return pytesseract.image_to_string(img)

def sort(string):

	reverse_string =''.join(reversed(string))
	print reverse_string
	return reverse_string

img = 'captcha.png'
#load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
image = Image.open(img)
captcha_text = resolve(image)
print "\n=====output=======\n"
print captcha_text+"\n"
