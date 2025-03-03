def min_heapify(arr,n,i):
    smallest=i
    left=2*i+1
    right=2*i+2

    if left < n and arr[left]<arr[smallest]:
        smallest=left
    
    if right < n and arr[right]<arr[smallest]:
        smallest=right
    
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        min_heapify(arr,n,smallest)

def build_heap(arr,n):
    for i in range(n//2-1,-1,-1):
        min_heapify(arr,n,i)

def heap_sort(arr):
    n=len(arr)
    build_heap(arr,n)
    sorted=[]

    for _ in range(n):
        sorted.append(arr[0])
        arr[0]=arr[-1]
        arr.pop()
        min_heapify(arr,len(arr),0)
    
    return sorted

arr = [5, 3, 8, 4, 2, 7, 1, 9]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)