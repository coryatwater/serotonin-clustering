import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Define the dimensions of the graph (symmetric in x and y by default)
xDim = 1000
yDim = xDim

# Define width of the bins for grouping when creating gaussians
binWidth = 10

# The amount of bins is equal to the length in the x direction 
# divided by the bin width
numBins = (int)(xDim/binWidth)

# keep track of the bins
xBins = [0] * numBins
yBins = [0] * numBins

# Creates an array of length n with values between vmin and vmax.
# The values in the array that get returned will have a normal
# distribution about a random point between vmin and vmax
def randrange(n, vmin, vmax):

	# Get a random center point for the graph
	rand = np.random.rand(1)[0] * xDim/2
	if (round(rand * 10) % 2 == 0):
		rand *= -1

	return (((vmax - vmin)) * np.random.normal(.5, .1, n)) + rand

# Sort the data points into bins
def makebins(xvals):
	# Keep track of the sum total to compute the mean
	summ = 0
	bins = [0] * numBins

	# Loop through all of the points contained by the graph
	for i in range(len(xvals)):

		# Set val as the value at this point in the graph
		val = xvals[i]

		# Add this value to the mean
		summ += val

		# Make sure that the value isn't too big or small to fit into
		# one of the bins that are set up
		if (val > xDim - binWidth or val < 0): continue

		# Find and set the bin that this point belongs in
		n = (int)(val / binWidth)
		bins[n] += 1
	print('actual mean', (summ/len(xvals)))
	return bins


# Generates random spots
# TODO: Actual RNA spot detection
def generatespots(numSpots, numPoints):
	# Set up 2d array to contain X and Y values
	pointsList = [[0],
		      [0]]

	# Generate a spot i times
	for i in range(numSpots):

		# Create an X and a Y set of indices
		spotx = randrange(numPoints, 0, xDim)
		spoty = randrange(numPoints, 0, yDim)

		# Add this spot's points to the list of points
		pointsList[0] = np.concatenate((pointsList[0], spotx))
		pointsList[1] = np.concatenate((pointsList[1], spoty))

	return pointsList

# Denoise an array by smoothing it (pretty destructive so look out)
def meandenoise(vals, intensity):
	'''
	 Hey bud, I'm Cory. I hope what I wrote here is looking
	 good to you so far! I'm just writing this cuz I figured 
	 it might be a little funny to see a message from me in 
	the middle of the file. Have a good read, and a good day!
	'''
	# Keep track of the previous values so that when you loop thru
	# for multiple denoisings you use the most recently denoised
	# function
	valsprev = vals
	# Define an alternator so that the resulting function isn't offest
	flicker = 1

	# Denoise (intensity) times
	for i in range(intensity):

		# Create an empty array equal to the previous values
		vals2 = [0] * len(valsprev)

		# Make each value the average of this value and the next
		for i in range(len(valsprev) - 1):
			vals2[i + flicker] = ((valsprev[i] + valsprev[i + 1]) /2 )

		# Make the edited set the new set of values
		valsprev = vals2

		# Set flicker to the other value
		if (flicker == 1): flicker = 0
		else:flicker = 1

	return vals2

# Construct random spots
pList = generatespots(3,2000)

# Get set of points
xvals = pList[0]
yvals = pList[1]

# Create an array
x = np.arange(numBins) * binWidth
y = np.arange(numBins) * binWidth

xBins = makebins(xvals)
yBins = makebins(yvals)

plt.plot(x, xBins, 'r', linewidth=2.0)
plt.plot(yBins, y, 'b', linewidth=2.0)

# label graph
plt.ylabel('Height')
plt.xlabel('Width')

# Plot points
plt.plot(xvals, yvals, 'r.', markersize=1)
plt.axis([0, xDim, 0, yDim])


# Plot a bunch of different levels of denoising
#xBins = meandenoise(xBins, 100)
#yBins = meandenoise(yBins, 100)
plt.plot(x, xBins,linewidth=2.0)
plt.plot(yBins, y,linewidth=2.0)

zBins = np.add(xBins, yBins)

plt.plot(x, zBins,linewidth=2.0)

# Plot the bar graph of bins 
plt.bar(x, xBins, xDim / 200, color="blue")
plt.barh(y, yBins, xDim / 200, color="green")

'''
xBins = meandenoise(xBins, 100)
plt.plot(x, xBins,linewidth=2.0)
xBins = meandenoise(xBins, 100)
plt.plot(x, xBins,linewidth=2.0)
xBins = meandenoise(xBins, 100)
plt.plot(x, xBins,linewidth=2.0)
'''
plt.show()
