import matplotlib.pyplot as plt
import numpy as np
import line as line
xDim = 1000
yDim = xDim
binWidth = 10
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
	return (vmax - vmin) * np.random.normal(.5, .1, xDim) + vmin

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
	pointsList = [[numPoints * numSpots], [numPoints * numSpots]]
	for i in range(numSpots):
		rand = np.random.rand(1)[0]
		print(rand)
		'''
		spotx = randrange(xDim, 0, yDim * rand)
		spoty = randrange(xDim, 0, yDim * rand)
		xvals = np.concatenate((spot1x, spot2x, spot3x))
		yvals = np.concatenate((spot1y, spot2y, spot3y))
		'''
	
# construct random points

# first spot
spot1x = randrange(xDim, 0, yDim)
spot1y = randrange(xDim, 0, yDim)

# second spot
spot2x = randrange(xDim, 0, yDim)
spot2y = randrange(xDim, 0, yDim)

# second spot
spot3x = randrange(xDim, 0, yDim / 4)
spot3y = randrange(xDim, 0, yDim / 4)

# get set of points
xvals = np.concatenate((spot1x, spot2x, spot3x))
yvals = np.concatenate((spot1y, spot2y, spot3y))

generatespots(5,5)

# label graph
plt.ylabel('Height')
plt.xlabel('Width')

plt.plot(xvals, yvals, 'r.', markersize=1)
plt.axis([0, xDim, 0, yDim])
print(xvals,yvals)
blo = makebins(xvals, yvals)
x = np.arange(numBins) * binWidth
print(blo)
width = 1/1.5
plt.bar(x, blo, 8, color="blue")


lineee = line.line(1, 200)
print(lineee.yfromx(10))
plt.show()
