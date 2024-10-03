# Count Occurrences

# Problem Description

# Find the number of occurrences of bob in string A consisting of lowercase English alphabets.

# Problem Constraints
# 1 <= |A| <= 1000

# Input Format
# The first and only argument contains the string A, consisting of lowercase English alphabets.

# Output Format
# Return an integer containing the answer.


# Example Input
# Input 1:
#   "abobc"
# Input 2:
#   "bobob"

# Example Output
# Output 1:
#   1
# Output 2:
#   2

# Example Explanation

# Explanation 1:

#   The only occurrence is at second position.
# Explanation 2:

#   Bob occures at first and third position.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count = 0
        if len(A) < 3:
            return -1
        for i in range(len(A)-2):
            if "".join(A[i:i+3]) == 'bob':
                count+= 1
        return count