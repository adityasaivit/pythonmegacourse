content=["carrot are sliced completely",
         "carrots are reportedly sliced",
         "slicing process was as well as presented"]
filenames=["doc.txt","report.txt","presentation.txt"]


for i,j in zip(content,filenames):
    file=open(j,'w')
    file.write(i)
    file.read()
    file.close()


