### for more information search https://ryanstutorials.net/bash-scripting-tutorial/ site ###

#!/bin/bash

# intialize variable with =
a=amir

# use $ to access the value of variable
echo $a

# intialize variable with = and "" with spaces
b="amir nik $a"

# intialize variable with = and '' with spaces without value of variable
b='amir nik $a'

# use $( command ) use this for assign output of command to variables
l=$( ls )

# ((expr)) use this for arithmatic
a=$(( 5 + 4 ))
b=$(( a \* 2 ))

# if statements
if [ $a -le 2 ]
then
    echo $a
elif [ $a -le 5 ]; then
    echo $a
else
    echo $a
fi

#we can use break and continue in loops
# while loop
counter=1
while [ $counter -le 10 ]
do
    echo $counter
    ((counter++))
done

# for loop
names='Stan Kyle Cartman'
for name in $names
do
    echo $name
done

# select items
names='Kyle Cartman Stan Quit'
PS3='Select character: '
select name in $names
do
if [ $name == 'Quit' ]
then
    break
fi
    echo Hello $name
done

print_something () {
    echo Hello $1
    local var1='local 1' # only in this function
    return 5
}
print_something Mars

ls () {
    command ls -lh # use command when the name of the command (ls) is the same as function name
}

# So we now have 3 methods for getting input from the user:
# 1: Command line arguments
# 2: Read input during script execution
# 3: Accept data that has been redirected into the Bash script via STDIN
# also we can use mixture of them

# read input with read
read -p 'Username: ' uservar
read -sp 'Password: ' passvar   




