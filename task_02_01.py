def is_palindrome(s):
    res = False
    s2 = s.replace(' ', '')
    s3 = s2.replace(',', '')
    s_fin = s3.lower()
    if s_fin[::-1] == s_fin:
        res = True
    return res
