#!/usr/bin/env python
#coding=utf-8
#__author__='David Chung'

import collections

matrix=[[(1,2,3,4,5),(3,8)],[(2,3,4,5,6),(3,10)]]


all_front=[]
for i in matrix:
    all_front.extend(i[0])

print(all)

print(dict(Counter(all)))


