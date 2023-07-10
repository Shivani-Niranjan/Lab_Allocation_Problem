x,y,z,n = map(int, input().split())
allocation = sorted([x,y,z,n])
n = (allocation[(allocation.index(n))+1])
if n==x:
    print("L1")
elif n==y:
    print("L2")
else :
    print("L3")