def xxx(s):
    # 初始化计数器
    count = 0
    # 遍历字符串中的每个字符
    for _ in s:
        # 每遇到一个字符，计数器加一
        count += 1
    # 返回最终计数结果
    return count

s1 = 'hello world'
s2 = 'python'
result = xxx(s2)

print(result)


def add(x, y):
    """
    两数相加
    :param x:加数1
    :param y:加数2
    :return: 返回相加的结果
    """
    return x+y