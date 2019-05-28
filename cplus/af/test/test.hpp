#include<map>
#define TwoDimSize 9
typedef struct{
    int buf[TwoDimSize][TwoDimSize];
}TwoDimData;


#define OneDimSize 9
typedef struct{
    int buf[OneDimSize];
}OneDimData;

template<typename T1, typename T2>
class data{
   public:
    bool insert(T1 key, T2 data);
    bool find(T1 key, T2* buf);
   private:
    std::map<T1, T2> mmap;
};