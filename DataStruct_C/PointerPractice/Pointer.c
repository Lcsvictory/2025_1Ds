#include <stdio.h>

int main() {
	char* a = "대한";
	printf("포인터 a가 가르키는 주소 : %p\n", a);
	printf("포인터 a가 가르키는 주소의 값 : %s\n", a);
	printf("포인터 a의 자기자신 주소 : %p\n", &a);
	printf("포인터 a가 가르키는 주소의 역참조 값 = a[0]. a[0]과 a[1]두가지 비트값이 모두 있어야 '대' 글자가 출력됨.: %x\n", (unsigned char)*a); //한글은 2바이트로 저장됨.
	printf("포인터 a가 가르키는 주소의 역참조 값(퍼센트s로 출력방법) = %.2s\n", a);
	char* b = a;
	char** c = &b; //pointer b = &"대한"
	a = "민국";
	b = "만세";
	printf("%s\n", a);
	printf("a = %s\nb = %s\nc = %s\n", a, b, *c);
	printf("a = %p\nb = %p\nc = %p\n", a, b, *c);
}