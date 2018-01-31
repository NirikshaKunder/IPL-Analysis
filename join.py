import csv
from random import randint
bat_clust={}
bowl_clust={}
players=[]
with open('bat_clust.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	bat_clust[row[0]]=row[1]
with open('bowl_clust.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	bowl_clust[row[0]]=row[1]
#print(bat_clust)
#print(bowl_clust)
with open('PVP/players.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
    	players.append(list(row))
players[0].append('bat_clust')
players[0].append('bowl_clust')
for i in range(1,len(players)):
	if(players[i][0] in bat_clust):
		players[i].append(bat_clust[players[i][0]])
	else:
		bat_clust[players[i][0]]=randint(1,10)
		players[i].append(bat_clust[players[i][0]])
	if(players[i][1] in bowl_clust):
		players[i].append(bowl_clust[players[i][1]])
	else:
		bowl_clust[players[i][1]]=randint(1,10)
		players[i].append(bowl_clust[players[i][1]])
with open('players_clust.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(players)
