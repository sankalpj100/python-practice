import random
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def dataset_creation():
	text = open('/home/sankalp/dm/iris.data')
	data_all = []
	for line in text:
	    row_data = line.strip("\n").split()
	    data_all.append(row_data)
	data_all.pop()
	final_dataset = []
	for data in data_all:
		line = ' '.join(map(str, data))
		row = line.split(",")
		final_row = row[0:4]
		final_row = [float(val) for val in final_row]
		final_dataset.append(final_row)
	random.shuffle(final_dataset)
	return final_dataset
	
def euc_distance(centroid, val):
	x1, y1, z1, o1 = val[0], val[1], val[2], val[3]
	X1, Y1, Z1, O1 = centroid[0], centroid[1], centroid[2], centroid[3]
	eucdist = math.sqrt(((x1 - X1) ** 2) + ((y1 - Y1) ** 2) + ((z1 - Z1) ** 2) + ((o1 - O1) ** 2))
	return float("{:.3f}".format(eucdist))

def make_clusters(final_dataset,initial_centroids):
	c1, c2 = [], []
	for h in range(len(final_dataset)):
		dist=[]
		for i in range(3):
			dist.append(euc_distance(initial_centroids[i], final_dataset[h]))
		c = dist.index(min(dist))
		if c == 0:
			c1.append(final_dataset[h])
		elif c == 1:
			c2.append(final_dataset[h])
	return [c1,c2]

def mean(inp):
	s =sum(inp)
	l = len(inp)
	return float("{:.3f}".format(s/l))

def new_centroids(list_of_clusters):
	new_centroid = []
	for clust in list_of_clusters:
		size = len(clust)
		l, m, n, h = [], [], [], []
		for i in range(size):
			l.append(clust[i][0])
			m.append(clust[i][1])
			n.append(clust[i][2])
			h.append(clust[i][3])
		new_centroid.append([mean(l),mean(m),mean(n),mean(h)])
	return new_centroid

def first_centroid(final_dataset):
	initial_centroids = random.sample(final_dataset, k=3)
	return initial_centroids

def scid(list_of_clusters, centroid):
	val = []
	for i in range(len(list_of_clusters)):
		clust = list_of_clusters[i]
		scid_val = 0
		for point in clust:
			scid_val += ((euc_distance(centroid[i], point))**2)
		val.append(scid_val)
	return list_of_clusters[val.index(max(val))]

def plot(list_of_clusters):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	coord = []
	for clust in list_of_clusters:
		size = len(clust)
		sepal_l, sepal_w, petal_l = [], [], []
		for i in range(size):
			sepal_l.append(clust[i][0])
			sepal_w.append(clust[i][1])
			petal_l.append(clust[i][2])
		coord.append([sepal_l,sepal_w,petal_l])


	ax.scatter(coord[0][0], coord[0][1], coord[0][2], c='r', marker='o')
	ax.scatter(coord[1][0], coord[1][1], coord[1][2], c='b', marker='o')
	ax.scatter(coord[2][0], coord[2][1], coord[2][2], c='g', marker='o')

	ax.set_xlabel('Sepal Length')
	ax.set_ylabel('Sepal Width')
	ax.set_zlabel('Petal Length')

	plt.show()

def main():
	data = dataset_creation()
	i = 0
	j = 1
	k = 3
	cent_old = first_centroid(data)
	new_cluster = []
	while len(new_cluster) != k:
		new_cluster = make_clusters(data,cent_old)
		new_cluster.append(make_clusters(scid(new_cluster,cent_old),first_centroid(scid(new_cluster,cent_old))))
	# while 1:
	# 	new_cluster= make_clusters(data,cent_old)
	# 	cent_new = new_centroids(new_cluster)
	# 	i+=1
	# 	if cent_new == cent_old:
	# 		break
	# 	cent_old = cent_new
	# scid_val = scid(new_cluster, cent_new)
	print(new_cluster)
	# print("The centroid for Cluster 1 is " + str(cent_new[0]))
	# print("The centroid for Cluster 2 is " + str(cent_new[1]))
	# print("The centroid for Cluster 3 is " + str(cent_new[2]))
	# print("The SCID value of the solution is " + str(scid_val))
	# print(str(i) + " iterations")
	plot(new_cluster)

if __name__ == '__main__':
	main()
# 3 iterations
# The centroid for Cluster 1 is [5.006, 3.418, 1.464, 0.244]
# The centroid for Cluster 2 is [6.85, 3.074, 5.742, 2.071]
# The centroid for Cluster 3 is [5.902, 2.748, 4.394, 1.434]
# The SCID value of the solution is 78.93191000000002


