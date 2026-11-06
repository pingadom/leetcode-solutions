class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = []
        for n in range(0,numRows):
            array.append([])
        c = 0
        while len(s) > 0:
            for i in range(0,numRows):
                for j in range (0,max(numRows-1,1)):
                    array[i].append("")
            if len(s) >= numRows:
                for i in range(0,numRows):
                    array[i][c] = s[i]
                c+=1
                s = s[numRows:]
            else:
                for i in range(0,len(s)):
                    array[i][c] = s[i]
                s = ""

            for j in range(numRows - 2, 0, -1):
                if len(s) == 0:
                    break

                array[j][c] = s[0]
                s = s[1:]
                c += 1
        
        string = ''
        for row in array:
            for item in row:
                string += item

        return string

        return string 

