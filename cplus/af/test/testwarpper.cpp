#include<stdio.h>
#include "test.hpp"

struct data_{
    data<int,TwoDimData> D;
};


/*
 *@comment insert data struct, key is int, and data is struct
 */
struct data_* Get_instance( void ){
    return new struct data_;    
};

int data_map_two_dimen_insert( struct data_* d, int key, TwoDimData  buf ){
    bool result = false;
    result = d->D.insert( key, buf );
    return result;
}

int data_map_two_dimen_find( struct data_*d, int key, TwoDimData* buf ){
    bool result = false;
    result = d->D.find(key, buf);
    return result;
}
