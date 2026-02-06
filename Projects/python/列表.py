#!/usr/bin/python3

list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[0] )
print( list[1] )
print( list[2] )

#!/usr/bin/python3

list = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print( list[-1] ) #black 
print( list[-2] ) #white
print( list[-3] ) #yellow

#!/usr/bin/python3

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(nums[0:4]) #[10, 20, 30, 40]从下标为0开始取，到下标为4结束，但不包括下标4

#!/usr/bin/python3

list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]

# 读取第二位
print ("list[1]: ", list[1])
# 从第二位开始（包含）截取到倒数第二位（不包含）
print ("list[1:-2]: ", list[1:-2])

#!/usr/bin/python3

list = ['Google', 'Runoob', 1997, 2000]

print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)

#!/usr/bin/python3
 
list = ['Google', 'Runoob', 1997, 2000]
 
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)
'''
Python 表达式	                          结果	                            描述
len([1, 2, 3])	                           3	                           长度
[1, 2, 3] + [4, 5, 6]	          [1, 2, 3, 4, 5, 6]	                   组合
['Hi!'] * 4	                 ['Hi!', 'Hi!', 'Hi!', 'Hi!']	               重复
3 in [1, 2, 3]	                         True	                      元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	                           迭代
'''

'''
1	len(list)   列表元素个数
2	max(list)   返回列表元素最大值
3	min(list)   返回列表元素最小值
4	list(seq)   将元组转换为列表
'''

'''
1	list.append(obj)                       在列表末尾添加新的对象
2	list.count(obj)                        统计某个元素在列表中出现的次数
3	list.extend(seq)                       在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)                        从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)                将对象插入列表
6	list.pop([index=-1])                   移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)                       移除列表中某个值的第一个匹配项
8	list.reverse()                         反向列表中元素
9	list.sort( key=None, reverse=False)    对原列表进行排序
10	list.clear()                           清空列表
11	list.copy()                            复制列表
'''