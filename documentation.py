def add(x,y):
    '''
     The add function adds to numbers
     x: can be anything
     y: can be anything
     if x and y are strings, the result is a concatanated string
     otherwise, the result can be regular addition
    '''
    return x+y

def sub(x,y):
    '''
    this function subtracts to numbers
    '''
    return x-y

y = add(2,4)
text = add("Hello", "World")
print(y)
print(text)
print(add.__doc__)
new_text = sub("Hello", "World")
# in java, c++, c
# int add(int x, int y){
#
#}