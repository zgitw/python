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

a = 0x00111100
b = 0x00001101
print ("a & b = ", a & b)
print ("a | b = ", a | b)   
print ("a ^ b = ", a ^ b)
print ("~a = ", ~a)
print ("a << 2 = ", a << 2) 
print ("a >> 2 = ", a >> 2)
a = 60      # 60 = 0011 1100 
b = 13      # 13 = 0000 1101
print ("a & b = ", a & b) # 12 = 0000 1100
print ("a | b = ", a | b) # 61 = 0011 1101
print ("a ^ b = ", a ^ b) # 49 = 00110001
print ("~a = ", ~a)       # -61 = 1100 0011
print ("a << 2 = ", a << 2) # 240 = 111 10000
print ("a >> 2 = ", a >> 2) # 15 = 0000 1111    

#!/usr/bin/python3
 
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b        # 12 = 0000 1100
print ("1 - c 的值为：", c)
 
c = a | b        # 61 = 0011 1101 
print ("2 - c 的值为：", c)
 
c = a ^ b        # 49 = 0011 0001
print ("3 - c 的值为：", c)
 
c = ~a           # -61 = 1100 0011
print ("4 - c 的值为：", c)
 
c = a << 2       # 240 = 1111 0000
print ("5 - c 的值为：", c)
 
c = a >> 2       # 15 = 0000 1111
print ("6 - c 的值为：", c)


#!/usr/bin/python3
 
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")
 
# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")

#!/usr/bin/python3
 
a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")

#!/usr/bin/python3
 
a = 20
b = 10
c = 15
d = 5
e = 0
 
e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("(a + b) * c / d 运算结果为：",  e)
 
e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("((a + b) * c) / d 运算结果为：",  e)
 
e = (a + b) * (c / d)    # (30) * (15/5)
print ("(a + b) * (c / d) 运算结果为：",  e)
 
e = a + (b * c) / d      #  20 + (150/5)
print ("a + (b * c) / d 运算结果为：",  e)

x = True
y = False
z = False
 
print("情况1：默认优先级（先算and）")
if x or y and z:  # 等同于 x or (y and z)
    print("yes")  # 会输出
else:
    print("no")
 
print("\n情况2：强制改变优先级（先算or）")
if (x or y) and z:  # 人为添加括号改变顺序
    print("yes")  # 不会输出
else:
    print("no")  # 会输出
