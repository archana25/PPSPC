
Project Topic :  Simulating Road Traffic

Group Info : 14206,14231,14301
		
Description : We have used Vornoi Diagrams to create input file. After generating input file, we are validating it. After validation, we are creating 		   output file. We are mainting log file (log.txt).

	Input :
		newXml.xml

	Output :
		Map.ps

	Validation :
		- Validation of number of quadpoint pair in each quad.
		- Validation of redudant quadpoint pair in each quad.
		- Validation of valid number of road boundaries.
		- Validation of connectivity of polygon.

	Run :
		python road_mapbackup.py newXml.xml log.txt
