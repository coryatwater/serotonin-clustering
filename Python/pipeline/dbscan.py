from sklearn.cluster import DBSCAN
import numpy as np
import x, y, z
import time

# make it print the whole thing out
np.set_printoptions(threshold=np.nan)

# store the data in this array
data = [x.x,y.y,z.z]
start = len(x.x)
# zip the data from [x,y,z] to [(x,y,z),(x,z,z)...]
data = zip(*data)

# make the DBSCANner with tuned epsilon and minimum sample size
db = DBSCAN(eps=40, min_samples=45).fit(data)

# create an empty array of zeroes the length of the label list
# then turn it into a mask, so that I can scoop out the points that are gucci
labels = db.labels_
the_label = 5
end = len(db.core_sample_indices_)
unique_labels = set(db.labels_)

x = open("scanned_indices/xc.py", "w")
y = open("scanned_indices/yc.py", "w")
z = open("scanned_indices/zc.py", "w")

x.write("x = [")
y.write("y = [")
z.write("z = [")

begin = time.time()

for the_label in range(1, len(unique_labels) - 1):
	print the_label
	core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
	core_samples_mask[db.core_sample_indices_] = True
	points_mask = np.zeros_like(db.labels_, dtype=bool)
	points_mask = (labels == the_label)

	core_samples = np.array(data)[core_samples_mask & points_mask]

	core_samples = zip(*core_samples)
	x.write(str(core_samples[0]) + ", ")
	y.write(str(core_samples[1]) + ", ")
	z.write(str(core_samples[2]) + ", ")

x.write("()]")
y.write("()]")
z.write("()]")

print time.time() - begin
print "began with " + str(start) + " ended with " + str(end)

