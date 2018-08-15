import cv2
import numpy as np
import time as t
import multiprocessing as mp
import argparse

def print_numbers(i):
	print i

def read_and_process(i):
	c = i[1]
	i = i[0]
	infix = format( i + 1, '03d')
#	strname = '../../Images/hcr_analysis/Gad1-B2-647-B4-cy3b_sample1_40x-2-1_Out_z' + infix + 'c1+2.tif'
#	                              set_2_z     026     _c001.gif
 	strname = '../../Images/set_2/CZI_z' + infix + '_c002.bmp'
#	strname = '../Images/mad.png'
	frame = cv2.imread(strname, 1)
	frame = cv2.GaussianBlur(frame,(3,3),0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#green channel settings:
	#	lower: 60, 56, 24
	#	upper: 61, 200, 255
	#red channel settings:
	#	lower: 61, 0, 27
	#	upper: 255, 206, 255

	if c == "red":
		lower = np.array([61,0,27])
		upper = np.array([255,206,255])
	if c == "green":
		lower = np.array([60,56,24])
		upper = np.array([61,200,255])
	if c == "ns":
		lower = np.array([0,0,27])
		upper = np.array([255,255,255])
	

	kernel = np.ones((5,5)) * -1
	kernel[2,2] = 24
	res = cv2.filter2D(frame, -1, kernel)
	mask = cv2.inRange(hsv, lower, upper)
	res = cv2.bitwise_and(res,res, mask=mask)
	return res

def write_image(i):
	infix = format( i[0] + 1, '03d')
	strname = '../../Images/hcr_spotted/Gad1-B2-647-B4-cy3b_sample1_40x-2-1_Out_z' + infix + 'c1+2.bmp'
	cv2.imwrite(strname, i[1]);

def process_images(pool):
	ap = argparse.ArgumentParser()
	ap.add_argument("-c", "--channel", help = "what color spots to isolate")
	#ap.add_argument("-r", "--radius", type = int, help="radius of Gaussian blur; must be odd")
	args = vars(ap.parse_args())
	c = args["channel"]
	if c == None: c = "ns"
	begin = t.time()
	print t.time() - begin



	numages = 187
	begin = t.time()
	print "processing images... "
	arr = pool.map(read_and_process, zip(*(range(1,numages), ([c] * numages))))
	print "finished in " + str(t.time() - begin)
	return arr

def write_images(pool, arr):
	print "writing images... "
	begin = t.time()
	stuff = zip(*(range(1, len(arr)), arr))
	pool.map(write_image, stuff)
	print "finished in " + str(t.time() - begin)
	print "exiting"

def localize_hsv_profile():
	upper = 255
	lower = 0
	step = (upper + lower) / 2
	cursor = step
	while 1:
		step /= 2
		if step == 0: step = 1
		next_step = 'u'
		res = read_and_process(cursor)
		cv2.imshow('142', res)
		cv2.waitKey(5)
		next_step = raw_input("u or d: ")
		if next_step == 'd':
			cursor -= step
		elif next_step == 'u':
			cursor += step
		else:
			break
		print str(cursor) + " " + str(step)
def main():
	if __name__ == '__main__':
		pool = mp.Pool(processes=8)
	images = process_images(pool)
	write_images(pool, images)
	
main()
