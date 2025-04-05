#include <stdio.h>


int funcPointer(int a) {
	printf("testPointer() -> hello world\n");
	return 0;
}

int main(void) {
	int (*imptFunc)(int) = funcPointer;
	funcPointer(0);
	return 0;
}