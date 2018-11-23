# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 13:46:10 2018

@author: biao
算法思路：
1.初始化outlist[]
2.利用count判断该字符在str中出现了几次，大于1次则添加到outlist中
注：出现了一些错误，因为没有注意换行与每段前的空格
另外需要一些断言确保输入的为数字list，但是并没有写因为还不是很懂。。。
"""

def checkio(str):
    
    outlist = []
    
    for tempChar in str:
        
        if str.count(tempChar) > 1:
            
            outlist.append(tempChar)
            
    return outlist
