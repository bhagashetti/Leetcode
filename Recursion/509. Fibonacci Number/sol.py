class Solution:
    def fib(self, n: int) -> int:

        def recursivefib(n):
            if n < 2:
                return n
            return recursivefib(n-1) + recursivefib(n-2)
        return recursivefib(n)

        