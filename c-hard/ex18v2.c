
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

//die from ex17
void die(const char *message)
{
	if (errno) {
		perror(message);
	} else {
		printf("ERROR: %s\n", message);
	}

	exit(1);
}

// a typedef creates a fake type, in this case a function pointer

typedef int (*compare_cb) (int a, int b);

// a classic bubblesort function that uses
// the compare_cb to do the sorting

int *bubble_sort(int *numbers, int count, compare_cb cmp)
{
	int temp = 0;
	int i = 0;
	int j = 0;
	int *target = malloc(count * sizeof(int));

	if (!target)
		die("Memory error.");

	memcpy(target, numbers, count * sizeof(int));

	for (i=0; i < count; i++) {
		for (j = 0; j < count -1; j++) {
			if (cmp(target[j], target[j+1]) > 0) {
				temp = target[j+1];
				target[j+1] = target[j];
				target[j] = temp;
			}
		}
	}
	 return target;
}

int *insert_sort(int *numbers, int count, compare_cb cmp)
{
	int temp_first = 0;
	int temp_index =0;
	int i = 0;
	int j = 0;
	int *target = malloc(count * sizeof(int));

	memcpy(target, numbers, count * sizeof(int));

	for (i=0; i< count-1; i++) {
		temp_first = target[i];
		temp_index = i;
		for (j=i; j<count; j++) {
			if (cmp(temp_first, target[j])>0) {
				temp_first = target[j];
				temp_index = j;
			}
		}
		target[temp_index] = target[i];
		target[i] = temp_first;
	}

	return target;
}






int sorted_order(int a, int b)
{
	return a-b;
}

int reverse_order(int a, int b)
{
	return b-a;
}

int strange_order (int a, int b)
{
	if (a==0||b==0) {
		return 0;
	} else {
		return a%b;
		}
}

// used to test that we are sorting things correctly
// by doing the sort and printing it out

void test_sorting(int *numbers, int count, compare_cb cmp)
{
	int i = 0;
	int *sorted = bubble_sort(numbers, count, cmp);
	int *sorted2 = insert_sort(numbers, count, cmp);
	int indicator = 1;

	if (!sorted)
		die("Failed to sort as requested");

	for (i=0; i<count; i++) {
		printf("%d ", sorted[i]);
	}
	printf("\n");


	for (i=0; i<count; i++) {
		printf("%d ", sorted2[i]);
	}
	printf("\n");


	for (i=0; i < count; i++){
		if (sorted[i]!=sorted2[i]) {
			indicator=0;
		}
	}
	if (indicator) {
		printf("the sortings are consistent\n");
	} else printf("The sortings are inconsistent\n");

	free(sorted);
	free(sorted2);
}

int main(int argc, char *argv[])
{
	if (argc < 2) die("USAGE: ex18 4 3 1 5 6");

	int count = argc -1;
	int i =0;
	// pode dizer que o ponteiro eh igual o array + 1, isso soh muda os indices na hora de copiar
	char **inputs = argv + 1;

	int *numbers = malloc(count * sizeof(int));
	if (!numbers) die("Memory error.");

	for (i=0; i < count; i++) {
		numbers[i] = atoi(inputs[i]);
	}

	test_sorting(numbers, count, sorted_order);
	test_sorting(numbers, count, reverse_order);
	test_sorting(numbers, count, strange_order);

	free(numbers);

	return 0;
}

