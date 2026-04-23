class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        maxHeap = [-num for num in count.values()]
        heapq.heapify(maxHeap)
        queue = deque([])

        cycles = 0
        while maxHeap or queue:
            cycles += 1

            if maxHeap:
                task = heapq.heappop(maxHeap) + 1
                if task:
                    queue.append([task, cycles + n])
            else:
                cycles = queue[0][1]

            if queue and queue[0][1] == cycles:
                task = queue.popleft()[0]
                heapq.heappush(maxHeap, task)

        return cycles