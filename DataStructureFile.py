import pickle
import json
from ClassFile import QuadInformation


def dataStructureFile(objectList):
	noOfQuads = len(objectList)
	myfile = open("PickletrafficData.bin","wb")
	originalMyfile = open("originalPickletrafficData.bin","wb")
	for i in range(0,noOfQuads):
		json.dump(objectList[i].attributeValues,originalMyfile)
		pickle.dump(objectList[i].attributeValues,myfile)

	originalMyfile.close()
		
	myfile.close()

