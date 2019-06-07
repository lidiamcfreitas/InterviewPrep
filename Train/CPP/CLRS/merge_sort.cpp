//
// Created by Lídia Maria Carvalho de Freitas on 08/03/2018.
//
#include <vector>
#include <iostream>


std::vector<int>& merge_sort(std::vector<int>&);
std::vector<int>& merge(std::vector<int>& array1, std::vector<int>& array2);

int main(){
  std::vector<int> array;
  int x;

  while (std::cin >> x) array.push_back(x);

  array = merge_sort(array);


}

std::vector<int>& merge_sort(std::vector<int>& array,long i, long j){
  if (i < j){
    long mid = i + (j - i) / 2;
    std::vector<int> left  = merge_sort(array, i, mid);
    std::vector<int> right = merge_sort(array, mid+1,j);
    return merge(left, right);
  }
}
std::vector<int>& merge(std::vector<int> &array1, std::vector<int> &array2) {
  int i=0,j=0;
  std::vector<int> result;

  while (i < array1.size() && j < array2.size()){
    if (i == array1.size()){
      result.push_back(array2[j]);
      ++j;
    }
    else if (j == array2.size()){
      result.push_back(array1[i]);
      ++i;
    }
    else {
      if (array1[i] < array2[j]){
        result.push_back(array1[i]);
        ++i;
      } else {
        result.push_back(array2[j]);
        ++j;
      }
    }
  }
  return result;
}

