'''THIS WORKS FOR ONLY CONSECUTIVE INTEGERS INPUT'''
def min_swaps(arr):
    ct=0
    for i in range(len(arr)-1):
        while(arr[i]!=i+1):
            temp=arr[i]
            arr[i],arr[temp-1]=arr[temp-1],temp
            ct+=1
    return ct
arr=[int(x) for x in input().split()]
print(min_swaps(arr))

