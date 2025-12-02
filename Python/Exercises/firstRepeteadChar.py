charFrequency = {}
input = "a ggrreenn applle"

def getCharFrequency(str):
    str = str.replace(' ','')
    for char in str:
        if char in charFrequency:
            charFrequency[char] += 1
        else:
            charFrequency[char] = 1
    return charFrequency

def firstNonRepeatedString(str):
    frequency = getCharFrequency(input)
    print(frequency)
    for char in str:
        if frequency.get(char, None) and frequency[char] > 1:
            return char
    return None

print(firstNonRepeatedString(input))

