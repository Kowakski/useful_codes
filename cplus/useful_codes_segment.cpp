/*
 *@comment:对结构体进行排序，然后删除重复的元素
 *@重定义“<”小于号，重定义"=="等于号，然后用sort和erase排序并删除重复内容
 */
typedef struct{
    alt_u8 x;
    alt_u8 y;
}axis_t; //0 x, 1 y

bool operator < ( const axis_t& a, const axis_t& b ){
    if( a.x < b.x ){
        return true;
    }else if( (a.x == b.x)&&( a.y < b.y ) ){
        return true;
    }
    return false;
}

bool operator == ( const axis_t& a, const axis_t& b ){
    return ( ( a.x == b.x ) && ( a.y == b.y ) );
}

void SncDetec::unique_vector( std::vector<axis_t>& vec ){
    std::sort( vec.begin(), vec.end() );
    vec.erase( std::unique( vec.begin(), vec.end() ), vec.end() );
    return;
}