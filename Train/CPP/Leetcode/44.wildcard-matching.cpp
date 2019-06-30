#include <unordered_map>
#include <string>
#include <utility>
#include <map>

class Solution {

  std::map<std::pair<int,int>, bool> memo;

 public:


  bool isMatch(const std::string& s, const std::string& p, int index_s=0, int index_p=0) {
    auto pt_memo = memo.find(std::make_pair(index_s,index_p));
    if (pt_memo != memo.end()){
      return pt_memo->second;
    }

    // cout << index_s << "  " << index_p << endl;

    if (index_s<s.size()){
      if (index_p==p.length()) { // s not empty and p is empty
        memo[std::make_pair(index_s,index_p)] = false;
        return memo[std::make_pair(index_s,index_p)];
      }

      if (p[index_p]=='?' || s[index_s]==p[index_p]){ // match
        memo[std::make_pair(index_s,index_p)] = isMatch(s, p, index_s+1, index_p+1);
        return memo[std::make_pair(index_s,index_p)];
      }
      if (p[index_p]=='*'){
        memo[std::make_pair(index_s,index_p)] = isMatch(s, p, index_s+1, index_p) || isMatch(s, p, index_s, index_p+1);
        return memo[std::make_pair(index_s,index_p)];
      } else { // no match
        memo[std::make_pair(index_s,index_p)] = false;
        return memo[std::make_pair(index_s,index_p)];
      }
    }

    while (index_p<p.size() && p[index_p]=='*') index_p++;
    return index_p==p.size();
  }
};