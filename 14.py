def calculate_sum(a, n):
    """
    计算 s = a + aa + aaa + ... 的值，其中 a 是 1 到 9 之间的数字，n 是项数。

    :param a: int, 1 到 9 之间的数字
    :param n: int, 项数
    :return: int, 计算结果
    """
    s = 0

    for i in range(1, n + 1):
        # 构造当前项的字符串形式
        current_str = str(a) * i
        print(current_str)
        # 将字符串转换为整数并累加
        s += int(current_str)

    return s


# 输入 a 和 n
a = int(input("请输入数字 a (1-9): "))
n = int(input("请输入项数 n (不超过10): "))

# 调用函数并输出结果
result = calculate_sum(a, n)
print(f"计算结果为: {result}")

