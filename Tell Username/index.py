nums=[1,2,3,4,5,6]
target=6
left=0
right=len(nums)-1

count=0
# while(left<right):
#     count=count+1
#     mid=int(left+right/2)
#     if(nums[mid]==target): 
#         print("Found at the index", mid)
#         break

#     if(nums[mid]<target): left=left+1

#     if(nums[mid]>target): right=right-1


for i in range(len(nums)):
    count=count+1
    if(nums[i]==target):
        print("Found at the index ",i)
        break


print(count)



