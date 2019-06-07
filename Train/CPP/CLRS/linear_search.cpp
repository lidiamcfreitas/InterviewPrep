//
// Created by Lídia Maria Carvalho de Freitas on 08/03/2018.
//

#include <vector>
#include <iostream>


int linear_search(std::vector<int>& array, int n){
  for (int i = 0; i < array.size(); ++i) {
    if (array[i] == n) return i;
  }
}


int main() {
  std::vector<int> array;

  int x, n;
  std::cin >> n;

  while( std::cin >> x){
    array.push_back(x);
  }

  std::cout << linear_search(array, n);

}