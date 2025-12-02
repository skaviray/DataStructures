string = "hellobyering"

## charecter with the index is stored
last_seen = {}

## All substrings without repeated charecters are stored along with the lengths
substrings = {}

left = 0

for right, char in enumerate(string):
    if last_seen.get(char):
        print(last_seen)
        # print("hello")
        substrings[string[left:right]] = right - left 
        left = last_seen[char] + 1
    last_seen[char] = right
if left != len(string):
    substrings[string[left:]] = len(string) - left 
print(substrings)
unrepeatedstrings = sorted(substrings, key=lambda s : substrings[s], reverse=True)
print("longest substring is ", substrings[unrepeatedstrings[0]])
# print(sorted(substrings,key=lambda substring: substrings[substring], reverse=True))
