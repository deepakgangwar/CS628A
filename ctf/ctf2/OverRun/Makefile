SHELL=/bin/bash
all: OverRun

OverRun: OverRun.c
	rand=$$((16+$$RANDOM%20)) && \
	gcc -fno-stack-protector -U_FORTIFY_SOURCE -mpreferred-stack-boundary=4 -w -m32 -DSUFFICIENT=$$rand -o $@ $< 

clean:
	rm -f OverRun
