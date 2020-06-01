#!/usr/bin/env python3

import re

a = re.findall(r'[a-c].','abcd')
# we can use () in pattern as capturing group then access the with index.0 index always is pattern as hole and other indexes are capturing group respectively
b = re.findall(r'([a-c]).','abcd')
c = re.findall(r'([a-c])(.)','abcd')
# for regex pattern use r''
# use \ for scaping special char like +,*,.
# ^ start of the line
# $ end of the line
# \b \b  block of word
# \w upper,lower,underscore
# \d numbers
# * zero or more
# + one or more
# . every char
# ? one or zero
# {5} 5 times repetion
# {2,3} 2 or 3 times
# {5, } 5 or more
# {,5} zero to 5
# {5,} 5 or more
# [ac] a or c
# in [] chars does'nt have special meaning like *,+,. 
# cat|dog cat or dog

# split in regex is like split in string but with pattern as delimiter
# split when ocuring the pattern
re.split(r'[.?!]','salam! I\'m happy. how are you?')
# if we put chars in ()  then the pattern also returned
re.split(r'([.?!])','salam! I\'m happy. how are you?')

# sub in regex is like replace in string
re.sub(r'Amir','Good boy','Amir go to school!')
# we can use capturing group to use them in replaced string
re.sub(r'(\w+),(\w+)',r'\2 \1','Amir,Nikpour')
