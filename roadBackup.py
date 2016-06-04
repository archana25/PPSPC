import xmltodict
from array import * 


doc_file = open("xml_file.xml")

doc = doc_file.read()

matter = xmltodict.parse(doc)

unicode_no = len(matter['road']['quads'])
no = int(unicode_no)
quads = matter['road']['quads']
temp_no = no
full_list = []
k=1
while(temp_no):
	temp_list = []
	temp_list_coordinate = []
	points = quads['quad'+str(k)]['quadpointpair']


	print type(points[2])
	for i in range(1,len(points)+1):
		coor = str(points[i-1]).split()
		print coor
		temp_list_coordinate.append(eval(coor[1]))
	road= list(eval((quads['quad'+str(k)]['roadBoundaries'])))
	temp_list = zip(temp_list_coordinate,road)
	temp_no = temp_no-1
	k = k+1
	full_list.append(temp_list)

print full_list[0][1]
target = open("road_map.ps",'w')
temp_no = 0
target.write("%!PS\n\n1 setlinewidth\n\n")
while(temp_no<no):
	first_coordinate= full_list[temp_no][0][0]
	target.write((str(first_coordinate).strip('(,)')).replace(',',' ')+" moveto\n")
	for i in range(1,len(full_list[temp_no])):
		if full_list[temp_no][i-1][1]==1:
			command = "lineto"
		else:
			command = "moveto"
		
		coordinate= full_list[temp_no][i][0]
		target.write((str(coordinate).strip('()')).replace(',',' ')+ "  "+command + " \n")
	if full_list[temp_no][i][1]==1 :
		target.write((str(coordinate).strip('()')).replace(',',' ')+ "  moveto" + " \n")
		target.write((str(first_coordinate).strip('()')).replace(',',' ')+ "  lineto" + " \n")
	else:
		print "CRAP"
		
	temp_no = temp_no+1
target.write("0 setgray\nstroke\n")
target.close()

