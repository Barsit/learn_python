a = int(input("请输入一个数"))
n = int(input("请输入求和次数"))

b = a
sum = a
for i in range(1, n+1):
    b = b + a *10 ** i
    sum += b
    print(b)
print(sum)