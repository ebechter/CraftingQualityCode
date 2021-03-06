def is_palindrome_v1(s):
	""" (str) -> bool
	Return True in and only if s is a palindrome.
	
	>>> is_palindrome_v1('noon')
	True

	"""
	return reverse(s) == s




def reverse(s):
	"""(str) -> str
	
	Return a reversed version of s.
	
	>>> reverse('hello')
	'olleh'
	>>> reverse('a')
	'a'
	"""
	rev = ''

	# For each character in s, add that car to the beginning of rev. 
	for ch in s:
		rev = ch+rev

	return rev

print(is_palindrome_v1('noon'))