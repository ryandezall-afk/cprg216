frequency = dict()
text = "Hello, how are you"


for ch in text:
    if frequency.get(ch) == None:
        frequency[ch] = "*"
    else:
        frequency[ch] += "*"

for ch in frequency:
    print(ch, ':', frequency[ch])
    