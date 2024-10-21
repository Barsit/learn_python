from win32api import Sleep
with open(r'python.txt', 'r',encoding='utf-8') as f:
    print(f.readline())
    print(f.readlines())
   