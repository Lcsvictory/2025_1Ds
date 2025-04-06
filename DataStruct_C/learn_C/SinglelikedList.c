#include <stdio.h>


//구조체를 타입으로 선언해서 struct 예약어 사용하지 않고 타입처럼 사용가능
//typedef struct NODE {
//	int nData;
//
//	struct NODE* next;
//} NODE;

struct NODE {
	int nData; //4바이트
	// padding 추가
	struct NODE* next; //8바이트
}; // 4 + 8 = 12바이트 이지만 4 or 8의배수로 만들어버림. 따라서 16바이트임.




int main(void) {

	
	
	struct NODE list[5] = { 0 };
	list[0].next = &list[1];
	list[1].next = &list[2];
	list[2].next = &list[3];
	list[3].next = &list[4];
	list[4].next = 0;

	printf("list[0] = %p\n", &list[0]);
	for (int i = 0; i < 5; i++) {
		printf("list[%d].next = %p\n", i, list[i].next);
	}

	list[0].nData = 100;
	list[1].nData = 200;
	list[2].nData = 300;
	list[3].nData = 400;
	list[4].nData = 500;

	for (int i = 0; i < 5; i++) {
		printf("list[%d].nData = %d\n", i, list[i].nData);
	}

	struct NODE* pHead = &list[0];
	while (pHead != NULL) {
		printf("%p : %d\n", pHead, pHead->nData);
		pHead = pHead->next;
	}
	return 0;
}