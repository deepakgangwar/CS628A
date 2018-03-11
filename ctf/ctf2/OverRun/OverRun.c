#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/* This never gets called! */
char *arr;
int setresuid(uid_t,uid_t,uid_t);
void setid(){
	uid_t eid = geteuid();
	setresuid(eid,eid,eid);
}
void vuln(char *input){
    char buf[SUFFICIENT];
    strcpy(buf, input);
    
}


void get_flag()
{
 printf("\nFlag is Here\n");
 sleep(10);
 printf("\nOhh Sorry!\n");
}


void give_shell(){
    setid();
    system(arr);
}

int main(int argc, char **argv){
    printf("Welcome !\n");

    if (argc > 2) 
        {
        arr=argv[1];
        vuln(argv[2]);
        }
     
    return 0;
}



