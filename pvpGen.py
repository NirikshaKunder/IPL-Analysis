import sys,os,yaml,shutil

pvpData={}
pVp={}
def processData(dic):
	innings1={}
	for i in dic["innings"][0]["1st innings"]["deliveries"]:
		innings1={**innings1,**i}
	for k,v in innings1.items():
		if 'wicket' in v.keys():
			key=(v["batsman"],v["bowler"],v["runs"]["total"],1)
		else:
			key=(v["batsman"],v["bowler"],v["runs"]["total"],0)
		if key in pvpData:
			pvpData[key]+=1
		else:
			pvpData[key]=1

	innings2={}
	if len(dic["innings"])>1:
		for i in dic["innings"][1]["2nd innings"]["deliveries"]:
			innings2={**innings2,**i}

		for k,v in innings2.items():
			if 'wicket' in v.keys():
				key=(v["batsman"],v["bowler"],v["runs"]["total"],1)
			else:
				key=(v["batsman"],v["bowler"],v["runs"]["total"],0)
			pvpKey=(v["batsman"],v["bowler"])
			if key in pvpData:
				pvpData[key]+=1
			else:
				pvpData[key]=1

def generatePVP():
	for k in sorted(pvpData):
		batsman,bowler,score,wickets=k
		key=(batsman,bowler)
		if key in pVp:
			pVp[key][score if score<=6 else 7]+=pvpData[k]
			if wickets == 1:
				pVp[key][8]+=pvpData[k]
		else:
			pVp[key]=[0 for i in range(9)]
			pVp[key][score if score<=6 else 7]+=pvpData[k]
			if wickets == 1:
				pVp[key][8]+=pvpData[k]
		

def main():
	sourceDir=os.path.join(os.path.dirname(__file__),sys.argv[1])
	opDir=os.path.join(os.path.dirname(__file__),sys.argv[2])
	if os.path.exists(opDir):
	    shutil.rmtree(opDir)
	os.makedirs(opDir)

	for root, dirs, filenames in os.walk(sourceDir):
	    for f in filenames:
	    	if f.endswith(".yaml"):
		        with open(os.path.join(sourceDir, f),"r") as stream:
		        	try:
		        		dic=yaml.load(stream)
		        		processData(dic)
		        		print("Processed ",f)

		        	except yaml.YAMLError as exc:
		        		print(exc)

	generatePVP()

	for k,v in sorted(pVp.items()):
		batsman,bowler=k
		fpath=os.path.join(opDir,"players.csv")
		total=0
		if not os.path.exists(fpath):
			with open(fpath ,"x") as f:
				f.write("BatsmanName,BowlerName,0s,1s,2s,3s,4s,5s,6s,extras,wickets,total_balls\n")

		with open(fpath,"a") as f:
			for i in range(8):
				total=total+int(v[i])
			s=','.join([str(i) for i in v])
			f.write(batsman+","+bowler+","+s+","+str(total)+"\n")


if __name__ == "__main__":
    if len(sys.argv[1:])==2:
    	main()
    else:
    	print("Usage(Requires Python 3.5+): python3 pvpGen.py <inputDir> <outputDir>")
