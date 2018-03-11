SHELL=/bin/bash
all: GameOfThrones

GameOfThrones: GameOfThrones.c
	rand=$$((200+8*$$RANDOM%20)) && \
	gcc -fno-stack-protector -U_FORTIFY_SOURCE -mpreferred-stack-boundary=2 -m32 -DSUFFICIENT=$$rand -o $@ $< 

clean:
	rm -f GameOfThrones

