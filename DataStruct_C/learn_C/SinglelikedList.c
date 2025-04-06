#include <stdio.h>


//����ü�� Ÿ������ �����ؼ� struct ����� ������� �ʰ� Ÿ��ó�� ��밡��
//typedef struct NODE {
//	int nData;
//
//	struct NODE* next;
//} NODE;

struct NODE {
	int nData; //4����Ʈ
	// padding �߰�
	struct NODE* next; //8����Ʈ
}; // 4 + 8 = 12����Ʈ ������ 4 or 8�ǹ���� ��������. ���� 16����Ʈ��.




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