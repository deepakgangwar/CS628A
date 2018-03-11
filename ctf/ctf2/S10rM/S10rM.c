#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int target;

void hello()
{
 uid_t eid = geteuid();
 setresuid(eid,eid,eid);
 printf("Get your Flag Now\n");
 system("cat flag.txt");
 _exit(1);
}

void vuln()
{
 char buffer[SUFFICIENT];

 fgets(buffer, sizeof(buffer), stdin);

 printf(buffer);

 exit(1); 
}

int main(int argc, char **argv)
{
 vuln();
}
