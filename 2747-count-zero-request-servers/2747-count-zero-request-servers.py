
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        sorted_logs = sorted(logs, key=lambda x: x[1])
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])

        final = [0] * len(queries)
        server_count = [0] * (n + 1)

        min_pointer = 0
        max_pointer = 0
        active_servers = 0

        for original_index, query in sorted_queries:
            left, right = query - x, query

            # Add logs entering the window
            while max_pointer < len(sorted_logs) and sorted_logs[max_pointer][1] <= right:
                server = sorted_logs[max_pointer][0]

                if server_count[server] == 0:
                    active_servers += 1

                server_count[server] += 1
                max_pointer += 1

            # Remove logs leaving the window
            while min_pointer < max_pointer and sorted_logs[min_pointer][1] < left:
                server = sorted_logs[min_pointer][0]

                server_count[server] -= 1

                if server_count[server] == 0:
                    active_servers -= 1

                min_pointer += 1

            final[original_index] = n - active_servers

        return final
