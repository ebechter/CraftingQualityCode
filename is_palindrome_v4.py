def is_palindrome_v4(s):
   
    for i in range(len(s) // 2):
      if s[i] != s[len(s) - i]:
        return False

    return True
