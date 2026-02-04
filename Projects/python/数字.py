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