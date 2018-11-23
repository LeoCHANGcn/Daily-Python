# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:37:45 2018

@author: biao

算法思路:
    1.给出所有的特征数字与其对应的罗马数字表
    2.检测输入的num,如果输入的数字大于数字表中的第i个数字，则减去它，并记录下对应的罗马数字
    3.
"""

def checkio(num):
    nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    pos = 0
    res = ""
    
    
    
    while num !=0:
        while num < nums[pos]:
            pos+=1
            num = num - nums[pos]
            res+=romans[pos]
    
    return res
