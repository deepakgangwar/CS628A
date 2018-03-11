#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
int setresuid(uid_t,uid_t,uid_t);
void setid(){
	uid_t eid = geteuid();
	setresuid(eid,eid,eid);
}

void read_flag()
{
    system("/bin/cat flag.txt");
}

void _strncpy(char *out, int outl, char *in)
{
  int i, len;

  len = strlen(in);
  if (len > outl)
    len = outl;

  for (i = 0; i <= len; i++)
    out[i] = in[i];
}

void wildlings(char *arg)
{
  char buf[SUFFICIENT];
  _strncpy(buf, sizeof buf, arg);
}

void crows(char *argv[])
{
  int *ptr;
  int var = 0;
  ptr = &var;
  wildlings(argv[1]);
  *ptr = var;
  _exit(0);
 
}

int main(int argc, char *argv[])
{
    setid();
    if (argc != 2)
    {
        fprintf(stderr, "Enter the argument\n");
        exit(1);
    }
    getchar();
    crows(argv);
    return 0;
}
