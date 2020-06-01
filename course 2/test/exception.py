
try:
    i = int(input('enter number:'))
    print(i)
except ValueError:
    print("wrong input")
else:
    print("OK")

print('Good bye!')

# use for debugging
i=5
assert type(i) == str , 'i should be string'

# Two aproaches for handling exception:
# 1- let exception happens and handle it in try except block
# 2- use if condition to prevent error happening