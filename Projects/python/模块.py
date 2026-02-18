'''
Docstring for python.模块

在前面的几个章节中我们基本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。

为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。

Python 中的模块（Module）是一个包含 Python 定义和语句的文件，文件名就是模块名加上 .py 后缀。

模块可以包含函数、类、变量以及可执行的代码。通过模块，我们可以将代码组织成可重用的单元，便于管理和维护。

模块的作用
代码复用：将常用的功能封装到模块中，可以在多个程序中重复使用。

命名空间管理：模块可以避免命名冲突，不同模块中的同名函数或变量不会互相干扰。

代码组织：将代码按功能划分到不同的模块中，使程序结构更清晰。

下面是一个使用 python 标准库中模块的例子。

1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
2、sys.argv 是一个包含命令行参数的列表。
3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
'''

#!/usr/bin/python3
# 文件名: using_sys.py
 
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')

'''
import 语句
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1[, module2[,... moduleN]

当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
搜索路径时一个解释器会先进行搜索的所有目录的列表。如想要导入模块 support，需要把命令放在脚本的顶端：
'''
#!/usr/bin/python3
# Filename: support.py
 
def print_func( par ):
    print ("Hello : ", par)
    return

#test.py 引入 support 模块：
#!/usr/bin/python3
# Filename: test.py
 
# 导入模块
import support
 
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

'''
一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。

当我们使用 import 语句的时候，Python 解释器是怎样找到对应的文件的呢？

这就涉及到 Python 的搜索路径，搜索路径是由一系列目录名组成的，Python 解释器就依次从这些目录中去寻找所引入的模块。

模块的搜索路径
当导入一个模块时，Python 会按照以下顺序查找模块：

当前目录。

环境变量 PYTHONPATH 指定的目录。

Python 标准库目录。

.pth 文件中指定的目录。

# 斐波那契(fibonacci)数列模块
 
def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
 
def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

然后进入Python解释器，使用下面的命令导入这个模块：
import fibo
这样做并没有把直接定义在fibo中的函数名称写入到当前符号表里，只是把模块fibo的名字写到了那里。

可以使用模块名称来访问函数：
fibo.fib(1000)
'''

'''
__name__ 属性
一个模块被另一个程序第一次引入时，其主程序将运行。

如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行。

#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

'''

'''
Python 本身带着一些标准的模块库，在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。

模块名	功能描述
math	数学运算（如平方根、三角函数等）
os	操作系统相关功能（如文件、目录操作）
sys	系统相关的参数和函数
random	生成随机数
datetime	处理日期和时间
json	处理 JSON 数据
re	正则表达式操作
collections	提供额外的数据结构（如 defaultdict、deque）
itertools	提供迭代器工具
functools	高阶函数工具（如 reduce、lru_cache）
'''