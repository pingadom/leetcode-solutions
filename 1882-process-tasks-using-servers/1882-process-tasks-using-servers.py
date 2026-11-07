import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        
        ans = [0] * len(tasks)
        server_heap = []
        for i,j in enumerate(servers):
            heapq.heappush(server_heap, (j,i))

        busy_heap = []

        c,t = 0,0
        while c < len(tasks):

            t = max(t,c)
            
            while busy_heap:
                x,y,z = busy_heap[0]
                if x <= t:
                    heapq.heappop(busy_heap)
                    heapq.heappush(server_heap, (y,z))
                    
                else:
                    break
            

            if server_heap:
                s_w,s_id = server_heap[0]
                ans[c] = heapq.heappop(server_heap)[1]
                heapq.heappush(busy_heap,((t)+tasks[c],s_w,s_id))

            elif busy_heap:
                f,g,h = busy_heap[0]
                ans[c] = heapq.heappop(busy_heap)[2]
                heapq.heappush(busy_heap,((f)+tasks[c],g,h))
            
           
            if not server_heap:
                t = busy_heap[0][0]
            c += 1
           
        
        return ans