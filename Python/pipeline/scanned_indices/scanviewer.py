import sys
import xc, yc, zc
import cv2
import time as t
import random

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

x = xc.x
y = yc.y
z = zc.z

filex = open("x.py", "a")
filey = open("y.py", "a")
filez = open("z.py", "a")

def cluster_data(clusters):
	for i in range(len(clusters[0])):
		print "cluster " + str(i) + " contains " + str(len(clusters[0][i])) + " points"

def compute_cluster_center(x, y, z, ind):
	lenx = len(x)
	xsum, ysum, zsum = (0,0,0)
	for i in range(lenx):
		xsum += x[i]
		ysum += y[i]
		zsum += z[i]
	xsum /= lenx
	ysum /= lenx
	zsum /= lenx

	print str(ind + 1) + ") center is " + "(" + str(xsum) + ", " + str(ysum) + ", " + str(zsum) + ")"
def clear_line(i):
	for j in range(i):
		sys.stdout.write(CURSOR_UP_ONE)
		sys.stdout.write(ERASE_LINE)
			
def save_spots(z_index, col, tick):
	clear_line(3)

	for i in range(tick):
		sys.stdout.write(CURSOR_UP_ONE)
		sys.stdout.write(ERASE_LINE)
	tick = 0
	print "image " + str(z_index)
	print "------------"
	counter = 0
	infix = format( z_index + 1, '03d')
	strname = '../../Images/hcr_spotted/Gad1-B2-647-B4-cy3b_sample1_40x-2-1_Out_z' + infix + 'c1+2.bmp'
	img = cv2.imread(strname)
	minCell = 100

	lineThickness = 1
	x1, x2 = (50,100)
	yint = 50
	for j in range(0,len(z)):
		done = False
		if len(z[j]) < minCell: continue
		for i in range(0,len(z[j])):
			if (z[j][i] == (z_index * 8)):
				if not done:
					compute_cluster_center(x[j], y[j], z[j], j)
					tick += 1
					done = True
			
				cv2.circle(img, ((int)(x[j][i]), (int)(y[j][i])), 9, col[j], 2)
				cv2.circle(img, ((int)(x[j][i]), (int)(y[j][i])), 1, (255,255,255), 5)
				cv2.line(img, (x1, yint - 10), (x1, yint + 10), (255,255,255), lineThickness)
				cv2.line(img, (x2, yint - 10), (x2, yint + 10), (255,255,255), lineThickness)
				cv2.line(img, (x1, yint), (x2, yint), (255,255,25), lineThickness)
				stri = "{} px.".format(x2 - x1)
				cv2.putText(img, stri, (x1, yint + 20),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 0)
				counter += 1

	cv2.namedWindow('image',cv2.WINDOW_NORMAL)
	cv2.imshow('image',img)
	cv2.resizeWindow('image', 600,600)
	step = cv2.waitKey(0)
	print
	if step == 106:
		return (-1, tick)
	else: return (1, tick)

cluster_data([x,y,z])
num = len(z) + 1
colors = mylist = [((random.randrange(0, 255),random.randrange(0,255), random.randrange(0,255)))  for k in range(num)]
numages = 186
mini = 2
i = mini
tick = 0
while i < numages:
	j, tick = save_spots(i, colors, tick)
	i += j
	if i < mini or i > numages:
		break	
	yint = 50
