class Solution:
    def canCompleteCircuit(self, A,B):
		
		# base case
		if sum(A) - sum(B) < 0:
			return -1

		A_tank = 0  # A available in car till now
		start_index = 0  # Consider first A station as starting point

		for i in range(len(A)):

			A_tank += A[i] - B[i]

			if A_tank < 0:  # the car has deficit of petrol
				start_index = i+1  # change the starting point
				A_tank = 0  # make the current A to 0, as we will be starting again from next station

		return start_index