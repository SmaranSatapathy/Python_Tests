word=list(input("Enter word: "))
print(word)
word.sort()
print(word)

newList=[]

for i in range(0,len(word)):
    if word[i] not in newList:
        newList.append(word[i])
    
print("New list is: ",newList)