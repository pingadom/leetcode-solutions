class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack)