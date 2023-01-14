class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key=lambda x:x[1])
        i=1
        n=len(A)
        cnt=1
        prev=A[0]
        while i<n:
            cur=A[i]
            if cur[0]>prev[1]:
                prev=cur
                cnt+=1
            i+=1
        return cnt
