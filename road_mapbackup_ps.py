import xmltodict
from ClassFile import QuadInformation
import json

objectList = []

doc_file = open("Name.xml")

doc = doc_file.read()

matter = xmltodict.parse(doc)

unicode_no = matter['road']['quads']['@has']
noOfQuads = 8
quads = matter['road']['quads']
temp_no = noOfQuads
mutant = 1
while(temp_no):
	temp_list = []
	temp_list_coordinate = []
	points = quads['quad'+str(mutant)]['quadpointpair']
	boolSignal  = quads['quad'+str(mutant)]['@signal']
	speedLimit = quads['quad'+str(mutant)]['@speedLimit']
	boolOneWay = quads['quad'+str(mutant)]['@oneway']
	for i in range(1,len(points)+1):
		coordinate = points[i-1].split()
		temp_list_coordinate.append(eval(coordinate[1]))
	road= list(eval((quads['quad'+str(mutant)]['roadBoundaries'])))
	temp_listOfCoordinates = zip(temp_list_coordinate,road)
	if(len(temp_listOfCoordinates) != 4):
		print "Incorrect number of coordinates in quadrant no %s!!" %(mutant-20)
		print len(temp_listOfCoordinates)
		break
	temp_list.append(temp_listOfCoordinates)
	temp_list.append(int(boolSignal))
	temp_list.append(int(speedLimit))
	temp_list.append(int(boolOneWay))
	temp_list = [mutant]+temp_list
	objectList.append(QuadInformation(temp_list))
	temp_no = temp_no-1
	mutant = mutant+1


target = open("road_map1.ps",'w')
temp_no = 0
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
