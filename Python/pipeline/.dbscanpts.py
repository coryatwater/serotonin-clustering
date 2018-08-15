from sklearn.cluster import DBSCAN
import numpy as np
import x, y, z
import time

# make it print the whole thing out
np.set_printoptions(threshold=np.nan)

# store the data in this array
data = [x.x,y.y,z.z]
print "(" + str(len(x.x)) + ", " + str(len(y.y)) + ", " + str(len(z.z)) + ")"
print "began with " + str(len(x.x))
# zip the data from [x,y,z] to [(x,y,z),(x,z,z)...]
data = zip(*data)

# make the DBSCANner with tuned epsilon and minimum sample size
db = DBSCAN(eps=50, min_samples=30).fit(data)

# create an empty array of zeroes the length of the label list
# then turn it into a mask, so that I can scoop out the points that are gucci
labels = db.labels_
the_label = 5
core_samples = zip(*db.components_)

x = open("scanned_indices/xc.py", "w")
y = open("scanned_indices/yc.py", "w")
z = open("scanned_indices/zc.py", "w")

x.write("x = [")
y.write("y = [")
z.write("z = [")

begin = time.time()
print str(len(core_samples))
print "(" + str(core_samples[0]) + ", " + str(core_samples[1]) + ", " + str(core_samples[2]) + ")"
x.write(str(core_samples[0]) + ", ")
y.write(str(core_samples[1]) + ", ")
z.write(str(core_samples[2]) + ", ")

x.write("()]")
y.write("()]")
z.write("()]")
print "ended with " + str(len(core_samples[0]))
print str(len(set(db.labels_))) + " blobs found"
print time.time() - begin

