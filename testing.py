def hello(arr):
    n=len(arr)
    last=n//2-1

    for i in range (last,-1,-1):
        left=2*i+1
        right=2*i+2

        if (arr[left] < arr[i]):
            temp=arr[i]
            arr[i]=arr[left]
            arr[left]=temp

        if (arr[right] < arr[i]):
            temp=arr[i]
            arr[i]=arr[right]
            arr[right]=temp  

    print("here is the final min-heaped array",arr)

    
arr=[4,10,3,5,1]
hello(arr)