Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false



class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num / 2;
        temp = 0;
        while(sqrt != temp):
            temp = sqrt
            sqrt = ( num/temp + temp) / 2;
        return sqrt.is_integer()
