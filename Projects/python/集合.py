'''
Docstring for python.集合
'''
'''
集合（set）是一个无序的不重复元素序列。

集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。

set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合

s.add( x ) # 将元素 x 添加到集合 s 中，如果 x 已经存在于集合中，则不进行任何操作。
s.update( x ) # 将可迭代对象 x 中的所有元素添加到集合 s 中，如果 x 中的元素已经存在于集合中，则不进行任何操作。
s.remove( x ) # 从集合 s 中移除元素 x，如果 x 不存在于集合中，则会引发 KeyError 异常。
s.discard( x ) # 从集合 s 中移除元素 x，如果 x 不存在于集合中，则不进行任何操作。
s.clear() # 移除集合 s 中的所有元素，使其成为一个空集合
len(s) # 返回集合 s 中元素的数量
x in s # 判断元素 x 是否存在于集合 s 中，返回 True 或 False
'''

'''
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
len()	计算集合元素个数
'''