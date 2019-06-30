/*
 * @lc app=leetcode id=293 lang=cpp
 *
 * [293] Flip Game
 *
 * https://leetcode.com/problems/flip-game/description/
 *
 * algorithms
 * Easy (58.96%)
 * Total Accepted:    41.5K
 * Total Submissions: 70.3K
 * Testcase Example:  '"++++"'
 *
 * You are playing the following Flip Game with your friend: Given a string
 * that contains only these two characters: + and -, you and your friend take
 * turns to flip two consecutive "++" into "--". The game ends when a person
 * can no longer make a move and therefore the other person will be the
 * winner.
 * 
 * Write a function to compute all possible states of the string after one
 * valid move.
 * 
 * Example:
 * 
 * 
 * Input: s = "++++"
 * Output: 
 * [
 * ⁠ "--++",
 * ⁠ "+--+",
 * ⁠ "++--"
 * ]
 * 
 * 
 * Note: If there is no valid move, return an empty list [].
 * 
 */

#include <string>
#include <vector>
#include <iostream>

class Solution {
public:
    std::vector<std::string> generatePossibleNextMoves(std::string s) {
      std::vector<std::string> res;

      for(int i=1; i<s.size(); i++){
        std::cout << i << std::endl;
        if (s[i]==s[i-1] && s[i]=='+'){
          std::string solution(s);
          solution[i]='-'; solution[i-1]='-';
          res.push_back(solution);
        }
      }

      return res;
    }
};