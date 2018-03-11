#include<stdio.h>
#include<string.h>
#include <unistd.h>
int setresuid(uid_t,uid_t,uid_t);
void setid(){
	uid_t eid = geteuid();
	setresuid(eid,eid,eid);
}
void biodata(){
	char info[SUFFICIENT];
	int c;
	for(c=0;c<5;c++){
		switch(c){
			case 0:
				printf("\nEnter Name: ");
				scanf("%s",info);
				if(strlen(info)>SUFFICIENT)
					return;				
				printf(info);
				break;
			case 1:
				printf("\nEnter Roll No: ");
				scanf("%s",info);
				if(strlen(info)>SUFFICIENT)
					return;
				printf(info);
				break;
			case 2:
				printf("\nEnter Programme: ");
				scanf("%s",info);
				if(strlen(info)>SUFFICIENT)
					return;
				printf(info);
				break;
			case 3:
				printf("\nEnter Department: ");
				scanf("%s",info);
				if(strlen(info)>SUFFICIENT)
					return;
				printf(info);
				break;
			case 4:
				printf("\nEnter Year: ");
				scanf("%s",info);
				if(strlen(info)>SUFFICIENT)
					return;
				printf(info);
				break;
		}								
	}	
	puts("\n!!!!Thank You!!!!\n");
}
int main(int argc,char *argv[]){
	setid();
	biodata();
	return 0;
}
