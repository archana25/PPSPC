import xmltodict
from ClassFile import QuadInformation
import pickle
import json
from xmlTops import xmlToPS
import game_xml2bin
from ValidatingPolygon import validatingPolygon


objectList = []

doc_file = open("Name.xml")

doc = doc_file.read()

matter = xmltodict.parse(doc)

noOfQuads = len(matter['road']['quads'])-1
print noOfQuads

quads = matter['road']['quads']
temp_no = noOfQuads
mutant = 1
while(temp_no):
	temp_list = []
	temp_list_coordinate = []
	points = quads['quad'+str(mutant)]['quadpointpair']
	for i in range(1,len(points)+1):
		coordinate = points[i-1].split()
		temp_list_coordinate.append(eval(coordinate[0]))
	if(len(temp_list_coordinate) != 4):
		print "Incorrect number of coordinates in quadrant no %s!!" %(mutant)
		break
	temp_list.append(temp_list_coordinate)
	temp_list = [mutant]+temp_list
	objectList.append(QuadInformation(temp_list))
	temp_no = temp_no-1
	mutant = mutant+1

xmlToPS(objectList)

myfile = open("PickletrafficData.bin","wb")
originalMyfile = open("originalPickletrafficData.bin","wb")
for i in range(0,noOfQuads):
	json.dump(objectList[i].attributeValues,originalMyfile)
	pickle.dump(objectList[i].attributeValues,myfile)

originalMyfile.close()
	
myfile.close()

myfile = open("PickletrafficData.bin","rb")
for i in range(0,noOfQuads):
	newList = pickle.load(myfile)


game_xml2bin.compressFile('originalPickletrafficData.bin')

validatingPolygon(objectList)
