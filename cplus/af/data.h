/*
 *定义一个类，用来处理af中的数，包括数据的存储和运算
 */
#include<iostream>

template<typename T1,  typename T2>
class data{
public:
    data();
    ~data();
    int  data_size_get( void );//return data size
    bool data_insert( T2 data );//insert data
    void data_erase( void );   //clear data
private:
    unsigned int size; //map size
    std::array< T1, size > indexs; //save keys value, key type is T1
    std::map< T1, T2 > map; //save data, key type is T1, data type is T2
};
