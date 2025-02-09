file = open('/Users/jennifernelson/Documents/Lesson_Content_Spring_25/Foundation/06_Python/01_File_Access/test_file.txt', 'r')
#can also use just name of file.txt for mac

# print(file) # What do we get?

"""
Reading the file
"""

# content = file.read()  # try passing a number as an arg. like read(3)
    #read(3) , reads the first 3 characters of the file
# content = file.readline() #reads a line
content = file.readlines()
print(content)

"""
IMPORTANT: now that we have finished our operations with the file, we must CLOSE it. 
Otherwise it would still be open and changes not save. 
Also others cannot access the file while it is open.
"""

# we need to run this

#saving of a file only happens at this point at file.close()
# file.close()