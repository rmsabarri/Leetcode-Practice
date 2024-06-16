class Solution {
    public int fib(int n) {
        int i, sum=0;
        if(n==1 || n==0)
        return n;
        if(n<0)
        return 0;
        return(fib(n-1)+fib(n-2));


        
        }
    }
