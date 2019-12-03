#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

//Solves Quadratic equations using the quadratic formula

void solve (void) {

	char A[20];
	char B[20];
	char C[20];
	int a, b, c;
	float sol1, sol2;
	start:
		printf("\033[38;2;255;255;0mEnter a Quadratic equation variables, and I will solve it for you:\n");
		
		printf("\033[31mWhat's your `a`?: \033[32m");
		fgets(A, 20, stdin);
		printf("\033[31mWhat's your `b`?: \033[32m");
		fgets(B, 20, stdin);
		printf("\033[31mFinally, what's your `c`?: \033[32m");
		fgets(C, 20, stdin);

		printf("Processing...\033[0m\n");

		a = atoi(A);
		b = atoi(B);
		c = atoi(C);
		char i[30] = "";
		double m = (sqrt(pow(b,2) - (4 * a * c)));
		if (isnan(m)) {
			strcpy(i, "\033[3m\033[1mi\033[0m");
			m = sqrt(-1 * (pow(b, 2) - (4*a*c)));
		}
		sol1 = (b * -1 + m)/2 * a;
		sol2 = (b * -1 - m)/2 * a;
		double sa1, sa2;
		sa1 = a * pow(sol1, 2);
		sa2 = a * pow(sol2, 2);
		if ((b * sol1) + c + sa1 != 0.0) {
			sa1 *= -1;
		}
		if ((b * sol2) + c + sa2 != 0.0) {
			sa2 *= -1;
		}
		if ((int) sol1 == sol1)
			printf("(x = %i%s)\n", (int) sol1, i);
		else
			printf("(x = %f%s)\n", sol1, i);
		printf("\t%f + %f + %d = 0.000000\n", sa1, b * sol1, c);
		if ((int) sol2 == sol2)
			printf("(x = %d%s)\n", (int) sol2, i);
		else
			printf("(x = %f%s)\n", sol2, i);
		printf("\t%f + %f + %d = 0.000000\n", sa2, b * sol2, c);

		goto start;
}
int main (void) {
	puts("\033[34m(c) 2019 @Raphael Spoerri\n");
	puts("instructions:\n");
	puts("interact with the terminal by giving it");
	puts("your a, b, and c.");
	puts("\n\nhave fun!\n");
	solve();
	return 0;
}
