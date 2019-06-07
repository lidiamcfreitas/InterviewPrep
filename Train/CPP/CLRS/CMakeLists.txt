cmake_minimum_required(VERSION 3.9)
project(CLRS)

set(CMAKE_CXX_STANDARD 17)

add_executable(main main.cpp)
add_executable(selection_sort selection_sort.cpp)
add_executable(binary_sum binary_sum.cpp)
add_executable(linear_search linear_search.cpp)
add_executable(insertion_sort insertion_sort.cpp)
add_executable(merge_sort merge_sort.cpp)