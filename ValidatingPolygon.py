from ClassFile import QuadInformation


def validatingPolygon(objectList,log_file):
		j = 0
		groupDictionary = {}
		group1 = []
		group2 = []
		group3 = []
		group4 = []	
		while(j<len(objectList)):
			i=0
			count = 0
			tempList = []
			while i<4:
				tupleList =[] 
				if objectList[j].attributeValues[1][i][1] == 0:
					count = count+1
					if i+1 ==4:
						tupleList.append(objectList[j].attributeValues[1][i][0])
						tupleList.append(objectList[j].attributeValues[1][0][0])

					
					else:
						tupleList.append(objectList[j].attributeValues[1][i][0])
						tupleList.append(objectList[j].attributeValues[1][i+1][0])
					if count == 1 :
						tempList.append(objectList[j].attributeValues[0])
						tempList.append(tupleList)
					if count>1:
						tempList.append(tupleList)
				i = i+1
			if count ==1:
				group1.append(tempList)
			elif count ==2:
				group2.append(tempList)
			elif count ==3:
				group3.append(tempList)

			else:
				group4.append(tempList)
				
				
			j=j+1	
		
		groupDictionary['1'] = group1	
		groupDictionary['2'] = group2	
		groupDictionary['3'] = group3	
		groupDictionary['4'] = group4	
		
			
		for i in range(1,5):
			for j in range(0,len(groupDictionary[str(i)])):
				connectionList = []
				for k in range(1,len(groupDictionary[str(i)][j])):
					connectedQuad = checkConnectivity(groupDictionary[str(i)][j][0],groupDictionary[str(i)][j][k],groupDictionary,log_file) 
					connectionList.append(connectedQuad)
				objectList[groupDictionary[str(i)][j][0]-1].attributeValues.append(connectionList)




		log_file.write("Polygon has been verified for it's connectivity......\t\t\t\tPASS\n")	

def checkConnectivity(primaryKey,vertexList,groupDictionary,log_file):
	connectionList = []
	for i in range(1,5):
		for j in range(0,len(groupDictionary[str(i)])):
			for k in range(1,len(groupDictionary[str(i)][j])):
				if vertexList[0] == groupDictionary[str(i)][j][k][0] or vertexList[0] == groupDictionary[str(i)][j][k][1]:
					if vertexList[1] == groupDictionary[str(i)][j][k][0] or vertexList[1] == groupDictionary[str(i)][j][k][1]:
						if primaryKey != groupDictionary[str(i)][j][0]:
							connectionList.append(groupDictionary[str(i)][j][0])
						
							
	
	if len(connectionList)>1:
		log_file.write("Error in Connection!!")
		print "ERROR!!"
		exit()
		
	if len(connectionList)==0:
		print "ERROR"
		log_file.write("Polygon has been verified for it's connectivity......\t\t\t\tFAILED  Problem with edge %s\n" %(vertexList))	
		exit()
	else:
		return connectionList[0]
					


