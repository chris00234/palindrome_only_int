class Solution:
    def isPalindrome(self, x: int) -> bool:
        tmp = x
        digit = 0
        if x < 0:
            return False
        
        while tmp != 0:
            tmp = tmp // 10
            digit += 1
        
        iter = digit // 2
        
        for i in range(iter):
            front = x // pow(10, (digit - i - 1))
            end = x % 10
            if front != end:
                return False
        
        return True  
            