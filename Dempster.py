from collections import Counter

def permutations(A):
	def permutations(A):
		if len(A) == 0:
			return
		if len(A) == 1:
			yield A
		else:
			for i in range(1, len(A)):
				for p in permutations(A[i:]): # Pretend slicing is O(1)
					for q in permutations(A[:i]): # Pretend slicing is O(1)
						yield p + q # Pretend O(1)
						yield q + p # Pretend O(1)
	return set(permutations(A))

P = permutations((1, 2, 3))
C = Counter(P)
print(P)
print(C)