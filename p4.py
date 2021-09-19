# wapp to keep a track on count of letters
# in the given word
# kkammmmallll {'k':2, 'a':2, 'm':3, 'l':3}

word = input(" enter a word ") 
lc = {}

for w in word:
	co = lc.get(w)
	if co is None:
		lc[w] = 1
	else:
		lc[w] = co + 1 

print(lc)

for i in lc:
	print(i)
	print(l, lc[1])
	