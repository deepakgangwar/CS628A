SHELL=/bin/bash
all: Absent_Minded

Absent_Minded: Absent_Minded.c
	gcc -U_FORTIFY_SOURCE -mpreferred-stack-boundary=4 -w -m32 -o $@ $< 

clean:
	rm -f Absent_Minded

