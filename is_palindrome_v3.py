def is_palindrome_v3(s):
	""" (str) -> bool
	Return True in and only if s is a palindrome.
	
	>>> is_palindrome_v1('noon')
	True

	"""

	i = 0;
	j = len(s)-1

	while i< j and s[i] ==s[j]:
		i = i+1
		j = j-1

	return j <= i


print(is_palindrome_v3('noon')) 
