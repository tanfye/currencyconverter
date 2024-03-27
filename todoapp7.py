todos = []

while True:
    option = input("Type add, show, remove or edit: ").lower()
    match option:
        case 'add':
            todo = input("Enter todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for i, j in enumerate(todos):
                print(f"{i + 1}. {j.title()}")
        case 'remove':
            x = int(input("Enter item to remove: "))
            todos.pop(x-1)
        case 'exit':
            break
        case _:
            print("Invalid keyword, try again")

print("Program ended")