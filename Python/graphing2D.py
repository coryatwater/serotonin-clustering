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
	return (vmax - vmin) * np.random.normal(.5, .1, xDim)

def makebins(xvals, yvals):
	summ = 0
	for i in range(len(xvals)):
		summ += xvals[i]
		n = (int)(xvals[i] / binWidth)
		bins[n] += 1
	print('actual mean', (summ/len(xvals)))
	return bins

# construct random points

# first spot
xvals = randrange(xDim, 0, yDim*2)
yvals = randrange(xDim, 0, yDim*2)

# second spot
xvals1 = randrange(xDim, 0, yDim)
yvals1 = randrange(xDim, 0, yDim)

# label graph
plt.ylabel('Height')
plt.xlabel('Width')

plt.plot(xvals, yvals, 'r.', markersize=1)
plt.plot(xvals1, yvals1, 'b.', markersize=1)
##plt.axis([0, numbins, 0, numbins])

blo = makebins(xvals1, yvals1)
N = numBins
x = np.arange(N)
width = 1/1.5
##plt.bar(x, blo, width, color="blue")

line.liner()
plt.show()
