string = "babad"
palindrome_strings = {}
last_seen = {}
left = 0
for right, char in enumerate(string):
    # print(last_seen)
    if char in last_seen and last_seen[char] >= left:
        string = reversed_string = string[last_seen[char]:right+1]
        reversed_string.split().reverse()
        if string == reversed_string  and len(string) > 1:
            palindrome_strings[string] = right - last_seen[char] + 1
    last_seen[char] = right
print(palindrome_strings)
