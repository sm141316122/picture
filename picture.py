from PIL import Image
import os

for file in os.listdir("old_pictures"):
	img = Image.open(os.path.join("old_pictures", file)) #file path
	img = img.convert('L') # convert to L (Grayscale)
	img.save(os.path.join("new_pictures", file[:-4] + "_grey.jpg"))#file path