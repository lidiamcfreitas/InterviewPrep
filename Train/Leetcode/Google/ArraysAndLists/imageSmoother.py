from copy import deepcopy


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        def get_val(x, y):
            count = 0
            s = 0

            for i in (-1,0,1):
                for j in (-1,0,1):

                    new_point = x + i, y + j

                    if 0 <= new_point[0] < len(M) and 0 <= new_point[1] < len(M[0]):
                        count += 1
                        s += M[new_point[0]][new_point[1]]
            if count:
                return s // count
            return 0

        res = deepcopy(M)

        for i in range(len(M)):
            for j in range(len(M[0])):
                res[i][j] = get_val(i,j)

        return res
