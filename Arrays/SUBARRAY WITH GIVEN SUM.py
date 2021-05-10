def subArraysum(arr,n,s):
    for i in range(n):
        cur_sum = arr[i]
        j=i+1
        while j<=n:
            if cur_sum == s:
                print("%d %d"%(i,j-1))
                return 1
            if cur_sum>s or j==n:
                break
            cur_sum+=arr[j]
            j=j+1
    print("No subarray found")
    return 0

arr = [15,2,4,8,9,5,10,23,34,22,12,45]
n=len(arr)
s=22
subArraysum(arr,n,s)






    





