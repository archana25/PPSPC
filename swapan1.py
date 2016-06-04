from ClassFile import QuadInformation
import xmltodict


def parsingXmlFile(doc_file,log_file):
	objectList = []
	doc = doc_file.read()

	matter = xmltodict.parse(doc)

	
	quadLimit = 4
	quads = matter['road']['quads']
#	bikes = matter['road']['bikes']
#	trucks = matter['road']['trucks']
#	cars = matter['road']['cars']
	trafficInfoDictionary={}
	temp_no =len(quads)
	mutant = 1
	while(temp_no):
		temp_list = []
		temp_list_coordinate = []
		points = quads['quad'+str(mutant)]['quadpointpair']
	#	boolSignal  = quads['quad'+str(mutant)]['@signal']
	#	speedLimit = quads['quad'+str(mutant)]['@speedLimit']
	#	boolOneWay = quads['quad'+str(mutant)]['@oneway']
		for i in range(1,len(points)+1):
			coordinate = points[i-1].split()
			print coordinate
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
#		temp_list.append(int(boolSignal))
#		temp_list.append(int(speedLimit))
#		temp_list.append(int(boolOneWay))
		temp_list = [mutant]+temp_list
		objectList.append(QuadInformation(temp_list))
		temp_no = temp_no-1
		mutant = mutant+1


	log_file.write("Each quadrant has been verified for redundant coordinate.......\t\t\tPASS\n")
	log_file.write("Each quadrant has been verified for valid no of edges.......\t\t\tPASS\n")
	log_file.write("Each quadrant has been verified for valid no of road boundaries.......\t\tPASS\n")
	trafficInfoDictionary["road"] = objectList
#	for i in range(0,3):
#		if i==0:
#			vehicle = cars
#			element = 'car'
#		elif i==1:
#			vehicle = trucks
#			element = 'truck'
#		else:
#			vehicle = bikes
#			element = 'bike'
#		mutant = 1
#		temp_no = len(vehicle)-2
#		print temp_no
#		carList=[]
#		dimension  =str(vehicle['@dimension'])
#		bgcolor = str(vehicle['@bgcolor'])
#		while(temp_no):
#			tempListOfCoordinates =[]
#			car = vehicle[element+str(mutant)]['quadpointpair']
#			for i in range(0,len(car)):
#				coordinate = car[i].split()
#				tempListOfCoordinates.append(eval(str(coordinate[1])))
#			carList.append(tempListOfCoordinates)
#			mutant = mutant+1
#			temp_no = temp_no -1
#		carList.append(dimension)
#		carList.append(bgcolor)
#		trafficInfoDictionary[element] = carList

#		return trafficInfoDictionary
		
	
