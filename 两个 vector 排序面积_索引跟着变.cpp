struct AreaCmp {
  AreaCmp(const vector<float>& _areas) : areas(&_areas) {}
  bool operator()(int a, int b) const { return (*areas)[a] > (*areas)[b]; }
  const vector<float>* areas;
};

vector<int> sortIdx(contours.size());
vector<float> areas(contours.size());

for( int n = 0; n < (int)contours.size(); n++ ) {
  sortIdx[n] = n;   //每一个轮廓的索引号。
  areas[n] = contourArea(contours[n], false);  //索引号和面积在两个vector里面，但是顺序要对应上。
}

std::sort( sortIdx.begin(), sortIdx.end(), AreaCmp(areas ));  //按照面积从大到小排列
