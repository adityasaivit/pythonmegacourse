# file=open('/Users/adityasai/Downloads/members.txt','w')
# file.write('solomon Right')
file=open('/Users/adityasai/Downloads/members.txt','r')
adi=file.readlines()
adi.append("Solomon Right\n")
file=open('/Users/adityasai/Downloads/members.txt','w')
file.writelines(adi)
print(adi)