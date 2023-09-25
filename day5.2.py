#bonus example

mylist=["sen",'ben',"john"]
# mylist.sort(reverse=True)
# for decending order
mylist.sort()

for index,item in enumerate(mylist):
    row=f"{index+1}.{item.capitalize()}"
    print(row)
