import cv2
from imutils import contours
from skimage import measure
import multiprocessing as mp
import numpy as np
import time
import tqdm
def find_multi_max(z_index):
	filex = open("x.py", "a")
	filey = open("y.py", "a")
	filez = open("z.py", "a")

	infix = format( z_index + 1, '03d')
	strname = '../../Images/hcr_spotted/Gad1-B2-647-B4-cy3b_sample1_40x-2-1_Out_z' + infix + 'c1+2.bmp'
	img = cv2.imread(strname)

	blur_radius = 1
	threshold = 26
	lbl_size = 3

	contrast = 100
	brightness = 0
	#convert to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#gray = cv2.blur(gray,(blur_radius, blur_radius))

	#gaussian blur to denoise
	gray = cv2.GaussianBlur(gray, (blur_radius, blur_radius), 0)

	#thresholding to get rid of more noise
	_, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
	its = 1
#	thresh = cv2.erode(thresh, None, iterations=its)
#	thresh = cv2.dilate(thresh, None, iterations=its)

	#perform connected component analysis on thresholded image
	#then make a mask to store only large components (large is
	#satisfying the size predfined as lbl_size)
	labels = measure.label(thresh, neighbors=8, connectivity=1, background=0)
	mask = np.zeros(thresh.shape, dtype="uint8")

	safe = False
	for label in np.unique(labels):
		#ignore background labels
		if label == 0:
			continue
		#construct the label mask and count the amount of pixels in it
		labelMask = np.zeros(thresh.shape, dtype="uint8")
		labelMask[labels == label] = 255

		numPixels = cv2.countNonZero(labelMask)

		#if the pixel number is large enough add it to mask of large blobs)
		if numPixels > lbl_size:
			safe = True
			mask = cv2.add(mask, labelMask)

	if not safe: return
	#find the countours in the mask
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[1]
	cnts = contours.sort_contours(cnts)[0]


	#loop over the contours
	#print "OUTSIDE " + str(z_index)
#	thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
	for (i, c) in enumerate(cnts):
		# draw the bright spot on the image
		(x, y, w, h) = cv2.boundingRect(c)
		((cX, cY), radius) = cv2.minEnclosingCircle(c)
		cv2.circle(thresh, ((int)(cX), (int)(cY)), 1, (255,255,255), 5)
		filex.write((", " + str(cX)))
		filey.write((", " + str(cY)))
		filez.write((", " + str(z_index * 8)))
#		cv2.putText(thresh, "({},{})".format(cX,cY), (x, y - 15),
#			cv2.FONT_HERSHEY_SIMPLEX, .45, (255, 255, 255), 2)
	cv2.imwrite(strname, thresh)
	

def main():
	with open("x.py", "w") as x:
		x.write("x = [0")
	with open("y.py", "w") as y:
		y.write("y = [0")
	with open("z.py", "w") as z:
		z.write("z = [0")

	#begin multiprocessing if in main thread
	if __name__ == '__main__':
		pool = mp.Pool(processes=8)

	#create an array for the images
	start = 1
	how_many = 185

	begin = time.time()

	print (begin - time.time()) * 189


	for _ in tqdm.tqdm(pool.imap(find_multi_max, range(start, how_many)), total=(how_many - start)):
		success = True
	pass

	print (time.time() - begin)
	'''
	#write images
	for i in range(1, 188):
		print i
		infix = format( i + 1, '03d')
		strname = '../../Images/hcr_spotted/Gad1-B2-647-B4-cy3b_sample1_40x-2-1_Out_z' + infix + 'c1+2.bmp'
		cv2.imwrite(strname, arr[i])
	'''
	x = open("x.py", "a")
	y = open("y.py", "a")
	z = open("z.py", "a")


	x.write("]")
	y.write("]")
	z.write("]")

main()	
