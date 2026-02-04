'''
整型(int) - 通常被称为是整型或整数，是正或负整数，
不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。

浮点型(float) - 浮点型由整数部分和小数部分组成，表示有小数的数值。浮点型在计算机中通常是用双精度来表示的，Python 的浮点数一般是 64 位双精度浮点数。

复数型(complex) - 复数由实数部分和虚数部分组成，虚数部分用字母 j 或 J 来表示。例如：3+5j 表示实数部分为 3，虚数部分为 5 的复数。在科学计算中经常会用到复数。
'''
#Python 支持四种不同的数值类型：整型(int)、浮点型(float)、复数型(complex)和布尔型(bool)。
# 整型
a = 10
print(type(a))  # <class 'int'>
# 浮点型
b = 3.14
print(type(b))  # <class 'float'>   
# 复数型
c = 2 + 3j
print(type(c))  # <class 'complex'>
# 布尔型
d = True
print(type(d))  # <class 'bool'>
# 数值类型转换
# 整型转换为浮点型
x = 5
y = float(x)
print(y)  # 5.0
print(type(y))  # <class 'float'>
# 浮点型转换为整型
x = 5.99
y = int(x)
print(y)  # 5
print(type(y))  # <class 'int'>
# 整型转换为复数型
x = 5
y = complex(x)
print(y)  # (5+0j)
print(type(y))  # <class 'complex'>
# 布尔型转换为整型
x = True
y = int(x)
print(y)  # 1
print(type(y))  # <class 'int'>
# 布尔型转换为浮点型
x = False
y = float(x)
print(y)  # 0.0
print(type(y))  # <class 'float'>
# 布尔型转换为复数型
x = True
y = complex(x)
print(y)  # (1+0j)
print(type(y))  # <class 'complex'>
'''
数学函数
函数	返回值 ( 描述 )
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)

如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃，使用 (x>y)-(x<y) 替换。
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	以浮点数形式返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	
返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。

其实准确的说是保留值将保留到离上一位更近的一端。

sqrt(x)	返回数字x的平方根。

随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：

函数	描述
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

三角函数
Python包括以下三角函数：

函数	描述
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度

数学常量
常量	描述
pi	数学常量 pi（圆周率，一般以π来表示）
e	数学常量 e，e即自然常数（自然常数）。
'''
