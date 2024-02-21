def maxArea(height: List[int]) -> int:
    # height = [1,8,6,2,5,4,8,3,7]
    # height = [2, 3, 4, 5, 18, 17, 6]
    # d = {}
    length = len(height)
    count = 1
    max = 0
    j=length-1
    i=0
    while True:
        val = min(height[i], height[j])
        diff = abs(j - i)
        mul = val * diff
        if max<mul:
            max=mul
        if height[i]<height[j]:
            # j-=1
            i+=1
        else:
            j-=1

        if i==(length) or j==(0):
            break

    return max




