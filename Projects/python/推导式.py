'''
Docstring for python.推导式

Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

Python 推导式是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。

在使用推导式时，需要注意可读性，尽量保持表达式简洁，以免影响代码的可读性和可维护性。

Python 支持各种数据结构的推导式：

列表(list)推导式
字典(dict)推导式
集合(set)推导式
元组(tuple)推导式

列表推导式格式为：
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]

或者 

[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]

out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值。

字典推导基本格式：
{ key_expr: value_expr for value in collection }

或

{ key_expr: value_expr for value in collection if condition }


集合推导式基本格式：
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }

元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。

元组推导式基本格式：
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )
'''

list1 = ['python', 'test1', 'test2']
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1]
print(list2)