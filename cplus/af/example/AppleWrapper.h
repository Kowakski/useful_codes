#if 1
#ifndef _APPLE_WRAPPER_H__
#define _APPLE_WRAPPER_H_
struct tagApple;
#ifdef __cplusplus
extern "C" {
#endif
struct tagApple *GetInstance(void);
void ReleaseInstance(struct tagApple **ppInstance);
extern void SetColor(struct tagApple *pApple, int color);
extern int GetColor(struct tagApple *pApple);
extern int print_test( char* str );
#ifdef __cplusplus
};
#endif
#endif
#else

#ifndef _APPLE_WRAPPER_H__
#define _APPLE_WRAPPER_H_
#ifdef __cplusplus
extern "C" {
#endif
int  GetInstance(int *handle);
void ReleaseInstance(int *handle);
extern void SetColor(int handle, int color);
extern int GetColor(int handle);
#ifdef __cplusplus
};
#endif
#endif

#endif