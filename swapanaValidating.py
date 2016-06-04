from ClassFile import QuadInformation


def validatingPolygon(objectList):
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
		
			
		print group2




