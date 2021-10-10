import heapq,random

a = [random.randint(1,100) for i in range(10)]
print(a)
print(heapq.nlargest(3, a))
print(heapq.nsmallest(3, a))