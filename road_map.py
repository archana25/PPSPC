import xmltodict
from ClassFile import QuadInformation
import pickle
import json
import game_xml2bin
from ValidatingPolygon import validatingPolygon
import sys


xml_file = sys.argv[1]
log = sys.argv[2]
output = sys.argv[2]
objectList = []

doc_file = open(sys.argv[1],"r")
log_file = open(sys.argv[2],"w")

doc = doc_file.read()

matter = xmltodict.parse(doc)

noOfQuads = len(matter['road']['quads'])
quadLimit = 4
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
		if len(temp_list_coordinate)>len(set(temp_list_coordinate)):
			print "ERROR"
			log_file.write("Each quadrant has been verified for redundant coordinate.......\t\tFAILED for quadrant%s\n" %(mutant))
			exit()
			
	road= list(eval((quads['quad'+str(mutant)]['roadBoundaries'])))
	if len(road)!=quadLimit:
		print "ERROR"
		log_file.write("Each quadrant has been verified for valid no of road boundaries.......\t\tFAILED for quadrant%s\n" %(mutant))
		exit()
	temp_listOfCoordinates = zip(temp_list_coordinate,road)
	if(len(temp_listOfCoordinates) != quadLimit):
		print "ERROR"
		log_file.write("Each quadrant has been verified for valid no of edges.......\t\tFAILED for quadrant%s\n" %(mutant))
		exit()
	temp_list.append(temp_listOfCoordinates)
	temp_list.append(int(boolSignal))
	temp_list.append(int(speedLimit))
	temp_list.append(int(boolOneWay))
	temp_list = [mutant]+temp_list
	objectList.append(QuadInformation(temp_list))
	temp_no = temp_no-1
	mutant = mutant+1


log_file.write("Each quadrant has been verified for redundant coordinate.......\t\t\tPASS\n")
log_file.write("Each quadrant has been verified for valid no of edges.......\t\t\tPASS\n")
log_file.write("Each quadrant has been verified for valid no of road boundaries.......\t\tPASS\n")
validatingPolygon(objectList,log_file)

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
	print newList


game_xml2bin.compressFile('originalPickletrafficData.bin')

