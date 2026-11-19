class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        check = set(str(word))
        temp = set("".join(list(map("".join,board))))
        if len(check) > len(temp):
            return False

        seen = {}
        len_r = len(board)
        len_c = len(board[0])
        len_f = len(word)

        def go(v,p,start):
            if p == len_f:
                return True
            r,c = v
            neighbors = [(i, j)
                        for i, j in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                        if 0 <= i < len_r and 0 <= j < len_c and (i,j) not in seen[start]]                        
            for i,j in neighbors:
                if board[i][j] == word[p]:
                    seen[start].append((i,j))
                    if go((i,j),p+1,start):
                        return True
                    else:
                        seen[start].pop()
            return False
                

        for r in range(len_r):
            for c in range(len_c):
                if board[r][c] == word[0]:
                    seen[(r,c)] = [(r,c)]
                    if go((r,c),1,(r,c)):
                        return True
                else:
                    continue
        
        return False
        