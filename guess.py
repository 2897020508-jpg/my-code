import random
number = random.randint(1,5)
guess = int(input("猜一个 1 到 5 的数字:"))
if guess > number:
    print("猜大了！")
elif guess < number:
    print("猜小了!")
else:
    print("猜对了!")