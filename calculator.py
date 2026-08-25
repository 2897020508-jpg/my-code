def add(a, b):
    return a + b
def sud(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
while True:
    print()
    print("1.加法 2.减法 3.乘法 4.除法  5.退出")
    choice = input("选一个(输入数字): ")
    if choice == "5":
        print("拜拜! ")
        break
    x =int(input("第一个数: "))
    y =int(input("第二个数: "))
    if choice == "1":
        print("结果: ", add(x, y))
    elif choice == "2":
        print("结果: ", sud(x, y))
    elif choice == "3":
        print("结果: ", mul(x, y))
    elif choice == "4":
        print("结果: ", div(x, y))
    else:
        print("看不懂,重新选择")


