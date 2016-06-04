from ClassFile import QuadInformation
import zlib

def compressFile(fileName):
	with open(fileName,'r') as file:
		str_object1 = file.read()
		str_object2 = zlib.compress(str_object1,9)
		f = open('originalcompressedFile','wb')
		f.write(str_object2)
	f.close()
		
	with open('compressedFile','r') as file:
		str_object1 = file.read()
		str_object2 = zlib.decompress(str_object1)
		f = open('DecompressedFile','wb')
		f.write(str_object2)
	f.close()
