#!/user/bin/env python3
def reverse(s):
	rev=""
	for i in range(len(s),-1,-1):
		rev = rev + s[i]

	return rev

reverse("Algodaily")
