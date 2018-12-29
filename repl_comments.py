# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

i=0
yorumlar=[]
numara = 1

while i==0:
    yorum= [input("Please leave a comment: ")]
    yorumlar = yorumlar + yorum
    print("All previous comments of yours: \n")
    for c in yorumlar:
        print(str(numara) + "- " + str(c) +  "\n")
        numara = numara + 1
    numara=1
    l= input("Leave or stay?(Type 'L' or 'l' to leave, type anything else(or just press enter) to stay): ")
    if l=="L" or l=="l":
        break
    