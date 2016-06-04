
#include<stdio.h>

char myno[7] = "fefrefre";
FILE *fileBi = fopen("input.bin","wb");

fwrite(myno,7,fileBi);

fileBi.close();
