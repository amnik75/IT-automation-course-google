import os
import datetime

file = open("a.txt")
line = file.readline() #read one line after the line that is read before
lines = file.read() #read lines untill the end from the line after the line that is read before
lines  = file.readlines() # make list of the lines
file.close()
# with close file byitself
with open('a.txt','w') as file:
    file.write("salam!")

with open('a.txt','r') as file:
    for l in file:
        print(l)

if os.path.exists("a.txt"):
    os.rename("a.txt",'r.txt')
if os.path.exists("r.txt"):
    os.remove('r.txt')

print(os.path.getsize('a.txt'))
print(os.path.getmtime('a.txt'))
print(datetime.datetime.fromtimestamp(os.path.getmtime('a.txt')))
print(os.path.abspath('a.txt'))

print(os.getcwd())
 # show files and directory
os.listdir('/')
path = os.path.join('Desktop','file.txt') # make a path of the file independent of operating system
bool = os.path.isdir(path)
os.mkdir("py_dir")
os.chdir("py_dir")
os.chdir("py_dir2")
os.rmdir('py_dir2')




print(os.path.expanduser ('~'))