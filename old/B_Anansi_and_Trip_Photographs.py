t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    heights=list(map(int,input().split()))
    heights.sort()
    left=0
    right=n
    flag=True
    while left<len(heights) and right<len(heights):
        difference=abs(heights[left]-heights[right])
        if difference<x:
            flag=False
            break
        else:
            left+=1
            right+=1

    if flag:
        print('YES')
    else:
        print('NO')
