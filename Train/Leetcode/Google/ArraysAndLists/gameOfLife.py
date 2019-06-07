from pprint import pprint


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        field = set()

        if not board:
            return board

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]:
                    field.add((i,j))

        def neighbours(cell):
            nei_dead = []
            n_alive = 0
            x, y = cell

            for i in (-1, 1, 0):
                for j in (-1, 1, 0):
                    if 0 <= x+i < len(board) and 0 <= y+j < len(board[0]):
                        if i == 0 and j == 0:
                            continue
                        if (x+i, y+j) in field:
                            n_alive += 1
                        else:
                            nei_dead += [(x + i, y + j)]

            return nei_dead, n_alive

        born = []
        died = []

        # Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        # Any live cell with two or three live neighbors lives on to the next generation.
        # Any live cell with more than three live neighbors dies, as if by over-population.
        # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

        for alive in field:
            nei_dead, n_alive = neighbours(alive)

            if n_alive < 2 or n_alive > 3:
                died += [alive]

            for neighbour in nei_dead:
                neighbour_deads, neighbour_n_alive = neighbours(neighbour)

                if neighbour_n_alive == 3:
                    born += [neighbour]

        # update game
        for cell in born:
            x, y = cell
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                field.add(cell)

                board[x][y] = 1

        for cell in died:
            x, y = cell
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                field.remove(cell)
                board[x][y] = 0

a = Solution()
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# pprint(board)
# print("_________________________________________")
# for i in range(10):
#     a.gameOfLife(board)
#     pprint(board)
#     print("_________________________________________")


print("_________________________________________")
board = [[1,1]]
a.gameOfLife(board)
print(board)