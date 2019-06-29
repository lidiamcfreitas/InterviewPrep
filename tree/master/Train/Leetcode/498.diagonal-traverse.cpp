#include <vector>

class Solution {
  static bool is_outside(int x, int y, int m, int n){
    return (x<0 || y<0 || x>=m || y>=n);
  }

public:
    std::vector<int> findDiagonalOrder(const std::vector<std::vector<int>>& matrix) {
      std::vector<int> res;
      if (matrix.empty()) return res;

      int m=matrix.size(), n=matrix[0].size();
      int x=0, y=0;
      int end_x=m-1, end_y=n-1;
      bool up=true;

      while(!is_outside(x,y,m,n)){
        res.push_back(matrix[x][y]);
        if (up) {
          if (!is_outside(x - 1, y + 1, m, n)) { // next not outside
            x--;
            y++;
          } else {
            up = false;
            if (!is_outside(x, y + 1, m, n)) { // outside so go right
              y++;
            } else { // right is outside so go down
              x++;
            }
          }
        }
        else {
          if (!is_outside(x+1,y-1, m, n)){
            x++; y--;
          }
          else { // next outside
            up = true;
            if (!is_outside(x+1, y, m, n)){ // outside so go down
              x++;
            }
            else { // down is outside so go right
              y++;
            }
          }
        }
      }
      return res;
    }
};
