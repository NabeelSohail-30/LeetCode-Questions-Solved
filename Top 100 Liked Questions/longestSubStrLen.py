class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize variables
        max_length = 0
        start = 0
        char_index_map = {}

        for end in range(len(s)):
            # If the character is already in the char_index_map and its index is greater than or equal to the start of the current substring
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                # Update the start of the substring to the next index of the repeating character
                start = char_index_map[s[end]] + 1
            # Update the index of the current character in the map
            char_index_map[s[end]] = end
            # Update the maximum length if needed
            max_length = max(max_length, end - start + 1)

        return max_length


solution = Solution()
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(solution.lengthOfLongestSubstring(s1))  # Output: 3
print(solution.lengthOfLongestSubstring(s2))  # Output: 1
print(solution.lengthOfLongestSubstring(s3))  # Output: 3
