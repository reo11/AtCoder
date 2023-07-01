import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
st = []
for _ in range(m):
    s, t = map(int, input().split())
    st.append([s, t])
lr = []
for _ in range(n):
    l, r = map(int, input().split())
    lr.append([l, r])


class Graph:
    # https://www.geeksforgeeks.org/python-program-for-topological-sorting/
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.rules = defaultdict(lambda: [0, float("inf")])

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def addRule(self, i, l, r):
        # num_i factor has to be l <= i <= r
        self.rules[i] = [l, r]

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack, depth=0):
        # Mark the current node as visited.
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        stack_num = n - (len(stack) + depth)
        # print(v, stack_num, depth)
        for i in self.graph[v]:
            # print(v, stack_num, depth, self.rules[stack_num])
            if (
                visited[i] == False
                and self.rules[stack_num][0] <= i + 1
                and i + 1 <= self.rules[stack_num][1]
            ):
                self.topologicalSortUtil(i, visited, stack, depth + 1)
        # Push current vertex to stack which stores result
        stack.appendleft(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = deque([])
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            stack_num = n - len(stack)
            if (
                visited[i] == False
                and self.rules[stack_num][0] <= i + 1
                and i + 1 <= self.rules[stack_num][1]
            ):
                self.topologicalSortUtil(i, visited, stack)
        # Print contents of stack
        return stack


def check(ans, st, lr):
    flag = True
    for s, t in st:
        if not (ans[s - 1] < ans[t - 1]):
            flag = False
            break
    # print(flag)
    for i, (l, r) in enumerate(lr):
        if not (l <= ans[i] and ans[i] <= r):
            flag = False
            break
    # print(flag)
    return flag


g = Graph(n)
for s, t in st:
    # 辺を追加
    g.addEdge(s - 1, t - 1)

for i, (l, r) in enumerate(lr):
    # 頂点の条件を追加
    g.addRule(i + 1, l, r)

top = g.topologicalSort()
ans = [0 for _ in range(n)]

for i, num in enumerate(top):
    ans[num] = i + 1
print(top)
print(ans)
if len(ans) == n and check(ans, st, lr):
    print("Yes")
    print(*ans, sep=" ")
else:
    print("No")
