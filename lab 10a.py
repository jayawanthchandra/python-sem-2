freq={}
f=open("code text.txt","r")
for line in f:
    for char in line:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
print(freq)                