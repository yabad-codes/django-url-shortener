import string

BASE62 = string.digits + string.ascii_lowercase + string.ascii_uppercase

def base62_encode(num):
	"""Encodes a number in Base62."""
	if num == 0:
		return BASE62[0]
	b62 = ''
	while num:
		num, rem = divmod(num, 62)
		b62 += BASE62[rem]
	return b62[::-1]

def base62_decode(b62_str):
	"""Decodes a Base62 string to a number."""
	num = 0
	for char in b62_str:
		num = num * len(BASE62) + BASE62.index(char)
	return num