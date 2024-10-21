# 定义一个空集合
unique_elements = set()

# 原始列表
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']

# 通过for循环遍历列表
for item in my_list:
    # 在for循环中将列表的元素添加至集合
    unique_elements.add(item)

# 最终得到元系去重后的集合对象，并打印输出
print(unique_elements)
