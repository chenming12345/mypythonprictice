#!/usr/bin/python
# -*- coding: utf-8 -*-
def build_lamp(x):
    """ define 100 lamps """
    lamp = []
    for i in range(0,x):
        lamp.append(False)
    return lamp


def turn_lamp(lamp, x):
    """turn on and turn off the light"""
    k = int(x)+1
    for i in range(1, k):
        for j in range(1, k):
            if i%j == 0:
                lamp[i-1]= not lamp[i-1]
    return lamp

def print_lamp(lamp, x):
    """print the opening lamp"""
    for i in range(0,x):
        if lamp[i]:
            print "the lamp %r is open." % (i+1)

lamp = build_lamp(100)
result = turn_lamp(lamp, 100)
print_lamp(result,100)


