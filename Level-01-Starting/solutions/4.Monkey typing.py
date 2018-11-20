# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:27:50 2018

@author: biao

算法思路：
1.定义函数 count_words(str,word)
2.初始化计数器 count=0,将str全部转换成小写字符
3.依次检验每个word在str中的个数，若大于0，则count+1

"""

def count_words(str,word):
    
    count = 0
    str = str.lower()
    
    for i in word:
        if str.count(i):
            count+=1
    return count
    