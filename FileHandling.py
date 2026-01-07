#this file has some basics regarding file handling in python
#opening a file. This method is not much recommended as we need to close the file explicitly after operations. r- read mode
#f = open('testfile.txt', 'r')
#print(f.name)
#f.close()

#using context manager - we can work with the file in the code block and it will be automatically closed. 
#no need to close the file explicitly. this will close during exceptions also.
#with open ('testfile.txt', 'r') as f:
    #reading the fiele contents
    #size_to_read = 100
    #f_content = f.read(size_to_read) #this will load all contents at once and takes more memory. can mention no of char to bread in the brackets.
   
   #looping through lines.
   #for line in f:
      #print(line, end='')
      
   #f_content = f.readline()  #read one line at  atime
   #f_content = f.readlines()  #read all lines one by one.but this will add new line at end. to reduce, use emd = '' in print.
#print(f_content, end='')

#write operations - if file exists this will overwrite, if not it will create the file
#with open ('testfile.txt', 'w') as wf:  
    #wf.write('New data from python\n')
    #wf.write('New data from python')
    #if we directly write on the file already existing, the insertion will delete the already existing data.

#print('write operation finished!')

#append method
#with open ('testfile.txt', 'a') as wf: 
    #wf.write('\n') 
    #wf.write('Appending new line\n')
#print('write operation finished!')

#read and write operations at the same time
with open('testfile.txt', 'r+') as rf:
    print(rf.read())
    rf.write('\nhello!')
    print(rf.read(), end='')
    
