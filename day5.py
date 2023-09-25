user_prompt='Type Add or Show or edit or Exit or complete:'
user_prompt=user_prompt.strip()

todos=[]
while True:
    user_action=input(user_prompt)
    match user_action:
        case 'add':
            todo=input("Enter a ToDo:")
            todos.append(todo)
        case 'show'| 'display':
            for index, todo in enumerate(todos):
                print(index,'.',todo)
                #fstrings
                print(f"{index+1}.-){todo}")
            # print(f"length is {index+1}")
            print(todos)
        case 'edit':
            for index,todo in enumerate(todos):
                print(str(index)+'.'+todo)
            inp=int(input("choose the todo which you want to edit:"))
            edit1=input("enter the new todo:")
            print("the existing todo was",todos[i-1])
            todos[inp-1]=edit1
        case 'complete':
            number=int(input("Enter the number of the todo to complete"))
            todos.pop(number-1)


        case 'exit':
            break
        case whatever:
            print("you had entered a wrong input")
print('Bye!!')