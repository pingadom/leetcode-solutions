class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        start, end = max(arriveAlice, arriveBob), min(leaveAlice, leaveBob)
        if start > end: 
            return 0
        start, end = (int(start[:2]), int(start[3:])), (int(end[:2]), int(end[3:]))

        days = 0
        for m in range(start[0], end[0]+1):
            days += days_in_month[m-1]

        days -= ((start[1]-1) + (days_in_month[end[0]-1] - end[1]))

        
        return days
        


        