bin_chars = ['0', '1']
oct_chars = ['0', '1', '2', '3', '4', '5', '6', '7']
dec_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
hex_chars = ['A', 'B', 'C', 'D', 'E', 'F']

def dec2bin(number):
    flag = True
    fstr = str(number)
    flst = list(fstr)

    for i in flst:
        if i not in dec_chars:
            flag = False

    if flag:
        lst = []
    
        while number > 1:
            lst.append(str(number % 2))
            number = number // 2
        lst.append(str(number % 2))

        flst = lst[::-1]
    
        return ''.join(flst)
   

def dec2oct(number):
    flag = True
    fstr = str(number)
    flst = list(fstr)

    for i in flst:
        if i not in dec_chars:
            flag = False

    if flag:
        lst = []
    
        while number > 7:
            lst.append(str(number % 8))
            number = number // 8
        lst.append(str(number % 8))

    
        flst = lst[::-1]
    
        return ''.join(flst)
    

def dec2hex(number):
    flag = True
    fstr = str(number)
    flst = list(fstr)

    for i in flst:
        if i not in dec_chars:
            flag = False

    if flag:
        lst = []
        lst_fin = []
    
        while number > 15:
            lst.append(str(number % 16))
            number = number // 16
        lst.append(str(number % 16))

        flst = lst[::-1]

        rev_hex_keys = {
            '0': '0',
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4',
            '5': '5',
            '6': '6',
            '7': '7',
            '8': '8',
            '9': '9',
            '10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F'
        }

        for i in flst:
            lst_fin.append(rev_hex_keys.get(i))

        return ''.join(lst_fin)


def bin2dec(number):
    fstr = str(number)
    flst = list(fstr)
    res = 0
    flag = True

    for i in flst:
        if i not in bin_chars:
            flag = False
    
    if flag:
        for i in range(len(flst)):
            res += int(flst[i]) * 2 ** (len(flst) - (i + 1)) 

        return res


def oct2dec(number):
    fstr = str(number)
    flst = list(fstr)
    res = 0
    flag = True

    for i in flst:
        if i not in oct_chars:
            flag = False
    
    if flag:
        for i in range(len(flst)):
            res += int(flst[i]) * 8 ** (len(flst) - (i + 1)) 

        return res


def hex2dec(number):
    fstr = str(number)
    flst = list(fstr)
    res = 0
    flag = True

    def myint(elem):
       
        hex_keys = {
            65: '10',
            66: '11',
            67: '12',
            68: '13',
            69: '14',
            70: '15'
        }
        return elem.translate(hex_keys)

    for i in flst:
        if (i not in dec_chars) and (i not in hex_chars):
            flag = False
    
    if flag:
        for i in range(len(flst)):
            res += int(myint(flst[i])) * 16 ** (len(flst) - (i + 1)) 

        return res




if __name__ == '__main__':
    print(dec2bin(250), dec2oct(250), dec2hex(250))
    print(bin2dec("1010011010"))
    print(oct2dec("755"))
    print(hex2dec("ABCDEF"))