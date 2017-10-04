def is_palindrome(s):
    res = False
    sstr = str(s)
    s2 = s.replace(' ', '')

    bad_chars = {33: None, 
    34: None,
    44: None,
    45: None,
    46: None,
    47: None,
    58: None,
    59: None,
    63: None,
    96: None,
    145: None,
    146: None,
    150: None,
    151: None,
    192: None,
    222: None
}

    s3 = s2.translate(bad_chars)
    s_fin = s3.lower()
    if s_fin[::-1] == s_fin:
        res = True
    return res
