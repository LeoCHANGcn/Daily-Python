# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 16:46:53 2018

@author: Jairo
"""

def checkio(data: str) -> bool:

    num = len(data)
    digitNum= 0
    lowerNum = 0
    upperNum = 0
    
    for i in range(len(data)):
        if data[i].isdigit():
            digitNum = digitNum + 1
        if data[i].islower():
            lowerNum = lowerNum + 1
        if data[i].isupper():
            upperNum = upperNum + 1
    
    if num >= 10 and digitNum * lowerNum * upperNum > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
