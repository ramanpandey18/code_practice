A = [[54, 70, 24, 65, 55, 99, 23, 31, 79, 58],
  [13, 93, 4, 77, 21, 41, 90, 18, 73, 97],
  [78, 67, 47, 97, 31, 82, 54, 48, 28, 39],
  [60, 60, 49, 11, 39, 25, 41, 30, 92, 67],
  [68, 18, 86, 13, 79, 84, 93, 45, 3, 90],
  [43, 83, 32, 8, 78, 55, 67, 26, 24, 11],
  [64, 31, 55, 49, 8, 36, 14, 97, 72, 52],
  [36, 1, 93, 49, 42, 91, 31, 18, 62, 50],
  [15, 45, 49, 27, 70, 75, 2, 49, 98, 98],
  [32, 34, 100, 73, 92, 26, 23, 94, 40, 81],
  [99, 29, 43, 81, 96, 67, 66, 51, 26, 68],
  [20, 97, 36, 60, 36, 70, 15, 2, 73, 30],
  [54, 17, 18, 40, 55, 17, 78, 88, 53, 40],
  [79, 30, 96, 75, 11, 48, 56, 91, 77, 49],
  [99, 55, 73, 51, 65, 13, 62, 85, 36, 88],
  [27, 61, 87, 94, 18, 94, 9, 57, 24, 15],
  [92, 9, 76, 81, 42, 70, 26, 64, 86, 4],
  [76, 82, 68, 36, 55, 97, 15, 20, 69, 62],
  [99, 78, 23, 10, 27, 53, 66, 86, 77, 88],
  [18, 33, 61, 14, 96, 12, 31, 99, 61, 50],
  [56, 32, 14, 29, 72, 17, 60, 75, 71, 97],
  [84, 37, 32, 62, 9, 51, 70, 71, 27, 24],
  [15, 93, 24, 7, 27, 72, 86, 23, 99, 14],
  [10, 69, 42, 43, 82, 14, 37, 5, 100, 28],
  [66, 48, 47, 27, 24, 4, 10, 6, 90, 44],
  [50, 68, 42, 44, 99, 55, 42, 50, 63, 44],
  [91, 28, 34, 16, 98, 88, 33, 89, 64, 74],
  [90, 87, 87, 73, 54, 6, 40, 91, 45, 99],
  [71, 85, 51, 70, 93, 42, 44, 93, 12, 40],
  [25, 65, 32, 24, 44, 42, 54, 44, 25, 55],
  [42, 66, 58, 67, 6, 6, 40, 98, 72, 14],
  [66, 46, 71, 38, 20, 60, 95, 72, 73, 97],
  [85, 60, 89, 96, 44, 100, 3, 3, 41, 5],
  [87, 93, 87, 6, 77, 3, 29, 79, 70, 91]]
# A = [0, 2, 8],[8, 2, 0],[0, 2, 8]
B = 1
elements_sum = 0
numrows = len(A)
numcols = len(A[0])
operations = 0
result = 0
for i in range(0+numrows):
	for j in range(0+numcols):
		result = result + A[i][j]
		if A[i][j] == 0:
			operations = operations + 1
		elif (A[i][j] % B == 0):
			operations = operations + (A[i][j]/B) - 1
		else:
			print(-1)
print(operations)
print(result)