
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        nearest = [-1] * 26

        # DFS on the original tree
        # (node, exiting, previous_nearest)
        stack = [(0, False, -1)]

        while stack:
            node, exiting, prev = stack.pop()
            c = ord(s[node]) - ord('a')

            if exiting:
                nearest[c] = prev
                continue

            prev = nearest[c]

            if prev != -1:
                new_parent[node] = prev

            nearest[c] = node

            stack.append((node, True, prev))

            for child in children[node]:
                stack.append((child, False, -1))

        # Build the final tree
        final_children = [[] for _ in range(n)]
        for i in range(1, n):
            final_children[new_parent[i]].append(i)

        # Traverse the final tree
        order = [0]
        for node in order:
            order.extend(final_children[node])

        # Calculate subtree sizes bottom-up
        answer = [1] * n

        for node in reversed(order):
            if node != 0:
                answer[new_parent[node]] += answer[node]

        return answer
