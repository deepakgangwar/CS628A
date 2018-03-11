SHELL=/bin/bash
all: S10rM

S10rM: S10rM.c
	rand=$$((512+$$RANDOM%100)) && \
	gcc -fno-stack-protector -U_FORTIFY_SOURCE -mpreferred-stack-boundary=4 -w -m32 -DSUFFICIENT=$$rand -o $@ $< 

clean:
	rm -f S10rM
