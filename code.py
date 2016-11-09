import sys
from sets import Set
from itertools import chain, combinations

configFile={}
inputDataDict={}				#dictionary for evry otem ocurring in which transaction
generalDict={}

#totalFrequentItemSet=0

def readFromConfigFile(fname):
	file_iter = open(fname, 'rU')
	for line in file_iter:
		line = line[:-1].split(',')
		configFile[line[0]]=line[1]

def readInputFile(fname):
	file_iter = open(fname, 'rU')
	counter=1
	for line in file_iter:
		line = line[:-1].split(',')
		#print line
		for item in line:
			if(tuple([item],) not in inputDataDict):
				inputDataDict[tuple([item],)]=Set([counter])
			else:
				inputDataDict[tuple([item],)].add(counter)	
		counter=counter+1
	return counter-1	
def getItemSet1(length,inputData,totalFrequentItemSet):
	tempitemset1={}
	itemSet = []
	for key, value in inputData.items():
		# print key,value,len(value)
		if(len(value) >= support ):
			tempitemset1[key]=value
			itemSet.append(key)
			# itemSet.add(frozenset([tuple([key],)]))
	generalDict[length]=tempitemset1
	totalFrequentItemSet=totalFrequentItemSet+len(tempitemset1)
	#print len(tempitemset1)		
	# for key,value in tempitemset1.items():
	# 	print key,value
	return itemSet,totalFrequentItemSet

def getAllSubsets(itemSet,length):					#generate all subsets
	pairs = combinations(itemSet, length)
	return pairs

def runAprioriAlgo(totalFrequentItemSet):
	itemSet,totalFrequentItemSet=getItemSet1(1,inputDataDict,totalFrequentItemSet)			#get frequent itemset of size 1
	# for item in itemSet:
	# 	print item

	allsubsets=getAllSubsets(itemSet,2)
	tempDict={}
	for item in allsubsets:
		intersectSet=inputDataDict[item[0]].intersection(inputDataDict[item[1]])
		if len(intersectSet) >=support :
			tempDict[item]=inputDataDict[item[0]].intersection(inputDataDict[item[1]])
			# print item[0],item[1]
			# print inputDataDict[item[0]].intersection(inputDataDict[item[1]])
	#print len(tempDict)			
	totalFrequentItemSet=totalFrequentItemSet+len(tempDict)		
	generalDict[2]=tempDict
	globalCount=3
	while generalDict[globalCount-1] !={}:
		counter=0
		temporaryDict={}
		for key1 in generalDict[globalCount-1].keys():
			counter=counter+1
			# print "key1= ",key1
			for key2 in generalDict[globalCount-1].keys()[counter:]:
				# print "key2= ",key2
				# print cmp(key1[:-1],key2[:-1])
				if cmp(key1[:-1],key2[:-1])==0 and key1[-1]!=key2[-1]:
					# print "Keys equal"
					tempKey=key1+(key2[-1],)
					tempDict=generalDict[globalCount-1]
					# print tempKey
					# print tempDict
					tempDict1=tempDict[key1]
					intersectSet=tempDict1.intersection(inputDataDict[key2[-1]])
					if len(intersectSet) >=support:
						temporaryDict[tempKey]=intersectSet
		generalDict[globalCount]=temporaryDict
		#print len(temporaryDict)
		totalFrequentItemSet=totalFrequentItemSet+len(temporaryDict)
		globalCount=globalCount+1
	return totalFrequentItemSet

def generateSubsets(lastLevelKeys):
	# print last	LevelKeys
	# print "dsfdffsdgnglsn"
	asso = Set()
	for i in range(1,len(lastLevelKeys)):
			asso = asso.union(Set(combinations(lastLevelKeys,i)))
	# for i in asso:
	# 	print i		
	return asso

def getAssociations(lastLevelKeys):
	subsets=generateSubsets(lastLevelKeys)
	# print subsets
	
	confidence=float(configFile["confidence"])
	tempDict=generalDict[len(generalDict)-1]
	numerator=len(tempDict[lastLevelKeys])
	asso_rules=[]
	asso_key = Set(lastLevelKeys)
	for item in subsets:
		# print item,len(item)
		tempDict=generalDict[len(item)]
		# print tempDict
		if(len(item)==1):

			if item[0] in tempDict:
				dinominator=len(tempDict[item[0]])
				# print numerator,dinominator
				if(float(numerator/dinominator) >= confidence):
					# print item[0], "=>" ,lastLevelKeys	
					temp=""
					for k in item[0]:
						temp=temp+str(k)+","
					temp=temp+"=>"
					for k in asso_key.difference(item):
						temp=temp+","+str(k)
					asso_rules.append(temp)

		else:
			if item in tempDict:
				dinominator=len(tempDict[item])
				# print numerator,dinominator
				if(float(numerator/dinominator) >= confidence):
					# print item, "=>" ,lastLevelKeys
					temp=""
					for k in item:
							temp=temp+str(k)+","
					temp=temp+"=>"
					for k in asso_key.difference(item):
						temp=temp+","+str(k)
					asso_rules.append(temp)	
	
	return asso_rules	
readFromConfigFile("config.csv")
numOfTransaction=readInputFile(configFile["input"])
#print numOfTransaction
support=float(configFile["support"])*numOfTransaction
#print support
totalFrequentItemSet=0
totalFrequentItemSet=runAprioriAlgo(0)


file3 = open(configFile["output"],"w+")
file3.write(str(totalFrequentItemSet)+"\n")
print totalFrequentItemSet
frequentItemSet=[]

for key,value in generalDict.items():
	for key1,val in generalDict[key].items():
		print key1
		temp=""
		for a in key1:
			temp=temp+str(a)+","
		temp=temp[:-1]	
		file3.write(temp+"\n")
		# file3.write(str(key1)+"\n")

lastLevelKeys=generalDict[len(generalDict)-1].keys()
# print lastLevelKeys
if(configFile["flag"]=="1"):
	# print "getAssociations Rules"
	allAssociationRules=[]
	asso_count=0
	for item in lastLevelKeys:
		allRules=getAssociations(item)
		asso_count=asso_count+len(allRules)
		allAssociationRules.append(allRules)
	print asso_count
	file3.write(str(asso_count)+"\n")
	for item in allAssociationRules:
		for i in item:
			print i
			temp=""
			for j in i:
				temp=temp+j+","
			temp=temp[:-1]	
			file3.write(temp+"\n")	
