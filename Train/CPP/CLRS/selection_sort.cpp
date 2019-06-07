//
// Created by Lídia Maria Carvalho de Freitas on 08/03/2018.
//

#include <vector>
#include <iostream>


int main(){
    std::vector<int> array;
    int x;

    while (std::cin >> x){
        array.push_back(x);
    }

    for (int i = 0; i < array.size() - 1; ++i) {
        int key = array[i], min_i = i, min = key;

        for (int j = i + 1; j < array.size(); ++j) {
            if (array[j] < min){
                min = array[j];
                min_i = j;
            }
        }

        array[i] = array[min_i];
        array[min_i] = key;
    }

    for (int x : array){
        std::cout << x << " ";
    }
    std::cout << std::endl;
}
