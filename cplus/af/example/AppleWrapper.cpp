#if 1
#include "AppleWrapper.h"
#include "apple.h"
#include <iostream>

// #ifdef __cplusplus
// extern "C" {
// #endif
using namespace std;
struct tagApple
{
	Apple apple;
};
struct tagApple *GetInstance(void)
{
	return new struct tagApple;
}
void ReleaseInstance(struct tagApple **ppInstance)
{
	delete *ppInstance;
	*ppInstance = 0;

}
void SetColor(struct tagApple *pApple, int color)
{
	pApple->apple.SetColor(color);
}

int GetColor(struct tagApple *pApple)
{
	return pApple->apple.GetColor();
}
int print_test( char* str ){
    cout<<"C++ print"<<str<<endl;
    return 0;
}
// #ifdef __cplusplus
// };
// #endif

#else

#include "AppleWrapper.h"
#include "apple.h"
#include <vector>

#ifdef __cplusplus
extern "C" {
#endif

static std::vector<Apple *> g_appleVector;

int GetInstance(int * handle)
{
 g_appleVector[0] =  new Apple;
 *handle = 0;
 return 1;
}
void ReleaseInstance(int *handle)
{
 delete g_appleVector[*handle];
 *handle = -1;

}
void SetColor(int handle, int color)
{
 g_appleVector[handle]->SetColor(color);
}

int GetColor(int handle)
{
 return g_appleVector[handle]->GetColor();
}
#ifdef __cplusplus
};
#endif

#endif