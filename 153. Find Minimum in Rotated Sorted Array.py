def findmin():
    l=-1
    n=len(nums)
    h=n-1
    while h-l > 1:
        m=(l+h)//2
        if nums[m] > nums[n-1]:
            l=m
        else:
            h=m
    return nums[h]




nums= [2,3,4,5,1]

ans= findmin()
print(ans)