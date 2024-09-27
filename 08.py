# 从键盘获取输入的自然数n
n = int(input("请输入一个自然数n: "))

# 初始化求和变量sum为0
sum = 0

# 使用for循环进行累加
for i in range(1, n + 1):
    sum += i

# 输出计算结果
print(f"1 加到 {n} 的和为: {sum}")
