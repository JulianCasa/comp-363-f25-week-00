#Global Variables to access in the heap
heapArray = []
elmntCt = 0

#Given methods
def left_child(parent: int) -> int:
    return 2 * parent + 1

def right_child(parent: int) -> int:
    return 2 * (parent + 1)

def parent(child: int) -> int:
    return (child - 1) // 2

def swap(heap_array: list, i: int, j: int) -> None:
    """In place swap of two array elements."""
    if i != j:
        temp = heap_array[i]
        heap_array[i] = heap_array[j]
        heap_array[j] = temp

#Add method
def add(element) -> None:
    #Immediately adds the element to the heap then iterates the element count
    heapArray.append(element)
    global elmntCt
    elmntCt+=1

    #It then loops and checks if the heap property is violated
    index = elmntCt - 1
    while index > 0 and heapArray[parent(index)] > heapArray[index]:
        swap(heapArray, parent(index), index)
        index = parent(index)

def remove() -> str:
    global elmntCt
    #checks if elements exist in the heap
    if elmntCt == 0:
        removed = None
    else:
    #Removes the first element in the array then copies the last item to the front
    #It then removes the copy at the very end and decrements the element count
        removed = heapArray[0]
        heapArray[0] = heapArray[elmntCt - 1]
        heapArray.pop()
        elmntCt -= 1

    #Variables needed tore balancing the heap
        index = 0
        leftNode = left_child(index)
        rightNode = right_child(index)
        smallest = index

        while (leftNode < elmntCt and heapArray[index] > heapArray[leftNode]) or (rightNode < elmntCt and heapArray[index] > heapArray[rightNode]):
        
        #finds the smallest element then swaps
            if leftNode < elmntCt and heapArray[leftNode] < heapArray[smallest]:
                smallest = leftNode
            if rightNode < elmntCt and heapArray[rightNode] < heapArray[smallest]:
                smallest = rightNode

            if smallest != index:
                swap(heapArray, index, smallest)


    return removed

#Test Code
print(remove()) # None

add(5)
add(3)
add(8)
add(1)

print(heapArray)  # [1, 3, 8, 5]

print(remove())   # 1
print(heapArray)  # [3, 5, 8]
    
add(25) 
print(heapArray) # [3, 5, 8, 25]
print(remove()) # 3
print(heapArray) # [5, 25, 8]

print(heapArray[0]) # 5

