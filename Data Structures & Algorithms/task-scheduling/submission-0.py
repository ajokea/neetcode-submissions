class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        maxHeap = []
        for num in count.values():
            heapq.heappush(maxHeap, -num)

        queue = deque([])

        cycles = 0
        while maxHeap or queue:
            cycles += 1

            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task:
                    queue.append([task, cycles + n])

            if queue and queue[0][1] == cycles:
                task = queue.popleft()[0]
                heapq.heappush(maxHeap, task)

        return cycles