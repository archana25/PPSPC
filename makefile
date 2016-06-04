
genroad: voronoi_main.o VoronoiDiagramGenerator.o getLines.o
	g++ -g -o genroad voronoi_main.o VoronoiDiagramGenerator.o getLines.o

voronoi_main.o: voronoi_main.cpp headerFile.h
	g++ -g -c voronoi_main.cpp

VoronoiDiagramGenerator.o: VoronoiDiagramGenerator.cpp headerFile.h
	g++ -g -c VoronoiDiagramGenerator.cpp 

getLines.o: getLines.cpp headerFile.h
	g++ -g -c getLines.cpp


