import matplotlib.pyplot as plt
import numpy as np
import line as line
xDim = 100
yDim = xDim
binWidth = 3
numBins = (int)(xDim/binWidth)
bins = [0] * numBins

def randrange(n, vmin, vmax):
	'''
	from https://matplotlib.org
	returns an array of random numbers in the specified range
	@param n    - length of array
	@param vmin - minimum random number
	@param vmax - maximum random number
	'''
	#np.random.rand() gives an array of randoms
	return (vmax - vmin) * np.random.normal(.5, .1, n)

def makebins(xvals, yvals):
	summ = 0
	for i in range(len(xvals)):
		summ += xvals[i]
		n = (int)(xvals[i] / binWidth)
		bins[n] += 1
	print('actual mean', (summ/len(xvals)))
	return bins

def normalize(dataset):
	for i in range(len(dataset)):
		dataset[i] = (50 * (dataset[i] / 150))
	return dataset

def generatespots(numSpots, numPoints):
	totalPoints = numSpots * numPoints
	pointsList = [[0],
		      [0]]
	for i in range(numSpots):
		rand = np.random.rand(1)[0]
		spotx = randrange(numPoints, 0, yDim)
		spoty = randrange(numPoints, 0, yDim)
		pointsList[0] = np.concatenate((pointsList[0], spotx))
		pointsList[1] = np.concatenate((pointsList[1], spoty))
		'''
		xvals = np.concatenate((spot1x, spot2x, spot3x))
		yvals = np.concatenate((spot1y, spot2y, spot3y))
		'''
	return pointsList
# construct random points

# first spot
spot1x = randrange(xDim, 0, yDim) - xDim/10 * 3
spot1y = randrange(xDim, 0, yDim) - xDim/10 * 3

# second spot
spot2x = randrange(xDim, 0, yDim) + xDim/10
spot2y = randrange(xDim, 0, yDim) + xDim/10

# second spot
#spot3x = randrange(xDim, 0, yDim)
#spot3y = randrange(xDim, 0, yDim)

pList = generatespots(5,50)

# get set of points
xvals = pList[0]
yvals = pList[1]

# label graph
plt.ylabel('Height')
plt.xlabel('Width')
plt.plot(xvals, yvals, 'r.', markersize=1)
plt.axis([0, xDim, 0, yDim])
blo = makebins(xvals, yvals)
x = np.arange(numBins) * binWidth
print(blo)
width = 1/1.5
#plt.bar(x, blo, 1, color="blue")
plt.plot(x, blo, linewidth=2.0)

lineee = line.line(1, 200)
print(lineee.yfromx(10))
plt.show()
