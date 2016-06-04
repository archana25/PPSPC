
import pickle
import json
from ClassFile import QuadInformation

def decompressBinaryFile(noOfQuads):
	myfile = open("PickletrafficData.bin","rb")
	for i in range(0,noOfQuads):
		newList = pickle.load(myfile)
		print newList

	myfile.close()

