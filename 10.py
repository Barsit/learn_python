# 提示用户输入数字 a 和项数 n
a = int(input("请输入一个 1~9 之间的数字 a: "))
n = int(input("请输入项数 n (不超过10): "))

# 初始化结果变量
s = 0

# 计算每一项的值并累加
for i in range(1, n + 1):
    # 构造当前项的字符串形式
    current_str = str(a) * i
    print(current_str)
    # 将字符串转换为整数并累加
    s += int(current_str)

# 输出最终结果
print(f"计算结果为: {s}")

