
#include"headerFile.h"


int getLines(char *filename){

FILE *fp,*fpXml;
float x1,y1,x2,y2;
float newX1,newY1,newX2,newY2,newX3,newY3,newX4,newY4;
int i=1;
float dx,dy,perpendicularX,perpendicularY,distance,width=10;
fpXml =  fopen("Name.xml","w+");
fp = fopen(filename,"r");
if(fp==NULL)
	fprintf(stderr,"Error in opening file");

fprintf(fpXml,"%s","<?xml version=\"1.0\" encoding=\"ISO-8859-15\"?>");
	fprintf(fpXml,"%s","\n<road>\n\t<quads>");
	

while(fscanf(fp,"%f%f%f%f",&x1,&y1,&x2,&y2)==4)
{
	dx= x2-x1;
	dy= y2 - y1;
	
	perpendicularX = dy;
	perpendicularY = (-dx);
	
	distance = sqrt(pow(perpendicularX,2) + pow(perpendicularY,2));
	
	perpendicularX = perpendicularX/distance;
	perpendicularY = perpendicularY/distance;

	perpendicularX = perpendicularX * width;
	perpendicularY = perpendicularY * width;

	
	newX1 = x2 + perpendicularX;   
	newY1 = y2 + perpendicularY;   
			
	newX2 = x1 + perpendicularX;   
	newY2 = y2 + perpendicularY;   
	newX3 = x2 - perpendicularX;   
	newY3 = y2 - perpendicularY;   
			
	newX4 = x1 - perpendicularX;   
	newY4 = y2 - perpendicularY;   


	printf("New Points:\n%f,%f--->%f,%f",newX1,newY1,newX2,newY2);

	fprintf(fpXml,"\n\t\t<quad%d>",i);
		fprintf(fpXml,"\n\t\t\t<quadpointpair>%d  (",i);
		fprintf(fpXml,"%f",newX1);
		fprintf(fpXml,",");
		fprintf(fpXml,"%f",newY1);
		
		fprintf(fpXml,")");
	
		fprintf(fpXml,"</quadpointpair>");
		fprintf(fpXml,"\n\t\t\t<quadpointpair>%d  (",i);
		fprintf(fpXml,"%f",newX2);
		fprintf(fpXml,",");
		fprintf(fpXml,"%f",newY2);
		
		fprintf(fpXml,")");
		fprintf(fpXml,"</quadpointpair>");
		fprintf(fpXml,"\n\t\t\t<quadpointpair>%d  (",i);
	
		fprintf(fpXml,"%f",newX4);
		fprintf(fpXml,",");
		fprintf(fpXml,"%f",newY4);
		
		fprintf(fpXml,")");
	
		fprintf(fpXml,"</quadpointpair>");
		fprintf(fpXml,"\n\t\t\t<quadpointpair>%d  (",i);
		fprintf(fpXml,"%f",newX3);
		fprintf(fpXml,",");
		fprintf(fpXml,"%f",newY3);
		
		fprintf(fpXml,")");
		fprintf(fpXml,"</quadpointpair>");
		fprintf(fpXml,"\n\n\t<roadBoundaries> (1,1,1,1)  </roadBoundaries>");
		fprintf(fpXml,"\n\t\t</quad%d>",i);
		i++;




}
	
	fprintf(fpXml,"\n\n</quads>\n</road>");
return 0;
}
