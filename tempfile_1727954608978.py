def make_sandwich(*toppings):
    print("制作中的三明治将包含以下食材:")
    for topping in toppings:
        print(f"- {topping}")
    print("\n")

if __name__ == '__main__':
# 调用函数三次，每次提供不同数量的食材
    make_sandwich('火腿', '奶酪')
    make_sandwich('生菜', '番茄', '黄瓜', '鸡蛋')
    make_sandwich('鸡肉', '辣椒酱', '洋葱', '蘑菇', '鳄梨')
