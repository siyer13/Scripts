def findStr(str):
    givenList = ['HelloMars','HelloWorld', 'HelloWorldMars', 'HiHo']
    matchingElements = []

    for word in givenList:
        if str in word:
            matchingElements.append(word)
    return matchingElements


finalList = findStr('He')
print(finalList)
