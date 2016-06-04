import pickle
import binascii
import struct

binFile = open("BinaryFile.bin","wb")

textFile = open("BinaryFile.txt",'w')

myint ="42"

binData = struct.pack(myint)
print binData
binFile.write(binData)
textFile.write(myint)

binFile.close()
textFile.close()
