class Solution:
    def divide(self, a: int, b: int) -> int:
        print('start')
        if a == 0:
            return 0
        neg = False
        if a < 0 or b < 0:
            a = abs(a)
            b = abs(b)
            neg = True
        # a是被除数
        n = a.bit_length() - 1
        i = 0
        ans = ''
        while n != -1:
            i = (i << 1) + 1
            print('test', (a >> n) & (i))
            if (c := (a >> n) & (i)) >= b:
                mod = c - b
                print('mod', mod)
                a = mod << n + (i >> 1)
                ans += '1'
            else:
                ans += '0'
            n -= 1
        print('end')
        print(ans)
        if neg:
            return ans
        return ans


obj = Solution()
a = 15
b = 2
obj.divide(a, b)
a = 7
b = -3
obj.divide(a, b)
a = -7
b = 3
obj.divide(a, b)
a = 0
b = 1
obj.divide(a, b)
