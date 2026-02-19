'''
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：

d = {key1 : value1, key2 : value2, key3 : value3 }

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
'''
emptyDict = dict()
 
# 打印字典
print(emptyDict)
 
# 查看字典的数量
print("Length:",len(emptyDict))
 
# 查看类型
print(type(emptyDict))

#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("tinydict['Name']: ", tinydict['Name'])
print ("tinydict['Age']: ", tinydict['Age'])

#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8                # 更新 Age
tinydict['School'] = "菜鸟教程"    # 添加信息
 
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])
print ("tinydict: ", tinydict);

#!/usr/bin/python3
 
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del tinydict['Name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

'''
1	dict.clear()删除字典内所有元素
2	dict.copy()返回一个字典的浅复制
3	dict.fromkeys()创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	dict.get(key, default=None)返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	key in dict如果键在字典dict里返回true，否则返回false
6	dict.items()以列表返回一个视图对象
7	dict.keys()返回一个视图对象
8	dict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)把字典dict2的键/值对更新到dict里
10	dict.values()返回一个视图对象
11	dict.pop(key[,default])删除字典 key（键）所对应的值，返回被删除的值。
12	dict.popitem()返回并删除字典中的最后一对键和值。
'''