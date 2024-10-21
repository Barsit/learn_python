# 定义一个人名，并在其开头和末尾添加空白字符
name = "\t\n  john doe  \n\t"

# 打印原始的人名
print(name)
print("原始人名:")
print(repr(name))  # 使用 repr 函数显示字符串中的转义字符

# 使用 lstrip() 去除左边的空白字符
left_stripped_name = name.lstrip()
print("\n去除左边空白后的名字:")
print(repr(left_stripped_name))

# 使用 rstrip() 去除右边的空白字符
right_stripped_name = name.rstrip()
print("\n去除右边空白后的名字:")
print(repr(right_stripped_name))

# 使用 strip() 同时去除左右两边的空白字符
stripped_name = name.strip()
print("\n去除左右两边空白后的名字:")
print(repr(stripped_name))
