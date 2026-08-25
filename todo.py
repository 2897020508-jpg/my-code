todos = []

def show_todos():
    print()
    print("待办清单(现在有", len(todos), "件)")
    for i in range(len(todos)):
        print(i + 1, ".", todos[i])

while True:
    show_todos()
    action = input("add 添加 / done 完成 / quit 退出: ")
    if action == "add":
        new = input("要做什么?")
        todos.append(new)
    elif action == "done":
        n = int(input("完成第几件?"))
        todos.pop(n - 1)
    elif action == "quit":
        print("拜拜!")
        break
    else:
        print("输入 add / done /quit")