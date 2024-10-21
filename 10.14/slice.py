my_list = [1, 2, 3, 4, 5]
new_list = my_list[1:4]	# 下标1开始，下标4（不含）结束，步长1
print(new_list)


my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[:]	# 从头开始，到最后结束，步长1
new_tuple2 = my_tuple[1:4:-1]
print(new_tuple)
print(new_tuple2)

# 1. 序列的切片的数据类型无变化
# 2. 切片都用中括号
# 3. 区间左边右开[  )

