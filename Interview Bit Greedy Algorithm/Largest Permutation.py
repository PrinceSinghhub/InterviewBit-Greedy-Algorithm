class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        
        copy = A.copy()
        copy.sort()
        if A == copy[::-1]:
            return A 
        
        
