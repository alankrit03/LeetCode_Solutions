def minSubArrayLen(s, nums):
    i=-1
    n=len(nums)
    sum_ = 0
    while i<n and sum_<s:
        print(sum_)
        i += 1
        sum_+=nums[i]

    if i==n and sum_<s:
        return 0
    j=0
    print(sum_)
    while 1:
        if sum_ - arr[j] >=s:
            sum_ -= arr[j]
            j+=1
        else:
            break

    print(f'subarray at this point = {nums[j: i + 1]} i={i} j={j} sum = {sum_}')
    while i < n-1 :

        sum_-=nums[j]
        sum_ += nums[i+1]
        j+=1
        i+=1

        while 1:
            if sum_ - arr[j] >= s:
                sum_ -= arr[j]
                j += 1
            else:
                break

        print(f'subarray at this point = {nums[j: i + 1]} i={i} j={j} sum = {sum_}')



    return i-j+1






sum_=8
arr=[2,3,1,2,4,3,1,6,2,7]

ans = minSubArrayLen(sum_,arr)
print('ans = ',ans)