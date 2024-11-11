.PHONY = all clean

CC = gcc
COMPILE_FLAGS = -g -O0 -fno-stack-protector -no-pie -z execstack # -m32
	# -g: default level of debug information
	# -O0: do not optimise (Optimisation level 0)
	# -fno-stack-protector: disable stack protectors (canaries(?))
	# -no-pie: disable position independent execution - disables relative paths for addresses
	# -z execstack: marks the stack as executable
	# -m32: compile as a 32 bit program

all: 7_RCE
apple: 7_RCE_apple


7_RCE:
	${CC} ${COMPILE_FLAGS} -m32 -o ./challenge RCE.c


7_RCE_apple:
	${CC} ${COMPILE_FLAGS} -o ./challenge RCE.c


clean:
	rm -rf ./challenge ./challenge.dSYM
