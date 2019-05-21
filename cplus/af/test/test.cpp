#include<iostream>
#include<map>
typedef struct {
    int buf[9][9];
}t;

t data={
    .buf = {
    {1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1},
    {1,1,1,1,2,1,1,1,1},
    {1,1,1,1,1,1,1,1,1},
    {1,1,1,1,3,1,1,1,1},
    {1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1},
    }
};

int main( void ){
    int i = 0;
    std::map< int, std::string > m;
    m.insert( std::pair<int, std::string>( 1,"studend_one" ) );
    m.insert( std::pair<int, std::string>( 2, "stuednt_two" ) );
    m.insert( std::pair<int, std::string>( 3, "student_three" ) );
    std::map<int, std::string>::iterator iter;
    for( iter = m.begin(); iter != m.end(); iter++ ){
        std::cout<<iter->first<<" "<<iter->second<<std::endl;
    }
#if 1
    std::map< int, t > m2;
    for( i = 0; i < 10; i++ ){
        data.buf[3][3] = i;
        m2.insert( std::pair< int, t >( i, data ) );
    }

    std::map< int, t >::iterator iter2;
    for( iter2 = m2.begin(); iter2 != m2.end(); iter2++ ){
        std::cout<<iter2->first<<"  "<<iter2->second.buf[3][3]<<std::endl;
    }

    std::cout<<"m2 contains "<<m2.size()<<" elements"<<std::endl<<"m2 max size is "<<m2.max_size();
#endif
}