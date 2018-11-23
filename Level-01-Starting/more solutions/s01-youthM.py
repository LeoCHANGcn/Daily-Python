# -*- coding: utf-8 -*-
def checkio(data):
    #replace this for solution
    import re
    flag = False
    r1 = re.search('[a-z]+',data)
    r2 = re.search('[A-Z]+',data)
    r3 = re.search("[0-9]+",data)
    r4 = re.search("\w{10,}",data)
    r5 = len(data) >= 10
    if r1 and r2 and r3 and r4 and r5:
        flag = True
    return flag

#Some hints
#Just check all conditions

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
