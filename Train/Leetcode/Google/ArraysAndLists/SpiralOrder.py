# took too long


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return matrix

        m , n = len(matrix), len(matrix[0])
        top, bottom, right, left = -1, m, n, -1

        elems_left = m * n
        going = 'right'
        res = []
        i, j = 0, 0

        def valid(i, j):
            print('valid:', bottom, i, top, ":", top, j, bottom)
            return top < i < bottom and left < j < right

        while elems_left:
            print(going, res, elems_left)
            if going == 'right':
                if valid(i, j):
                    res += [matrix[i][j]]
                    j += 1
                    elems_left -= 1
                else:
                    j -= 1
                    i += 1
                    going = 'down'
                    top += 1
            elif going == 'down':
                if valid(i,j):
                    res += [matrix[i][j]]
                    i += 1
                    elems_left -= 1
                else:
                    i -= 1
                    j -= 1
                    going = 'left'
                    right -= 1
            elif going == 'left':
                if valid(i, j):
                    res += [matrix[i][j]]
                    j -= 1
                    elems_left -= 1
                else:
                    j += 1
                    i -= 1
                    going = 'up'
                    bottom -= 1
            elif going == 'up':
                if valid(i, j):
                    res += [matrix[i][j]]
                    i -= 1
                    elems_left -= 1
                else:
                    going = 'right'
                    i += 1
                    j += 1
                    left += 1
            print(res)


        return res


a = Solution()
mat = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(a.spiralOrder(matrix=mat))
