import itertools
import enchant
print("Enter the outer circle letters")
letters = list(input().split())
print("Enter middle letter")
mid = input()
D = enchant.Dict("en_US")
Dx = enchant.Dict("en_UK")
words = []
n = len(letters)
for i in range(2**n):
	curlist = []
	for j in range(n):
		if(i & (1 << j)):
			curlist.append(letters[j])
	if len(curlist) < 3:
		continue
	curlist.append(mid)
	for perm in itertools.permutations(curlist):
		r = "".join(perm)
		if D.check(r) or Dx.check(r):
			words.append(r)
words = set(words)
print(words, end = '\n')
