''' 
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        # more efficient to add the strings as characters to an array
        result = []
        while i < len(word1) and j < len(word2):
            # append method appends object to the end of a list 
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word1[j:])


        # join method concatenates items together into a new string
        return "".join(result)

#create an instance of the class
solution = Solution()

word_one = "apple"
word_two = "tiger"

print(solution.mergeAlternately(word_one, word_two))


#------------- Alternate solution ------------

def merge_strings(word1, word2):
    result = []
    i, j = 0, 0
    # Inside the loop, check if the pointer i is less than the length of word1. If true, append the character at position i in word1 to the result list, and increment i
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            result.append(word1[i])
            i += 1
        if j < len(word2):
            result.append(word2[j])
            j += 1

    return ''.join(result)

word1_1, word2_1 = "beautiful", "pqr"
output_1 = merge_strings(word1_1, word2_1)
print(output_1)
