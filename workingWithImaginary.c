#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int chr_has(char * str, char item) {
	for (int i = 0;;i++) {
		if (str[i] == '\0')
			break;
		else if (str[i] == item)
			goto done;
	}
	return 0;
	done:
		return 1;
}
int valid(char * input) {
	for (int k = 0;;k++) {
		if (input[k] == '\0') return 1;
		if (input[k] < 48 || input[k] > 57) return 0;
	}
}

void repl() {
	char str[100];
	int remainder;
	int input;
	start:
	printf("Enter exponent of \033[3mi\033[0m (result = i\u207f; what's `n`?):");
	scanf("%99s", str);
	if (valid(str) == 0) {
		puts("\033[31mThat was not an positive integer (whole number).\033[0m");
		input = 0;
	}
	else {
		input = atoi(str);
		remainder = input % 4;
		switch (remainder) {
			case 0: puts("\tresult: 1"); break;
			case 1: puts("\tresult: i"); break;
			case 2:	puts("\tresult: -1"); break;
			case 3: puts("\tresult: -i"); break;
		}
	}
	goto start;
}
int main(void) {
	repl();
  	return 0;
}
