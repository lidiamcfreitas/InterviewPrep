//
// Created by Lídia Maria Carvalho de Freitas on 08/03/2018.
//

#include <string>
#include <iostream>

int main(){
    std::string a, b, res;
    int over = 0;

    std::cin >> a >> b;

    for (int i = a.size() - 1; i >= 0; --i) {
        if (over) {
            if (a[i] == b[i]) {
                res = "1" + res;
                if (a[i] == '1') {
                    over = 1;
                } else {
                    over = 0;
                }
            }
            else {
                res = "0" + res;
                over = 1;
            }
        } else {
            if (a[i] == b[i]) {
                res = "0" + res;
                if (a[i] == '1'){
                    over = 1;
                }
                else {
                    over = 0;
                }
            } else {
                res = "1" + res;
                over = 0;
            }
        }
    }

    if (over){
        res = "1" + res;
    }

    std::cout << res;

}