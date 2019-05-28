#include <stdio.h>
// #include <<cstddef>>
#ifndef _APPLE_WRAPPER_H__
#define _APPLE_WRAPPER_H_

#ifdef __cplusplus
extern "C" {
#endif

extern struct data_* Get_instance( void );
extern int data_map_two_dimen_insert( struct data_* d, int key, TwoDimData  buf );
extern int data_map_two_dimen_find( struct data_*d, int key, TwoDimData* buf );

#ifdef __cplusplus
};
#endif
#endif