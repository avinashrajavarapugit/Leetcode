class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # count no of set bits in num2
        # take res as num1 and cnt set bits of num1 from left as cnt2 if cnt2 == cnt 1 stop adn return
        # add remaining set bits if needed to the right where there is 0
        a, b = bin(num1).count('1'), bin(num2).count('1')
        res = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                res ^= 1 << i
                a -= 1
            if a < b and (1 << i) & num1 == 0:
                res ^= 1 << i
                a += 1
        return res
