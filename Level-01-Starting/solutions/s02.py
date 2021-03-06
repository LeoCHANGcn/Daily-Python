import re
def checkio(text: str) -> str:

    #replace this for solution
    text = str.lower(text)
    text = "".join(c for c in re.findall('[a-zA-Z]+', text))
    count = {}
    for c in text:
        count[c] = count[c] + 1 if c in count else 0
    
    count = min(count, key=lambda x: (-count[x], x))
    return count

if __name__ == '__main__':
    print("Example:")
    print(checkio("AAaooo!!!!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")