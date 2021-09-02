# -*- coding: UTF-8 -*-

from numpy import *
import matplotlib
import matplotlib.pyplot as pyplot
import kNN

fig = pyplot.figure()
ax = fig.add_subplot(111)
datingDataMat,datingLabels = kNN.file2matrix('/Users/fengxing/Documents/workspace/wangxutech/git/books/机器学习实战/source code/Ch02/datingTestSet2.txt')
print(datingDataMat)
print(datingLabels)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-2,25,-0.2,2.0])
pyplot.xlabel('Percentage of Time Spent Playing Video Games')
pyplot.ylabel('Liters of Ice Cream Consumed Per Week')
pyplot.show()