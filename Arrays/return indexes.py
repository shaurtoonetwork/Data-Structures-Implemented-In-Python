#Naive approach o(n^2)

'''def yo(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == s:
                print(i,j)'''




#Sorting  o(nlogn)
'''def yo(arr):
    arr1 = sorted(arr)
    n = len(arr1)
    l = 0
    r = len(arr) - 1
    while l<r:
        if (arr[l]+arr[r] == s):
            print(l,r)
            return
            
        elif(arr[l]+arr[r]<s):
            l+=1
        else:
            r-=1
    return 0'''



#Hash Maps
def printPair(A, s):
    dict = {}
 
    for i, e in enumerate(A):
        if s - e in dict:
            print(dict.get(s-e), i)
            
        dict[e] = i
    

 
 
 
arr = [2,3,5,6,7,8,9]
s = 10
printPair(arr,s)



