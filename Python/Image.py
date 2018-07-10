from PIL import Image

im = Image.open('../Images/mad.png')
pixels = im.load()

img = Image.new(im.mode, im.size)

for row in range(img.size[0]):
	for col in range(img.size[1]):
		print(pixels[row,col])
img.show()
img.close()
