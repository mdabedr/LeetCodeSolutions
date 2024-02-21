def myAtoi( s: str) -> int:
    # s="4193 with words"
    number=0
    sign=1
    for i in s:
        if i==' ':
            continue
        if i=='-':
            sign=-1
            continue
        if i=='+':
            sign=1
            continue
        if not (ord(i)-48>=0 and ord(i)-48<=9):
            break
        number=number*10+(int(i))
    if number>0:
        number=number*sign

    if number<(-2<<30):
        number=-2<<30
    if number>(2<<30-1):
        number=2<<30-1
    return number


