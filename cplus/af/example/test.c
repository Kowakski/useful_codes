/*
 *
g++ -c apple.cpp
g++ -c apple.cpp  AppleWrapper.cpp
gcc test.c -o test AppleWrapper.o apple.o -lstdc++
*/
#include "AppleWrapper.h"
#include <assert.h>

int main(void)
{
	struct tagApple * pApple;
	pApple= GetInstance( );
	SetColor(pApple, 1);
	int color = GetColor(pApple);
	printf("color = %d\n", color);
	ReleaseInstance(&pApple);
	assert(pApple == 0);
    print_test("hello");
	return 0;
}
