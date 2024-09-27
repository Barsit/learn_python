# 定义全局变量
money = 5000000
name = input("请输入您的姓名: ")


def check_balance():
    """查询余额"""
    print(f"{name}，您的当前余额为：{money}")


def deposit(amount):
    """存款"""
    global money
    money += amount
    print(f"{name}，您已成功存入 {amount} 元，当前余额为：{money}")


def withdraw(amount):
    """取款"""
    global money
    if amount > money:
        print(f"{name}，您的余额不足！")
    else:
        money -= amount
        print(f"{name}，您已成功取出 {amount} 元，当前余额为：{money}")


def main_menu():
    """主菜单"""
    while True:
        print("\n欢迎使用银行系统")
        print("1. 查询余额")
        print("2. 存款")
        print("3. 取款")
        print("4. 退出")

        choice = input("请选择操作 (1/2/3/4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = int(input("请输入存款金额: "))
            deposit(amount)
        elif choice == '3':
            amount = int(input("请输入取款金额: "))
            withdraw(amount)
        elif choice == '4':
            print("感谢使用本系统，再见！")
            break
        else:
            print("输入错误，请重新输入！")


# 启动主菜单
main_menu()
print(money)
