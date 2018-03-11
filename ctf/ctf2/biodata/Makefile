SHELL=/bin/bash
all: biodata

biodata: biodata.c
	rand=$$((16+$$RANDOM%20)) && \
	gcc -fno-stack-protector -U_FORTIFY_SOURCE -mpreferred-stack-boundary=4 -w -Wformat-security -m32 -DSUFFICIENT=$$rand -o $@ $< 

clean:
	rm -f biodata

