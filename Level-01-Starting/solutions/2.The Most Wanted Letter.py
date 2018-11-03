'''
这个程序比较关键的三个函数:
    1.str.lower()  将str中所有字符转换为小写字符
    2.str.count(tempChar)  统计str字符串中tempChar字符的个数
    3.sorted(mainList,key=lambda mainList : (-mainList[-1], mainList[0]))
    排序函数。
    sorted可对所有可迭代list排序，包括字母表。
    sorted不会改变原有list，key后面可自定义排序规则，本题中即找到其中那个出现最多的字母
    如果找到两个或两个以上出现频率相同的字母，那么返回字母表中靠前的那个。
    
    程序来源：https://blog.csdn.net/u013355826/article/details/78786719

'''
def checkio(Str):

    mainList = [] 

    checkList = []

    str = Str.lower()    #将所有字符转换成小写

    for tempChar in str:   #依次读取str中的每个字符，存在tempChar中

        tempList = []   #每次循环前初始化templist，templist的格式为[字符，字符出现的次数]

        if not(tempChar in checkList) and tempChar.isalpha(): 
            #前句判断该字符是否不在checklist中；isalpha()检测该字符是不是字母    

            checkList.append(tempChar)  # append() 将该字符添加到checklist尾部

            tempList.append(tempChar)   # append() 将该字符添加到templist尾部

            tempList.append(str.count(tempChar))
            #用count()统计该字母在str中出现的次数 并添加到templist尾部

            mainList.append(tempList)  #将每个字符和它出现的次数添加到mainlist中
    
    print(mainList) #打印排序前的mainlist
  

    mainList = sorted(mainList,key=lambda mainList : (-mainList[-1], mainList[0]))    
    #对mainlist排序 sorted不会改变原来的List。 key代表自定义排序，这里是根据每个数组第2个元素倒序排序，第二个元素相同则按第一个元素排序
    print(mainList)     #打印排序后的mainlist

    a = mainList[0][0] #读取排序后的mainlist第一个数组的第一个元素

    return a 
