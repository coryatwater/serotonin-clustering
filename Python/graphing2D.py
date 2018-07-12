import matplotlib.pyplot as plt
import numpy as np
import line as line
xDim = 1000
yDim = xDim
binWidth = 10
numBins = (int)(xDim/binWidth)
bins = [0] * numBins
flicker = 1

def randrange(n, vmin, vmax):
	'''
	from https://matplotlib.org
	returns an array of random numbers in the specified range
	@param n    - length of array
	@param vmin - minimum random number
	@param vmax - maximum random number
	'''
	#np.random.rand() gives an array of randoms
	randy = np.random.rand(1)[0] * 500
	if (round(randy) % 2 == 0):
		randy *= -1
		print('yolo!', randy)
	print('ono!', randy)

	return (((vmax - vmin)) * np.random.normal(.5, .1, n)) + randy

def makebins(xvals, yvals):
	summ = 0
	for i in range(len(xvals)):
		val = xvals[i]
		summ += val
		if (val > xDim - binWidth or val < 0): continue
		n = (int)(val / binWidth)
		bins[n] += 1
	print('actual mean', (summ/len(xvals)))
	bins[0] = bins[1]
	bins[len(bins) - 1] = bins[len(bins) - 2]
	return bins

def normalize(dataset):
	for i in range(len(dataset)):
		if ((dataset[i] / binWidth) > numBins - 1):
			dataset[i] = xDim - binWidth
		elif ((dataset[i] / binWidth) < 0):
			dataset[i] = 0
	return dataset

def generatespots(numSpots, numPoints):
	totalPoints = numSpots * numPoints
	pointsList = [[0],
		      [0]]
	for i in range(numSpots):
		spotx = randrange(numPoints, 0, xDim)
		spoty = randrange(numPoints, 0, yDim)
		pointsList[0] = np.concatenate((pointsList[0], spotx))
		pointsList[1] = np.concatenate((pointsList[1], spoty))
	return pointsList

def meandenoise(yvals, intensity):
	yvalsprev = yvals
	flicker = 1
	for i in range(intensity):
		yvals2 = [0] * len(yvalsprev)
		for i in range(len(yvalsprev) - 1):
			yvals2[i + flicker] = ((yvalsprev[i] + yvalsprev[i + 1]) /2 )
		yvalsprev = yvals2
		if (flicker == 1): flicker = 0
		else:flicker = 1
	return yvals2

# construct random points
pList = generatespots(2,2000)

# get set of points
xvals = pList[0]
yvals = pList[1]


x = np.arange(numBins) * binWidth
blo = makebins(xvals, yvals)
plt.plot(x, blo, 'r', linewidth=2.0)

# label graph
plt.ylabel('Height')
plt.xlabel('Width')
plt.plot(xvals, yvals, 'r.', markersize=1)
plt.axis([0, xDim, 0, yDim])

blo = meandenoise(blo, 100)
width = 1/1.5
plt.bar(x, blo, 1, color="blue")
plt.plot(x, blo,linewidth=2.0)

blo = meandenoise(blo, 100)
plt.plot(x, blo,linewidth=2.0)
blo = meandenoise(blo, 100)
plt.plot(x, blo,linewidth=2.0)
blo = meandenoise(blo, 100)
plt.plot(x, blo,linewidth=2.0)

plt.show()
