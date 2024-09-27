# 输入三角形的三个边长
a = float(input("请输入三角形的第一条边长: "))
b = float(input("请输入三角形的第二条边长: "))
c = float(input("请输入三角形的第三条边长: "))

# 判断是否能构成三角形
if a + b > c and a + c > b and b + c > a:
    # 判断三角形的类型
    if a == b == c:
        print("这是一个等边三角形。")
    elif a == b or a == c or b == c:
        print("这是一个等腰三角形。")
    else:
        print("这是一个普通三角形。")
else:
    print("输入的边长无法构成三角形。")
