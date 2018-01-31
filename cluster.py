import csv
import numpy as np
from sklearn.cluster import KMeans
data_bowl=[]
clusters_bowl=[]
output_bowl=[]
data_bat=[]
clusters_bat=[]
output_bat=[]
with open('twenty20careerbowling.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	temp=[]
    	if(row[0] and row[4] and row[10]):
	    	temp=[row[0],row[4],row[10]]
	    	data_bowl.append(temp)
    	else:
    		if row[0] is 'NA':
    			temp.append('-1')
    		else:
    			temp.append(row[0])
    		if row[4] is 'NA':
    			temp.append('-1')
    		else:
    			temp.append(row[4])
    		if row[10] is 'NA':
    			temp.append('-1')
    		else:
    			temp.append(row[10])
    		data_bowl.append(temp)
with open('twenty20careerbatting.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	temp=[]
    	if(row[0]!='NA' and row[4]!='NA' and row[9]!='NA'):
	    	temp=[row[0],row[4],row[9]]
	    	data_bat.append(temp)
    	else:
    		if row[0]=='NA':
    			temp.append('-1')
    		else:
    			temp.append(row[0])
    		if row[4]=='NA':
    			temp.append('-1')
    		else:
    			temp.append(row[4])
    		if row[9]=='NA':
    			temp.append('-1')
    		else:
    			temp.append(row[9])
    		#print(temp)
    		data_bat.append(temp)

X=np.array(data_bowl)
rows=range(1,len(X))
#print(X[rows][:,[1,2]])
kmeans = KMeans(n_clusters=10, random_state=0).fit(X[rows][:,[1,2]])
print(len(kmeans.labels_))
clusters_bowl.append('Clusters')
for i in kmeans.labels_ :
	clusters_bowl.append(i+1)
#print(clusters)
Y=np.vstack((X[:,0],clusters_bowl))
for i in range(len(Y[0])):
	output_bowl.append([Y[0][i],Y[1][i]])
with open('bowl_clust.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output_bowl)
#print(data_bat)
X=np.array(data_bat)
rows=range(1,len(X))
#print(X[rows][:,[1,2]])
kmeans = KMeans(n_clusters=10, random_state=0).fit(X[rows][:,[1,2]])
print(len(kmeans.labels_))
clusters_bat.append('Clusters')
for i in kmeans.labels_ :
	clusters_bat.append(i+1)
#print(clusters)
Y=np.vstack((X[:,0],clusters_bat))
for i in range(len(Y[0])):
	output_bat.append([Y[0][i],Y[1][i]])
with open('bat_clust.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(output_bat)
