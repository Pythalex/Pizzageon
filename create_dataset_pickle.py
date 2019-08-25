import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import pickle
import pandas as pd

directory = os.listdir("images")
nb_of_images = len(directory)

class Dataset:
	target = None
	data = None

dataset = Dataset()
dataset.target = np.ndarray((nb_of_images, ), dtype='uint8')
dataset.data = np.ndarray((nb_of_images, 3, 200, 200), dtype=bool)

def create_narray_from_pixels_data(pixels, width, height):
	array = np.zeros(shape=(3, height, width)) # RGB channels, width x height pixels
	for w in range(width):
		for h in range(height):
			p = pixels[w, h]
			if type(p) == int: # if BW image
				p = (p, p, p)
			try:
				for channel in range(3):
					array[channel, h, w] = p[channel]
			except:
				print(p)
				print(type(p))
				print(w, h)
				print(type(pixels))
				print(type(pixels[0,0]))
				print(pixels[0,0])
				exit(1)
	return array
	
def plot_image(array_img):
	plt.figure()
	plt.imshow(array_img, cmap=plt.cm.binary)
	plt.colorbar()
	plt.grid(False)
	plt.show()

def main():
	for idx, filename in enumerate(directory):
		
		if filename[:6] == "pigeon":
			target = 0 # pigeon
		else:
			target = 1 # pizza
			
		img = Image.open("images/" + filename)
		pixels = img.load()
		#print(filename)
		data = create_narray_from_pixels_data(pixels, 200, 200)
		
		dataset.target[idx] = target
		dataset.data[idx] = data
main()

with open("dataset.pkl", "wb") as f:
	pickle.dump(dataset, f)
		