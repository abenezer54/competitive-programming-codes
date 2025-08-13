
import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def II(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def solve():
    q = II()
    first = defaultdict(deque)
    root = ListNode()
    end = root
    parent = defaultdict(ListNode)
    for _ in range(q):
        inp = input().split()
        if len(inp) == 3:
            x = int(inp[1])
            y = int(inp[2])
            node = ListNode(x)
            if len(first[y]) > 0:
                prev = first[y][0]
                if prev == end:
                    end = node
                parent[node] = prev
                node.next = prev.next
                prev.next = node
                parent[node.next] = node
            else:
                # print(x,y)
                parent[node] = end
                # print(end.val)
                end.next = node
                end = node
            first[x].append(node)
        else:
            w = int(inp[1])
            if len(first[w]) == 0:
                continue

            prev = parent[first[w][0]]
            # print(first[w][0].next.val)
            # print(prev.val)
            if first[w][0] == end:
                # print('here', first[w][0].val, end.val)
                prev.next = None
                end = prev
            else:
                prev.next = first[w][0].next
                parent[prev.next] = prev

            first[w].popleft()
    cur = root
    ans = []
    while cur.next:
        ans.append(cur.next.val)
        cur = cur.next
    print(*ans)
solve()
