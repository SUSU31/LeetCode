class Solution:
    def reverse(self, x: int) -> int:
        f = x
        if x<-pow(2, 31) or x>pow(2,31)-1:
            return 0
        t = 0
        if f<0:
            x=x*(-1)
        while not x//10 == 0:
            t = t * 10 + x % 10
            x = x//10
        t = t * 10 + x % 10
        if f<0:
            t=t*(-1)
        if t<-pow(2, 31) or t>pow(2,31)-1:
            return 0
        return t


if __name__ == '__main__':
    S=Solution()
    t = S.reverse(1534236469)
    print(t)
