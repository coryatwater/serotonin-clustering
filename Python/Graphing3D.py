import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
	'''
	from https://matplotlib.org
	returns an array of random numbers in the specified range
	@param n    - length of array
	@param vmin - minimum random number
	@param vmax - maximum random number
	'''
	#np.random.rand() gives an array of randoms
	return (vmax - vmin) * np.random.rand(n) + vmin

def tdistance(pa, pb):
	'''
	determines distance between 2 points
	@param pa first point
	@param pb second point
	'''
	return (((pa[0] - pb[0]) ** 2 +
		 (pa[1] - pb[1]) ** 2 +
		 (pa[2] - pb[2]) ** 2 ) ** .5)

def flattenArray(row, col, numpts):
	print((numpts * (numpts + 1))/2 + 100)

def getdistances(xs, ys, zs):
	'''
	determines distances between all combinations of points and
	returns them in an array. The first point is the "tens" place,
	and the second point is the ones place
	@param xs x values
	@param ys y values
	@param zs z values
	'''
	#number of points
	numpts = len(xs)
	prev = 0
	points = [(numpts * (numpts + 1))/2 + 100]
	for row in range(numpts):
		for col in range(row, numpts):
			print(prev + col)
		prev += (numpts - row - 1)

	# for all points
	# check for neighbors
	# if less than minPts then the thing is noise
	# else its a cluster seed
		# go thru the cluster seed's points and determine neighbors of neighbors
		# if the neighbor < minpoints its not part of the cluster
		# if the neighbor >= minpoints its a part of the cluster

###################################################
#Graphing3D main                                  #
###################################################

ax = plt.gca(projection = '3d')

xs = randrange(100,0, 100)
zs = randrange(100,0, 100)
ys = randrange(100,0, 100)
ax.scatter(xs, ys, label='scapt')
ax.plot([1,100],[1,100],[1, 100], 'gray')


plt.show()
