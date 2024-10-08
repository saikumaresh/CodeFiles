# Sub-array with 0 sum

# Problem Description
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1, else return 0.

# Problem Constraints
# 1 <= |A| <= 100000
# -10^9 <= A[i] <= 10^9

# Input Format
# The only argument given is the integer array A.

# Output Format
# Return whether the given array contains a subarray with a sum equal to 0.

# Example Input

# Input 1:
#  A = [1, 2, 3, 4, 5]

# Input 2:
#  A = [4, -1, 1]

# Example Output

# Output 1:
#  0
# Output 2:
#  1

# Example Explanation

# Explanation 1:
#  No subarray has sum 0.

# Explanation 2:
#  The subarray [-1, 1] has sum 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        sum_index_hashmap = {}
        currsum = 0
        for i in range(len(A)):
            currsum += A[i]
            if currsum in sum_index_hashmap:
                return 1
            else:
                sum_index_hashmap[currsum] = 1
        if 0 in sum_index_hashmap.keys():
            return 1
        else:
            return 0
        