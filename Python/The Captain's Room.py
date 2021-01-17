# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
nums=map(int, input().split(" "))
nums=sorted(nums)
for i in range(1,len(nums)):
    if i!=len(nums)-1:
        if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
            print (nums[i])
            break
    else:
        print (nums[i])
