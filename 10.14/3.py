# 1. 创建一个包含五种简单食品的元组
foods = ("汉堡", "披萨", "沙拉", "三明治", "薯条")

# 2. 使用 for 循环打印这些食品
print("原始菜单:")
for food in foods:
    print(food)

# 3. 尝试修改元组中的一个元素
try:
    foods[0] = "寿司"
except TypeError as e:
    print("\n尝试修改元组中的元素时出现错误:")
    print(e)

# 4. 替换元组中的两种食品
# 重新创建一个新的元组
new_foods = ("寿司", "披萨", "沙拉", "寿司卷", "薯条")

# 使用 for 循环打印新元组的每个元素
print("\n新菜单:")
for food in new_foods:
    print(food)
