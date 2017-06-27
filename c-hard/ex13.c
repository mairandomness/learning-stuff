#include <stdio.h>

int main(int argc, char *argv[])
{
	int i = 0;

	//go through each string in argv
	//why am I skipping argv[0]?
	//because argv[0] is the call for the execution of the program, I'm not stupid, Zed...

	char *states[] = {"California", "Oregon", "Washington", "Texas" };
	/* argv[2] = states[1]; */
	/* states[2] = argv[1]; */
	for (i=1; i<argc; i++) {
		printf("arg %d: %s\n", i, argv[i]);
	}

	//let's make our own array of strings

	/* char *states[] = {"California", "Oregon", "Washington", "Texas" }; */

	int num_states = 4;

	for (i=0; i<num_states; i++) {
		printf("state %d: %s\n", i, states[i]);
	}

	return 0;
}
