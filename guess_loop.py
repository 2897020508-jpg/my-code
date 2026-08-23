import random
number = random.randint(1,10)
count = 0
while True:
    guess = int(input("猜一个 1 到 10 的数字:"))
    count =count + 1
    if guess > number:
        print("猜大了!")
    elif guess < number:
        print("猜小了!")
    else:
        print("猜对了!你一共猜了",count,"次")
        break