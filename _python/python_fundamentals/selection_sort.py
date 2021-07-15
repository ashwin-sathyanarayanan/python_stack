arr = [50,32,2,77,25]

def selectionSort(arr):
    minIndex = 0
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i+1,len(arr)):
            if(min > arr[j]):
                min = arr[j]
                minIndex = j
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    return arr

print(selectionSort(arr))