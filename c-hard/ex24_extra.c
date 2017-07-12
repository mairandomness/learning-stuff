#include <stdio.h>
#include <stdlib.h>

void recebe(char *enderec)
{
	scanf("%c", &enderec[0]);

	int i = 0;

	while (enderec[i] != '\n')
	{
		if (enderec[i] == ' ') {
			i--;
	}
		i++;
		scanf( "%c", &enderec[i]);
	}
	enderec[i] = '\0';
}

int main (int argc, char *argv[])
{
	char *name;
	name = malloc(sizeof(char)*100);

	printf("Type a name:");
	recebe(name);

	printf("%s\n", name);

	return 0;
}

