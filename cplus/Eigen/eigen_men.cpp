// #include "funset.hpp"
#include <math.h>
#include <iostream>
#include <vector>
#include <string>
// #include <opencv2/opencv.hpp>
#include <Eigen/Dense>
// #include "common.hpp"
#if 1
int test_meanStdDev()
{
/*
    int data[2][3] = {
               {1,2,3},
               {4,5,6}
           };

    const int rows{ 2 }, cols{ 3 };

    std::cout << Eigen::Map < Eigen::Matrix<int,2,3> >(data) << std::endl;
*/
    int array[9];
    for(int i = 0; i < 9; ++i) array[i] = i;
    cout << Map<Matrix3i>(array) << endl;

    return 0;
}
#else
int test_meanStdDev()
{
    std::vector<std::vector<float>> vec{ { 1.2f, 2.5f, 5.6f, -2.5f },
                        { -3.6f, 9.2f, 0.5f, 7.2f },
                        { 4.3f, 1.3f, 9.4f, -3.4f } };
    const int rows{ 3 }, cols{ 4 };

    std::vector<float> vec_;
    for (int i = 0; i < rows; ++i) {
        vec_.insert(vec_.begin() + i * cols, vec[i].begin(), vec[i].end());
    }
    // Eigen::Map < Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor> > m(vec_.data(), 1, rows * cols);
    std::cout << vec_.data() << std::endl;
    Eigen::Map < Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor> > m(vec_.data(),  rows,  cols);

    fprintf(stderr, "source matrix:\n");
    std::cout << m << std::endl;

    Eigen::MatrixXf mean = m.rowwise().mean(); //<==> m.rowwise().sum() / m.cols();
    float mean_ = mean(0, 0);
    Eigen::MatrixXf sqsum = (m * m.transpose()).rowwise().sum();
    float sqsum_ = sqsum(0, 0);
    float scale = 1. / (rows*cols);
    float variance_ = sqsum_ * scale - mean_ * mean_;
    float stddev_ = std::sqrt(variance_);
    fprintf(stdout, "\nEigen implement:\n");
    fprintf(stdout, "mean: %f, variance: %f, standard deviation: %f\n", mean_, variance_, stddev_);

    return 0;
}
#endif
int main( void ){
    test_meanStdDev();
    return 0;
}