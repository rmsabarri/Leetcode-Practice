class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False 
        
        rev=0
        temp=x

        while temp!=0:
            d=temp%10
            rev=rev*10+d
            temp //=10
        
        return rev==x
        