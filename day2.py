# user_prompt='Enter a  credential for Todo List:'
# while(True):
#     todo=input(user_prompt)
#     print(todo)
#     print("Next...")

#term used in the while can be any expression which was true like 2>1

#if we use False no while will be executed in the program
todos=[]
user_prompt='Enter a  credential for Todo List:'
while(True):
    todo=input(user_prompt)
    todo=todo.capitalize()
    todos.append(todo)
    print(todos)
    print("Next...")
# we cannot use append for the string
# .upper() to convert all the letters to the uppercase

