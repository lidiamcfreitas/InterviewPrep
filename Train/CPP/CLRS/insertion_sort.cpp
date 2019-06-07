//
// Created by Lídia Maria Carvalho de Freitas on 08/03/2018.
//

#include <vector>
#include <iostream>

int main(){
  std::vector<int> array;
  int x;

  while (std::cin >> x) array.push_back(x);

  for (int i = 1; i < array.size(); ++i) {
    int n = i, key = array[i];

    while (n > 0){
      if (array[n-1] > key){
        array[n] = array[n-1];
        n = n - 1;
      } else {
        break;
      }
    }
    array[n] = key;
  }

  for (int i : array){
    std::cout << i << " ";
  }
  std::cout << std::endl;
}

