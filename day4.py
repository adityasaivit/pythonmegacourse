user_prompt='Type Add or Show or edit or Exit:'
todos=[]
while True:
    user_action=input(user_prompt)
    match user_action:
        case 'add':
            todo=input("Enter a ToDo:")
            todos.append(todo)
        case 'show'| 'display':
            for item in todos:
                item=item.title()

                print(item)
            print(todos)
        case 'edit':
            for i in range(1,len(todos)+1,1):
                print(i,'.',todos[i-1])
            inp=int(input("choose the todo which you want to edit:"))
            edit1=input("enter the new todo:")
            print("the existing todo was",todos[i-1])
            todos[inp-1]=edit1


        case 'exit':
            break
        case whatever:
            print("you had entered a wrong input")
print('Bye!!')