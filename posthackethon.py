file=open('whatever.txt','r')
all=file.readlines()

while True:
    i=int(input())
    match i:
        case 1:
            a=input("enter a word:")+"\n"
            all.append(a)
            file1=open('whatever.txt','w')
            file1.writelines(all)
            print(all)
        case 0:
            break;
        case 2:
            file.readlines()
        case whatever:
            print("not a valid input")

