# 1. 定义列表并用变量接收
ages = [21, 25, 21, 23, 22, 20]

# 2. 追加一个数字31到列表尾部
ages.append(31)

# 3. 追加一个新列表[29, 33, 30]到列表尾部
ages.extend([29, 33, 30])

# 4. 取出第一个元素
first_age = ages[0]

# 5. 取出最后一个元素
last_age = ages[-1]

# 6. 查找元素31在列表中的下标位置
index_of_31 = ages.index(31)

# 打印结果以验证
print("原始列表:", ages)
print("第一个元素:", first_age)
print("最后一个元素:", last_age)
print("元素31的位置:", index_of_31)
