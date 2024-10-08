#  Diffk II
# Solved
# feature icon
# Using hints except Complete Solution is Penalty free now
# Use Hint
# Problem Description

# Given an array A of integers and another non negative integer B .

# Find if there exists 2 indices i and j such that A[i] - A[j] = B and i != j.



# Problem Constraints

# 1 <= |A| <= 106

# 0 <= A[i] <= 109

# 0 <= B <= 109



# Input Format

# First argument A is an array of integer

# Second argument B is an integer



# Output Format

# Return 1 if two such indexes are found and 0 otherwise


# Example Input

# Input 1:
# A = [1, 5, 3]
# B = 2
# Input 2:
# A = [2, 4, 3]
# B = 3


# Example Output

# Output 1:
# 1
# Output 2:
# 0


# Example Explanation

# For Input 1:
# The given value of A[1] = 1 and A[3] = 3.
# The value of A[3] - A[1] = 2.
# For Input 2:
# There are no pairs such that difference is B.

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        difference_hashmap = {}
        if len(A) < 2:
            return 0
        for i in A:
            if ( (i-B) in difference_hashmap ) or ( (i+B) in difference_hashmap ):
                return 1
            difference_hashmap[i] = i
        return 0