import math
input = [1, 7, 5, 9, 2, 12, 3, 10, 20, 22, 12,15,13, 21,19]

K = 2
diff = { i: i + K for i in input }
diffCount = [(i, diff[i]) for i in diff if diff[i] in input]
print(len(diffCount), diffCount)

# def findCountPairsWithDiff(input, K):