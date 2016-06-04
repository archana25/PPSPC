
def xmlTops(objectList):
	target = open("Map_road.ps",'w')
	temp_no = 0
	noOfQuads = len(objectList)
	target.write("%!PS\n\n1 setlinewidth\n\n")
	while(temp_no<noOfQuads):
		i=0
		coordinate= objectList[temp_no].attributeValues[1][i]
		target.write((str(coordinate[0]).strip('(,)')).replace(',','')+" moveto\n")
		for i in range(1,len(objectList[temp_no].attributeValues[1])):
			if type(objectList[temp_no].attributeValues[1][i]) != int:
					command = "lineto"
				
					cordinate= objectList[temp_no].attributeValues[1][i]
					print cordinate[0]
					target.write((str(cordinate[0]).strip('()')).replace(',','')+" "+command+" \n")
		target.write("\nclosepath\n");
		temp_no = temp_no+1

	target.write("\nstroke")
	target.close()

