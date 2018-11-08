def checkio(text:str) -> str:
    text = str.lower(text)
    lowstr=set(text)
    order_str=list(lowstr)
    order_str=sorted(order_str)
    chstr=[]
    k=[]
    j=0
    for c in order_str:
            if(c>='a' and c<='z'):
	            k.append(text.count(c))
	            chstr.append(c)
    if(chstr==[]):return ''  #若字符串中无字母，则返回空字符
    maxnum=max(k)
    j=k.index(maxnum)
    return chstr[j]

if __name__ == '__main__':
    print("Example:")
    print(checkio("AAaooo!!!!"))

    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
