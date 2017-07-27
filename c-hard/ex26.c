#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <glob.h>
#include "dbg.h"

int file_search(FILE *file, char *word)
{
	size_t length_word = strlen(word);
	int size_of_word = sizeof(char)*length_word;
	char *is_this_word = malloc(size_of_word);
	long int offset = 0;
	int read_bytes = size_of_word;

	rewind(file);
	while (read_bytes) 	{
	  read_bytes = fread(is_this_word, size_of_word, 1,file);

		int v = strcmp(is_this_word, word);
		if (v==0) {
			free(is_this_word);
			return 1;
		}
		offset++;
		fseek(file, offset, SEEK_SET);
	}
	free(is_this_word);
	return 0;
}

typedef struct {
	int count;
	char **filenames;

} FILE_LIST;

FILE_LIST* find_files(char* pattern){
	glob_t glob_result;
	glob(pattern,GLOB_TILDE,NULL,&glob_result);

	// copy the results from glob to our result struct
	FILE_LIST* result = malloc(sizeof(FILE_LIST*));
  result->count = glob_result.gl_pathc;
	result->filenames = malloc(sizeof(char*)*result->count);

	for (int i=0; i < result->count; i++){
		result->filenames[i] = malloc(sizeof(char)*strlen(glob_result.gl_pathv[i]));
		strcpy(result->filenames[i], glob_result.gl_pathv[i]);
	}

	globfree(&glob_result);
	return result;
}

int amain (int argc, char *argv[]) {
	FILE* file = fopen("./a.txt", "r");
	if (!file) {
		printf("shiat arquivo nao abriu");
		return -1;
	}

  printf("achou? %d\n", file_search(file, "pipoca"));
  printf("achou? %d\n", file_search(file, "pipoco"));
  printf("achou? %d\n", file_search(file, "pipica"));
	return 1;
}

int main(int argc, char *argv[])
{
	int count = argc;
	int start=1;
	int or_and=0; //if its an or and we get at least one one,
	check(argc>1, "Please input at least one word to be found.");

	int v = strcmp("-o", argv[1]);

	int words = argc-1;
	if (v == 0){
		check(argc>2, "Please input at least one word to be found.");
		or_and = 1;
		start = 2;
		words = argc-2;
	}


	FILE_LIST* files = find_files("*.*");
	for (int i = 0; i < files->count; i++) {
		char* filename = files->filenames[i];
		FILE *file = fopen(filename, "r+");

		int words_found =0;
		for (int j = start; j < count; j++)	{
			int result_search = file_search(file, argv[j]);
			if(or_and==0 && result_search==0 ){ //and, didnt find word, skip rest of words
				break;
			}
			if(or_and ==1 && result_search==1){ //or, found one word, print file and skip rest of words
				printf("%s\n", filename);
				break;
			}
			if(or_and == 0 && result_search == 1){ //and, found one word, lets make sure it found all
				words_found++;
			}

			//the last option is an or with the not being found, so we keep looking and do nothing
		}

		if (or_and == 0 && words_found == words) printf("%s\n", filename);
		free(filename);
	}

  free(files->filenames);
  free(files);

	return 0;


error:
	return -1;


}


