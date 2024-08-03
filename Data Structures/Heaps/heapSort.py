from heap import MaxHeap

def heap_sort(array):
    heap = MaxHeap()
    heap.buildMaxHeap(array)

    heap_size = len(heap.max_heap)
    if heap_size == 0:
        print("empty heap")
        return []
    else:
        for i in range(heap_size):
            # swap the maximum value of the heap and the last node
            heap.max_heap[0], heap.max_heap[heap_size-1] = heap.max_heap[heap_size-1], heap.max_heap[0]

            # decrease the size of the heap, partitioning it into unsorted and sorted subarrays
            heap_size -= 1

            # heapify the first node on the unsorted subarray
            heap.heapify(0, heap_size)
    return heap


sorted = heap_sort([1, 150, 100, 75, 25])
print("Sorted: ", sorted.show_heap())
