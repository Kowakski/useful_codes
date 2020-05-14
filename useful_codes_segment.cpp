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

计算斜率:
float AfResult::value_slope( alt_u16 value[], alt_u8 lens ){
    alt_u8 i = 0;
    int m = lens;
    float sum_x = 0, sum_y = 0, sum_xy = 0, sum_xx = 0;

    for( i = 0; i < lens; i++ ){
        sum_x  += i;
        sum_y  += value[i];
        sum_xy += i*value[i];
        sum_xx += i*i;
    }
    return (m*sum_xy - sum_x*sum_y)/(m*sum_xx-(sum_x)*(sum_x));
}