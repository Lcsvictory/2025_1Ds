#include <stdio.h>

int main() {
	char* a = "����";
	printf("������ a�� ����Ű�� �ּ� : %p\n", a);
	printf("������ a�� ����Ű�� �ּ��� �� : %s\n", a);
	printf("������ a�� �ڱ��ڽ� �ּ� : %p\n", &a);
	printf("������ a�� ����Ű�� �ּ��� ������ �� = a[0]. a[0]�� a[1]�ΰ��� ��Ʈ���� ��� �־�� '��' ���ڰ� ��µ�.: %x\n", (unsigned char)*a); //�ѱ��� 2����Ʈ�� �����.
	printf("������ a�� ����Ű�� �ּ��� ������ ��(�ۼ�Ʈs�� ��¹��) = %.2s\n", a);
	char* b = a;
	char** c = &b; //pointer b = &"����"
	a = "�α�";
	b = "����";
	printf("%s\n", a);
	printf("a = %s\nb = %s\nc = %s\n", a, b, *c);
	printf("a = %p\nb = %p\nc = %p\n", a, b, *c);
}