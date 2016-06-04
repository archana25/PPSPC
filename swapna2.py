
def xmlToPS(objectList):
	target = open("Map_road.ps",'w')
	temp_no = 0
	noOfQuads = len(objectList)
	target.write("%!PS\n\n1 setlinewidth\n\n")
	while(temp_no<noOfQuads):
		coordinate= objectList[temp_no].attributeValues[1][0][0]
		target.write((str(coordinate).strip('(,)')).replace(',','')+" moveto\n")
		for i in range(1,len(objectList[temp_no].attributeValues[1])):
			if type(objectList[temp_no].attributeValues[1][i]) != int:
				if objectList[temp_no].attributeValues[1][i-1][1] == 1:
					command = "lineto"
					cordinate= objectList[temp_no].attributeValues[1][i][0]
					target.write((str(cordinate).strip('()')).replace(',','')+" "+command+" \n")
					target.write((str(cordinate).strip('()')).replace(',','')+" "+" moveto"+" \n")

				else:
					command = "moveto"
					cordinate= objectList[temp_no].attributeValues[1][i][0]
					target.write((str(cordinate).strip('()')).replace(',','')+" "+command+" \n")

				if i == 3 and objectList[temp_no].attributeValues[1][i][1] == 1:
					target.write((str(coordinate).strip('(,)')).replace(',','')+" lineto\n")
		temp_no = temp_no+1

	target.write("\nclosepath\n")
	target.write("\nstroke")
	target.close()

	target = open("road_map1.ps",'a+')
	target.close()
