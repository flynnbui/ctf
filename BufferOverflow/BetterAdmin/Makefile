.PHONY = all clean

CC = gcc
COMPILE_FLAGS = -g -O0 -fno-stack-protector -no-pie # -m32
	# -g: default level of debug information
	# -O0: do not optimise (Optimisation level 0)
	# -fno-stack-protector: disable stack protectors (canaries(?))
	# -no-pie: disable position independent execution - disables relative paths for addresses
	# -m32: compile as a 32 bit program

all: 2_betterAdmin
apple: 2_betterAdmin_apple


2_betterAdmin:
	${CC} ${COMPILE_FLAGS} -m32 -o ./challenge betterAdmin.c


2_betterAdmin_apple:
	${CC} ${COMPILE_FLAGS} -o ./challenge betterAdmin.c


clean:
	rm -rf ./challenge ./challenge.dSYM
