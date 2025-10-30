frequency = dict()
text = "Hello, how are you"


for ch in text:
    if frequency.get(ch) == None:
        frequency[ch] = "*"  #for some reasono using two == like that gave it an invalid error
    else:
        frequency[ch] += "*"

for ch in frequency:
    print(ch, ':', frequency[ch])
    