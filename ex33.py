#!usr/bin/python
# -*- coding: utf-8 -*-
def test(x ,y):
    i = 0
    j=x
    numbers = []

    while i < j:
        print "At the top i is %d" % i
        numbers.append(i)
    
        i += y
        print "Numbers now:" , numbers
        print "At the bottom i is %d" % i
    
    print "The numbers:"
    
    for num in numbers:
        print num



test(100, 5)
