filenames=["1.Raw Data.txt","2.Reports.txt","3.Presentations.txt"]
for filename in filenames:
    print(filename)
    newf=filename.replace('.','-',1)
    #the above represents only changes the first occurence of '.' if we remove the 1 argument all '.' will be replaced
    filename=newf
    print(filename)
print(filenames)

# filename() for the tuple
filenamess=("1.Raw Data.txt","2.Reports.txt","3.Presentations.txt")
print(type(filenamess))