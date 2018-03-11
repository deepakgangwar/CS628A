#include <stdlib.h>
#include <stdio.h>

int setresuid(uid_t,uid_t,uid_t);
void setid(){
	uid_t eid = geteuid();
	setresuid(eid,eid,eid);
}
void get_flag();

int main(int argc, char **argv)
{
   char *p=getenv("USER");
   if(p==NULL) return EXIT_FAILURE;
  if(getenv(p)!=NULL)
{
   //printf("Environment variable value is %s\n",getenv(p));
   get_flag();
}
else
{
  printf("Bye!\n");
}

}


void  get_flag()
   {
     char *ctf_flag=getenv("HACK");
    if(getenv("HACK")!=NULL)
    {
	setid();
	system(ctf_flag);
    }
    else
     printf("Something is missing\n");

   }




