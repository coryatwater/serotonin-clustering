from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int, help="radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

processed_x = []
processed_y = []
processed_z = []
'''
print(args["image"])
image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.imshow('image',orig)
cv2.waitKey(0)
cv2.imshow('image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow("Naive", image)
cv2.waitKey(0)
'''


def find_max(img):
	#make  a grayscale copy of img
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	#save critical values to various variables
	(minWeakVal, maxWeakVal, minWeakLoc, maxWeakLoc) = cv2.minMaxLoc(gray)

	#apply gaussian blur to denoise
	gray = cv2.GaussianBlur(gray, (41, 41), 0)

	#save critical values to various variables for good blurred process
	(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

	#draw a circle on the highest intensity points for both methods
	cv2.circle(img, maxLoc, 40, (255, 0, 0), 2)
	cv2.circle(img, maxWeakLoc, 40, (0,255,0), 2)

	#show the image and hold it until theres a keypress
	cv2.imshow('image', img)
	cv2.waitKey(0)

#TODO: https://www.pyimagesearch.com/2016/10/31/
	#detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
def find_multi_max(img, z_index):
	#convert to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#gaussian blur to denoise
	blurred = cv2.GaussianBlur(gray, (3, 3), 0)

	#thresholding to get rid of more noise
	thremage, thresh = cv2.threshold(blurred, 65, 255, cv2.THRESH_BINARY)
	thresh = cv2.erode(thresh, None, iterations=2)
	thresh = cv2.dilate(thresh, None, iterations=4)

	#perform connected component analysis on thresholded image
	#then make a mask to store only large components
	labels = measure.label(thresh, neighbors=8, connectivity=2, background=0)
	mask = np.zeros(thresh.shape, dtype="uint8")

	safe = False
	for label in np.unique(labels):
		#ignore background labels
		if label == 0:
			print('hit a bg')
			continue
		#construct the label mask and count the amount of pixels in it
		labelMask = np.zeros(thresh.shape, dtype="uint8")
		labelMask[labels == label] = 255

		numPixels = cv2.countNonZero(labelMask)

		#if the pixel number is large enough add it to mask of large blobs)
		if numPixels > 100:
			safe = True
			mask = cv2.add(mask, labelMask)
	if not safe: return
	#find the countours in the mask
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[1]
	cnts = contours.sort_contours(cnts)[0]
	# loop over the contours
	for (i, c) in enumerate(cnts):
		#draw bright spot
#		print('drawing spot')
#		(x, y, w, h) = cv2.boundingRect(c)
		((cX, cY), radius) = cv2.minEnclosingCircle(c)
#		cv2.circle(img, (int(cX), int(cY)), 40, (0,0,255), 3)
#		cv2.putText(img, "#{}".format(i + 1), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX,
#					.45, (0,0,255), 2)
		processed_x.append(cX)
		processed_y.append(cY)
		processed_z.append(z_index * 3)
def print_pixel_values(img):
	width, height,_ = img.shape
	for i in range(width):
		for j in range(height):
			if(img[i, j][0] > 10 or img[i, j][0] > 10 or img[i, j][0] > 10):
				print(img[i, j])
			
def operate_on_stack(func):
	t0 = time.time()
	#Gad1-B2-647-B4-cy3b_sample1_40x-2-1_Out_z158c1+2.tif
	file_prefix = '../Images/hcr_analysis/Gad1-B2-647-B4-cy3b_sample1_40x-2-1_Out_z'
	file_suffix = 'c1+2.tif'
	z_stack_size = 189
	z_stack = [0] * z_stack_size

	for i in range(z_stack_size):
		file_name = file_prefix + format(i + 1, '03d') + file_suffix
		z_stack[i] = cv2.imread(file_name)
		func(z_stack[i], i)
		print(file_name)

	print(time.time() - t0)

np.set_printoptions(threshold=np.nan)
operate_on_stack(find_multi_max)
x = open("x.py", "w")
y = open("y.py", "w")
z = open("z.py", "w")

x.write("x = ")
y.write("y = ")
z.write("z = ")

x.write(str(processed_x))
y.write(str(processed_y))
z.write(str(processed_z))
