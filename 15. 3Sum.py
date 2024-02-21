

def threeSum(nums: List[int]) -> List[List[int]]:
    # nums = [-1, 0, 1, 2, -1, -4]
    l=[]
    length=len(nums)
    import copy
    for i in range(0,length-1):
        temp=copy.deepcopy(nums)
        a=temp.pop(i)
        b=temp.pop(i)
        for j in temp:
            if a+b+j==0 and [a,b,j] not in l and a!=b and b!=j and j!=a:
                l.append([a,b,j])
    print(l)
    # i += 1
    return l

