# odd is lower case
# even is upper case
def mixed_string(text):
    result = ""
    for i in range(0,len(text)):
        if i%2 == 0: # even
            result += text[i].lower()
        else:
            result += text[i].upper()
    return result

print(mixed_string("Happy"))
print(mixed_string("Hamilton"))