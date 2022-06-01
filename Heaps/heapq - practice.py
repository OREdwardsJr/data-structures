import heapq

heap = []

# Heap Push
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 100)
heapq.heappush(heap, 10)
heapq.heappush(heap, 55)
print(heap)

# Heap Pop
test = heapq.heappop(heap)
print(test)
print(heap)

# Heapify
arr = [10, 28, 93, 0, 8, 3, 82, 21]
heapq.heapify(arr)
print(arr)

# Pushpop
test = heapq.heappushpop(arr, 35)
print(test)
print(arr)

# Heapq - Replace
# Opposite of pushpop

# N smallest / largest
print(heapq.nsmallest(4, arr))
print(heapq.nlargest(4, arr))

# Priority Queue
list1 = [(1, "ria"), (4, "sia"), (3, "gia")]
heapq.heapify(list1)
print(list1)
for i in range(len(list1)):
    print(heapq.heappop(list1))
