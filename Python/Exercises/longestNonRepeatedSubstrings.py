x = "dvdf"
def lengthOfLongestSubstring(s: str) -> int:
    last_seen = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        max_length = max(max_length, right - left)
        

#     longest_strings = {}
#     # while(current_index != len(s)):
#     for index, char in enumerate(s):
#         substring = []
#         size = 0
#         current_index = 0
#         new_string = s[index:]
#         while current_index != len(new_string):
#             if substring and new_string[current_index] in substring:
#                 longest_strings[size] = ''.join(substring)
#                 substring = []
#                 size = 0
#             substring.append(new_string[current_index])
#             size += 1
#             current_index +=1
#         if substring:
#             longest_strings[size] = ''.join(substring)
#     longest_sizes = sorted(longest_strings, reverse=True)
#     print(longest_strings)
#     # print(longest_strings[longest_sizes[0]])
# lengthOfLongestSubstring(x)