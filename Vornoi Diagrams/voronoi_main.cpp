/*
* The author of this software is Shane O'Sullivan.  
* Permission to use, copy, modify, and distribute this software for any
* purpose without fee is hereby granted, provided that this entire notice
* is included in all copies of any software which is or includes a copy
* or modification of this software and in all copies of the supporting
* documentation for such software.
* THIS SOFTWARE IS BEING PROVIDED "AS IS", WITHOUT ANY EXPRESS OR IMPLIED
* WARRANTY.  IN PARTICULAR, NEITHER THE AUTHORS NOR AT&T MAKE ANY
* REPRESENTATION OR WARRANTY OF ANY KIND CONCERNING THE MERCHANTABILITY
* OF THIS SOFTWARE OR ITS FITNESS FOR ANY PARTICULAR PURPOSE.
*/



#include <stdio.h>
#include <search.h>
#include <malloc.h>
#include "VoronoiDiagramGenerator.h"


int main(int argc,char **argv) 
{	
  /*
  float xValues[4] = {22,17,4,22};
  float yValues[4] = {9,31,13,5};
  */
  
	int limit,j=2;
  FILE *fp;
  fp = fopen("Name.xml","w");
	
	
  float *xValues,*yValues ;
	limit = atoi(argv[1]);
	xValues = (float*)malloc(sizeof(float)*limit);
	yValues = (float*)malloc(sizeof(float)*limit);
	for(int i=0;i<limit;i++)
		xValues[i] = atof(argv[j++]);

	for(int i=0;i<limit;i++)
		yValues[i] = atof(argv[j++]);

	
		
  	
	
	printf("%s",argv[1]); 	
	int count = (atoi(argv[1]));
	printf("COUNT:%d",count);
	int i=1,no,lineC=0,pointC=0;
	no = 12;

	VoronoiDiagramGenerator vdg;
	vdg.generateVoronoi(xValues,yValues,count, -500,500,-500,500,3);
		

	vdg.resetIterator();

	float x1,y1,x2,y2;

	fprintf(fp,"%s","<?xml version=\"1.0\" encoding=\"ISO-8859-15\"?>");
	fprintf(fp,"%s","\n<road>\n\t<quads>");
	
/*	printf("\n-------------------------------\n");*/
	while(vdg.getNext(x1,y1,x2,y2))
	{
		printf("%d %d -> %d %d \n",x1,y1,x2,y2);
		/*if(lineC%2==0)
		{	
		fprintf(fp,"\n\t\t<quad%d>",i);
		lineC=0;
		pointC=0;
		fprintf(fp,"\n\t\t\t<quadpointpair>(");
		fprintf(fp,"%f",x1);
		fprintf(fp,",");
		fprintf(fp,"%f",y1);
		
		fprintf(fp,")");
			pointC++;
		fprintf(fp,"</quadpointpair>");
		fprintf(fp,"\n\t\t\t<quadpointpair>(");
		fprintf(fp,"%f",x2);
		fprintf(fp,",");
		fprintf(fp,"%f",y2);
		
		fprintf(fp,")");
		fprintf(fp,"</quadpointpair>");
		pointC++;
		lineC++;

		}
		else{
		fprintf(fp,"\n\t\t\t<quadpointpair>(");
		fprintf(fp,"%f",x1);
		fprintf(fp,",");
		fprintf(fp,"%f",y1);
		
		fprintf(fp,")");
			pointC++;
		fprintf(fp,"</quadpointpair>");
		fprintf(fp,"\n\t\t\t<quadpointpair>(");
		fprintf(fp,"%f",x2);
		fprintf(fp,",");
		fprintf(fp,"%f",y2);
		
		fprintf(fp,")");
		fprintf(fp,"</quadpointpair>");
		fprintf(fp,"\n\t\t</quad%d>",i);
		i++;
		pointC++;
		lineC++;
		}*/
	}
		
	if(pointC != 4 )
		fprintf(fp,"\n\t\t</quad%d>",i);

	fprintf(fp,"%s","\n\t</quads>\n</road>");
	fclose(fp);
	return 0;

	
}
