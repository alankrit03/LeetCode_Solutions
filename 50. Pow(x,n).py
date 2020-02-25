class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x= 1/x
            n=-n
        if n==0:
            return 1
        elif n==1 :
            return x
        else:
            k = self.myPow(x,n//2)
            if n%2==0 :
                return k*k
            else:
                return k*k*x