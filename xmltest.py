import xmltodict

with open('xml_file.xml') as fd:
  obj = xmltodict.parse(fd.read())
  print '=================================='
  max_range = int(obj['road']['quads']['@has'])
  quadData  = obj['road']['quads']
  print '=================================='
  for i in range(1,max_range):
	quadPoints = quadData['quad'+str(i)]['quadpointpair']
	roadPoints = quadData['quad'+str(i)]['roadBoundaries']
	max_coordinates = len(quadPoints)
	for j in range(0,max_coordinates):
		if(j==0):
			print type(quadPoints[j])	
			print str.split()
			print str
  		print '=================================='
