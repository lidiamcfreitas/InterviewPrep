

/*
 * @lc app=leetcode id=469 lang=cpp
 *
 * [469] Convex Polygon
 *
 * https://leetcode.com/problems/convex-polygon/description/
 *
 * algorithms
 * Medium (35.52%)
 * Total Accepted:    7.1K
 * Total Submissions: 20K
 * Testcase Example:  '[[0,0],[0,1],[1,1],[1,0]]'
 *
 * Given a list of points that form a polygon when joined sequentially, find if
 * this polygon is convex (Convex polygon definition).
 * 
 * 
 * 
 * Note:
 * 
 * 
 * There are at least 3 and at most 10,000 points.
 * Coordinates are in the range -10,000 to 10,000.
 * You may assume the polygon formed by given points is always a simple polygon
 * (Simple polygon definition). In other words, we ensure that exactly two
 * edges intersect at each vertex, and that edges otherwise don't intersect
 * each other.
 * 
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * [[0,0],[0,1],[1,1],[1,0]]
 * 
 * Answer: True
 * 
 * Explanation:
 * 
 * 
 * Example 2:
 * 
 * 
 * [[0,0],[0,10],[10,10],[10,0],[5,5]]
 * 
 * Answer: False
 * 
 * Explanation:
 * 
 * 
 */

#include <math.h>

class Solution {
  // determinant of 2x2 matrix [A1-A0, A2-A0]
  long det2(const vector<vector<int>>& A) {
    return (A[1][0]-A[0][0])*(A[2][1]-A[0][1]) - (A[1][1]-A[0][1])*(A[2][0]-A[0][0]);
  }

public:
  bool isConvex(const vector<vector<int>>& p) {
    int pos=0, neg=0, n=p.size();

    for (int i=0; i < n; ++i) {
      long det = det2({p[i], p[(i+1)%n], p[(i+2)%n]});
      if ((pos|=(det>0))*(neg|=(det<0))) return false;
    }
    return true;
  }
};
