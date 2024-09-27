# 写一个程序，接收用户输入两个整数，计算它们的和、差、积、商、余数
# 用户输入两个整数
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))

# 计算和、差、积、商、余数
和 = num1 + num2
差 = num1 - num2
积 = num1 * num2
商 = num1 // num2  # 使用整数除法
余数 = num1 % num2

# 输出结果
print(f"{num1} 和 {num2} 的和为: {和}")
print(f"{num1} 和 {num2} 的差为: {差}")
print(f"{num1} 和 {num2} 的积为: {积}")
print(f"{num1} 和 {num2} 的商为: {商}")
print(f"{num1} 和 {num2} 的余数为: {余数}")
