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

a = 5
b = 20  
if ( a and b ):
    print ("14 - 变量 a 和 b 都为 true");
else:
    print ("14 - 变量 a 和 b 有一个不为 true");
if ( a or b ):
    print ("15 - 变量 a 和 b 都为 true，或其中一个变量为 true");
else:
    print ("15 - 变量 a 和 b 都不为 true");
if not( a and b ):
    print ("16 - 变量 a 和 b 都为 false");
else:
    print ("16 - 变量 a 和 b 有一个不为 false");

a = 10
b = 20
print ("a & b 的值为：", a & b)
print ("a | b 的值为：", a | b)
print ("a ^ b 的值为：", a ^ b)
print ("~a 的值为：", ~a)
print ("a << 2 的值为：", a << 2)
print ("a >> 2 的值为：", a >> 2)

a = 5
b = 20
print ("a 的值为：", a)
a +=  b
print ("a += b 的值为：", a)
a -=  b
print ("a -= b 的值为：", a)
a *=  b
print ("a *= b 的值为：", a)
a /=  b
print ("a /= b 的值为：", a)
a = 5
a %=  b
print ("a %= b 的值为：", a)
a = 5
a **= b
print ("a **= b 的值为：", a)
a = 20
a //= b
print ("a //= b 的值为：", a)

a = 5
b = 20
if a is b:
    print ("17 - a 与 b 有相同的标识")
else:
    print ("17 - a 与 b 没有相同的标识")
b = a
if a is b:
    print ("18 - a 与 b 有相同的标识")
else:
    print ("18 - a 与 b 没有相同的标识")
if a is not b:
    print ("19 - a 与 b 没有相同的标识")
else:
    print ("19 - a 与 b 有相同的标识")

a = 5
b = 20
if a < b:
    print ("20 - a 小于 b")
else:
    print ("20 - a 不小于 b")
if b > a:
    print ("21 - b 大于 a")
else:
    print ("21 - b 不大于 a")
if a <= b:
    print ("22 - a 小于或等于 b")
else:
    print ("22 - a 大于或等于 b")
if b >= a:
    print ("23 - b 大于或等于 a")
else:
    print ("23 - b 小于或等于 a")

a = 10
b = 10  
print (a is b)
b = 20
print (a is b)
print (a is not b)








