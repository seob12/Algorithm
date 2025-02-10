import heapq

n = int(input())
count = n

heap = []

for _ in range(n):
    lst = list(map(int,input().split()))
    for i in lst:
        #heapq.heappush(heap, i)
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

        #print(heap)


print(heap[0])