#include<stdio.h>
int main(int argc, char *argv[])
{
	//create two arrays we care about
	int ages[]={ 23, 43, 12, 89, 2};
	char *names[]={"Allan", "Frank", "Mary", "John", "Lisa"};

	//safely get the size of ages
	int count = sizeof(ages) / sizeof(int);
	int i = 0;

	//first way using index
	for (i=0; i<count; i++) {
		printf("%s has %d years alive.\n", names[i], ages[i]);
	}

	printf("---\n");

	//set up pointers to the start of the arrays
	int *cur_age = ages;
	char **cur_name = names;

	//second way using pointers

	for (i=0; i<count; i++) {
		printf("%s is %d years old.\n", *(cur_name + i),*(cur_age + i));
	}

	printf("---\n");

	//third way, pointers are just arrays

	for (i=0; i<count; i++) {
		printf("%s is %d years old again.\n", cur_name[i], cur_age[i]);
	}

	printf("---\n");

	//fourth way with pointers being used in a complicated way

	for (cur_name = names, cur_age=ages; (cur_age - ages) < count; cur_name ++, cur_age++) {
		printf("%s lived %d years so far. \n", *cur_name, *cur_age);
	}

	//
	//
	// PRINTING THE SAME STUFF BUT STARTING AT THE END
	//
	//

	printf("---\n");
	//first way using index
	for (i=count-1; i>=0; i--) {
		printf("%s has %d years alive.\n", names[i], ages[i]);
	}

	printf("---\n");

	//second way using pointers
	//reset the pointers first :) starting at the end
	cur_age = ages + count -1;
	cur_name = names + count -1;


	for (i=0; i<count; i++) {
		printf("%s is %d years old.\n", *(cur_name - i),*(cur_age - i));
	}

	printf("---\n");

	//third way, pointers are just arrays
	//reset pointers again, now starting at the beggining

	cur_age = ages;
	cur_name = names;


	for (i=count-1; i>=0; i--) {
		printf("%s is %d years old again.\n", cur_name[i], cur_age[i]);
	}

	printf("---\n");

	//fourth way with pointers being used in a complicated way

	for (cur_name = names + count-1, cur_age=ages+count-1;
			(cur_age - ages) >= 0 ; cur_name --, cur_age--) {
		printf("%s lived %d years so far. \n", *cur_name, *cur_age);
	}

	cur_age=ages;
	printf("size of ages %ld\n", sizeof(ages));

	printf("size of pointer ages %ld\n", sizeof(cur_age));
	printf("size of pointer ages with * %ld\n", sizeof(*cur_age));


	cur_name=names;
	printf("size of names %ld\n", sizeof(names));

	printf("size a  name %ld\n", sizeof(names[0]));
	printf("size of pointer names %ld\n", sizeof(cur_name));
	printf("size of pointer names with * %ld\n", sizeof(*cur_name));
	printf("size of pointer names with ** %ld\n", sizeof(**cur_name));

	char strings[]={"llal"};
  char *apontando= strings;
	printf("string %ld\n", sizeof(strings));
	printf("string[0] %ld\n", sizeof(strings[0]));
	printf("apontando %ld\n", sizeof(apontando));
	printf("apontando* %ld\n", sizeof(*apontando));


	return 0;

}



