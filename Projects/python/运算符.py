#!/usr/bin/python3
 
a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的值为：", c);

c = a - b
print ("2 - c 的值为：", c);

c = a * b
print ("3 - c 的值为：", c);

c = a / b
print ("4 - c 的值为：", c);

c = a % b
print ("5 - c 的值为：", c);

a = 2
b = 3
c = a**b
print ("6 - c 的值为：", c);

a = 10
b = 3
c = a//b
print ("7 - c 的值为：", c);

a = 21 
b = 10

if ( a == b ):
    print ("8 - a 等于 b")
else:
    print ("8 - a 不等于 b");  
if ( a != b ):
    print ("9 - a 不等于 b");
else:
    print ("9 - a 等于 b");
if ( a < b ):
    print ("10 - a 小于 b");
else:
    print ("10 - a 不小于 b");
if ( a > b ):
    print ("11 - a 大于 b");
else:
    print ("11 - a 不大于 b");
if ( a <= b ):
    print ("12 - a 小于或等于 b");
else:
    print ("12 - a 大于或等于 b");
if ( a >= b ):
    print ("13 - a 大于或等于 b");
else:
    print ("13 - a 小于或等于 b");