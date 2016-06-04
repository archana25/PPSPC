from ClassFile import QuadInformation
import game_xml2bin
from ValidatingPolygon import validatingPolygon
import sys
from ParsingXmlFile import parsingXmlFile
from DataStructureFile import dataStructureFile
from DecompressBinaryFile import decompressBinaryFile
from xmlTops import xmlTops


xml_file = sys.argv[1]
log = sys.argv[2]
output = sys.argv[2]

doc_file = open(sys.argv[1],"r")
log_file = open(sys.argv[2],"w")

trafficInfoDictionary= parsingXmlFile(doc_file,log_file)

list1 =  trafficInfoDictionary["road"]
xmlTops(trafficInfoDictionary['road'])

validatingPolygon(trafficInfoDictionary['road'],log_file)

dataStructureFile(trafficInfoDictionary['road'])

game_xml2bin.compressFile('originalPickletrafficData.bin')

decompressBinaryFile(len(trafficInfoDictionary['road']))


