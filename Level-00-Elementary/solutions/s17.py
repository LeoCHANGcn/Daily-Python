def checkio(str_number: str, radix: int) -> int:
    map_dict1 = dict(zip([chr(item) for item in range(65, 97)],range(10, 37)))
    map_dict2 = dict(zip([str(item) for item in range(10)], range(10)))
    map_dict = dict(map_dict1, **map_dict2)
    result = 0
    count = 0
    for i, e in enumerate( str_number):
        if map_dict[e] >= radix:
            return -1
        else:
            result += radix**(len(str_number)-i -1)*map_dict[e]
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
