#include<stdio.h>

int main(int arc, char *argv[])
{
	int numbers[4] = { 1 };
	char name[4] = { 'a', 'b', 'c', 'd' };

	// first, print them out raw
	printf("numbers: %d %d %d %d\n", numbers[0], numbers[1], numbers[2], numbers[3]);
  printf("name each: %c %c %c %c\n", name[0], name[1], name[2], name[3]);

	printf("name: %s\n", name);

	// set up the numbers

	numbers[0] = '1';
	numbers[1] = '2';
	numbers[2] = '3';
	numbers[3] = '4';

	//set uo the name

	name[0] = 51;
	name[1] = 52;
	name[2] = 53;
	name[3] = '\0';

	// then print them out initialized
 	printf("numbers: %d %d %d %d\n", numbers[0], numbers[1], numbers[2], numbers[3]);
  printf("name each: %c %c %c %c\n", name[0], name[1], name[2], name[3]);

	//print the name like a string
	printf("name: %s\n", name);

	//another way to use name
	char *another = "Zed";

	printf("another: %s\n", another);

	printf("another each: %c %c %c %c\n", another[0], another[1], another[2], another[3]);

	return 0;

}
