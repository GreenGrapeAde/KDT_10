numList = [ int(n) for n in input("").split()]
nameList1 = []
nameList2 = []

for i in range(numList[0]):
    nameList1.append(input(""))

for i in range(numList[1]):
    nameList2.append(input(""))

#print(nameList1, nameList2)

result = list(set(nameList1) & set(nameList2))
result.sort()

print(len(result))
for i in range(len(result)):
    print(result[i])