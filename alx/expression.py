import os, sys
sys.stdin = open("expression.in", "r")
sys.stdout = open("expression.out", 'w')

input = lambda: sys.stdin.readline().strip()
m = int(input())
n = int(input())
a = list(map(int, input().split()))
# Disjoint Set Union (DSU) / Union-Find Class
class Dsu:
    def __init__(self, size):
        # Initialize the parent and size arrays
        self.parent = list(range(size))  # Each element is its own parent initially
        self.size = [1 for _ in range(size)]  # Initial size of each set is 1

    def find(self, node):
        # Find the root of x with path compression
        root = node
        while root != self.parent[root]:
            root = self.parent[root]  # Move up to the parent
        while node != root:
            nxt = self.parent[node]
            self.parent[node] = root  # Path compression step
            node = nxt
        return root
    def union(self, x, y):
        # Union by size: attach smaller tree to the larger tree
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                rootx, rooty = rooty, rootx  # Ensure rooty is the larger root
            self.parent[rootx] = rooty  # Merge the trees
            self.size[rooty] += self.size[rootx]  # Update the size of the root rooty

    def is_connected(self, x, y):
        # Check if x and y are in the same set
        return self.find(x) == self.find(y)

def primeFactors(n):
    
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


MOD = 1 << 63
mult = 1
for i in range(n):
    mult *= a[i]
    # mult %= MOD


val = mult ** (1 / m)
if val != int(val):
    print(0)
else:
    print(1)
    vals = Counter(primeFactors(val))
    # print(vals)
    for k, v in vals.items():
        print(k, v)


