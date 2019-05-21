/*
 *one dimension data storage, visit. include int, float
 *two dimension data storage, visit. include int, float
 */
#include "data.h"

data::data( int s ):size(10){
    size = s;
}

int data::data_size_get( void ){
    return indexs.size();
}

template< typename T1, typename T2 >
bool data::data_insert( T1 key,T2 data ){
    if( indexs.size() == indexs.max_size() ){
        return false;
        std::cout<<"indexs buf is full"<<endl;
    }
    map.insert( pair<T1, T2>( key, data ) );
    return true;
}