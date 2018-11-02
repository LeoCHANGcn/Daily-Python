# -*- coding: utf-8 -*-
def checkio(data):
    return [i for i in data if data.count(i) > 1]

if __name__ == '__main__':
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
    assert checkio([1, 2, 3, 4, 5]) == []
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
