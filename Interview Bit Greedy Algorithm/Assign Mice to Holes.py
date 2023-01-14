class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):
		A.sort()
		B.sort()
		return max([abs(A[i]-B[i]) for i in range(len(A))])
