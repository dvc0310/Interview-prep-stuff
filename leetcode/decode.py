from collections import deque
import copy
class Solution(object):
    def decodeString(self, s):
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] == "]":
                stack.pop()
                substr = ""
                while stack[-1] != '[':
                    substr += stack.pop()
                num = ""
                stack.pop()
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                num = int(num[::-1])
                substr = num * substr
                stack.append(substr)
        wholestr = ""
        while stack:
            wholestr += stack.pop()
        return wholestr[::-1]
    
    def predictPartyVictory(self, senate):
        rq = deque()
        dq = deque()
        for index, senator in enumerate(senate):
            if senator == "R":
                rq.append((senator, index))
            else:
                dq.append((senator, index))
        
        while dq and rq:
            i = 0
            dskip = 0
            rskip = 0
            while i < len(senate):
                if senate[i][0] == "R":
                    if rskip == 0 and dq:
                        dq.popleft()
                        dskip += 1
                    else:
                        rskip -= 1
                else:
                    if dskip == 0 and rq:
                        rq.popleft()
                        rskip += 1
                    else:
                        dskip -= 1
                i += 1
            senate = copy.deepcopy(dq)
            senate.extend(copy.deepcopy(rq))
            senate = sorted(senate, key=lambda x: x[1])

        if len(dq) > len(rq):
            return "Dire"
        
        return "Radiant"

from collections import deque

class Solution2(object):
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        # Fill the queues with the senators
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(('R', i))
            else:
                dire.append(('D', i))

        # Start voting
        while radiant and dire:
            r_senator = radiant.popleft()
            d_senator = dire.popleft()

            if r_senator[1] < d_senator[1]:
                # 'R' senator bans 'D' senator
                radiant.append(('R', r_senator[1] + len(senate)))
            else:
                # 'D' senator bans 'R' senator
                dire.append(('D', d_senator[1] + len(senate)))

        return 'Radiant' if radiant else 'Dire'


s = "3[a2[c]]"
print(Solution().decodeString(s))
s = "2[a]10[bc]"
print(Solution().decodeString(s))
print(Solution2().predictPartyVictory("DRRD"))