import random
### Insertion Sort
def InsertionSort(array,start,end):
    for i in range(start+1,end+1):
        key=array[i]
        j=i-1
        while j>=start and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1]=key
### Merge arrays
def Merge(array,p,q,r):
    left_half = array[p:q+1]
    right_half = array[q+1:r+1]

    i = j = 0 
    k = p  
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        array[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        array[k] = right_half[j]
        j += 1
        k += 1
### Merge Sort
def MergeSort(Array, start_index, end_index):
    if start_index < end_index:
        mid = (start_index + end_index) // 2  
        MergeSort(Array, start_index, mid)
        MergeSort(Array,  mid+ 1, end_index)
        Merge(Array,start_index,mid,end_index)  
### Bubble Sort
def BubbleSort(array,start,end):
    for i in range(start,end):
        for j in range(start,end-i+start):
            if(array[j]> array[j+1]):
                array[j],array[j+1]=array[j+1],array[j]
    return array
### Selection Sort
def SelectionSort(array,start,end):
    for i in range(start,end+1):
        min_index =i
        for j in range (i+1,end+1):
            if array[j]<array[min_index]:
                min_index=j
        array[min_index],array[i]=array[i],array[min_index]
    return array
### Hybrid Merge Sort
def HybridMergeSort(Array, start_index, end_index):
    if end_index - start_index <= 5:
        InsertionSort(Array, start_index, end_index)
    else:
        if start_index < end_index:
            mid = (start_index + end_index) // 2  
            HybridMergeSort(Array, start_index, mid)
            HybridMergeSort(Array, mid + 1, end_index)
            Merge(Array, start_index, mid, end_index)
#### Bucket Sort
def BucketSort(array):
    length=len(array)
    output_array=[]
    number_of_buckets=[[]for _ in range(length)]
    for num in array:
        index=int(length*num)
        number_of_buckets[index].append(num)
    for bucket in number_of_buckets:
        bucket.sort()
    for bucket in number_of_buckets:
        output_array.extend(bucket)
    return output_array
### Counting Sort
def CountingSort(array):
    min_val=min(array) 
    k=max(array)-min_val
    intermediate_array=[0]*(k + 1)
    output=[]
    for j in array:
        intermediate_array[j-min_val]+=1
    for i in range(len(intermediate_array)):
        for _ in range(intermediate_array[i]):
            output.append(i+min_val) 
    return output
### Radix Sort
def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output=[0]*n
    count=[0]*10
    for i in range(n):
        index=(arr[i]//exp)%10
        count[index]+=1
    for i in range(1, 10):
        count[i]+=count[i-1]
    for i in range(n-1,-1,-1):
        index=(arr[i]//exp)%10
        output[count[index]-1]=arr[i]
        count[index]-=1
    for i in range(n):
        arr[i]=output[i]

def RadixSort(arr):
    max_val=max(arr)
    exp=1 
    while max_val//exp>0:
        counting_sort_by_digit(arr,exp)
        exp*=10
### Quick Sort
def partition(arr, p, r):
    x = arr[p]  # The first element is chosen as the pivot
    a = r          # a starts from the last element
    for b in range(p + 1, r + 1): 
        while b <= a and arr[a] >= x:
            a -= 1
        if b>= a:## Here the a and b cross each other
            break
        if arr[b] > x:
            arr[b], arr[a] = arr[a], arr[b]
    # Swap the pivot with the element
    arr[p], arr[a] = arr[a], arr[p]
    return a 
def Quick_Sort(array, p, r):
    if p<r:
        q = partition(array, p, r)
        Quick_Sort(array, p, q - 1)
        Quick_Sort(array, q + 1,r)
### Bogo Sort
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
def bogo_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr) 
    return arr
### Heap Sort
def heapify(arr, n, i):
    largest = i 
    left = 2 * i + 1  
    right = 2 * i + 2 
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)  