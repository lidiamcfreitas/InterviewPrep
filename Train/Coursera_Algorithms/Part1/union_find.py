class QuickFind:
    def __init__(self, N) -> None:
        super().__init__()

        self.list = []
        self.N = N

        for i in range(N):
            self.list.append(i)

    def connected(self, i, j):
        return self.list[i] == self.list[j]

    def union(self,i ,j): # Too slow!

        if self.connected(i,j):
            return

        i_component = self.list[i]
        j_component = self.list[j]

        for i in range(self.N):
            if self.list[i] == j_component:
                self.list[i] = i_component

        return


class QuickUnion: # Too slow! because tree can get to thin/tall
    def __init__(self, N) -> None:
        super().__init__()

        self.list = []
        self.N = N

        for i in range(N):
            self.list.append(i)

    def root(self, i):
        if i == self.list[i]:
            return i
        return self.root(self.list[i])

    def connected(self, i, j):
        return self.root(i) == self.root(j)

    def union(self,i ,j):
        if not self.connected(i,j):
            root_i = self.root(i)
            root_j = self.root(j)

            self.list[root_j] = root_i



class WeightedQuickUnion:
    def __init__(self, N) -> None:
        super().__init__()

        self.list = []
        self.size_of_tree = [1] * N
        self.N = N


        for i in range(N):
            self.list.append(i)

    def root(self, i): # now it's log(N)!
        if i == self.list[i]:
            return i
        return self.root(self.list[i])

    def connected(self, i, j): # now it's log(N)!
        return self.root(i) == self.root(j)

    def union(self,i ,j): # now it's log(N)!
        if not self.connected(i,j):
            root_i = self.root(i)
            root_j = self.root(j)

            if self.size_of_tree[root_i] < self.size_of_tree[root_j]:
                self.list[root_i] = root_j
                self.size_of_tree[root_j] += self.size_of_tree[root_i]
            else:
                self.list[root_j] = root_i
                self.size_of_tree[root_i] += self.size_of_tree[root_j]
