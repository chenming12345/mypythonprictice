#!/usr/bin/python
#-*utf-8*-#
from sys import argv
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is :", first
print "Your second variable is:" , second
print "Your third variable is:" , third
print "what would u like to change the first argument?",
first = raw_input()
print "what would u like to change the second argument?",
second = raw_input()
print "what would u like to change the third argument?",
third = raw_input()
print "Your first variable is :", first
print "Your second variable is:" , second
print "Your third variable is:" , third