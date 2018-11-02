# -*- coding: utf-8 -*-
import string
def checkio(data):
    data=data.lower()
    return max(string.ascii_lowercase, key=data.count) 
if __name__ == '__main__':
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
    assert checkio("abe") == "a"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
