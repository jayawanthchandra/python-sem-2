c=0
w=0
l=0
with open("code text.txt") as file:
    for line in file:
         w+=len(line.split())
         l+=1
         c+=len(line)
print("No. of words: ", w)
print("No. of Characters: ",c)
print("No. of Lines: ", l)         