def bubbleSort(array):

    n=len(array)
    for i in range(0,n):
        for j in range(i,n-i-1,-1):
            if(array[j]<array[j-1]):       
                array[j],array[j-1]=array[j-1],array[j]         #swapping process
    return array

a=[1,2,4,3,0,6,7,8,12,11] #edit as needed
print(bubbleSort(a))
#optimized bubble sort
def bubbleSort(arr):
    while True:
        n=len(arr)
        newi=0
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                newi=i
        n=newi
        if(n<1):
            break
    return arr
arr=[5,4,3,2,1]
print(bubbleSort(arr))
                    
