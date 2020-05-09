print('Hello')
#numbers
print('add numbas')
x = (input())
y = (input())

print(x * y)
print(x + y)
print(x / y)
print(x * y)
print(x % y)
print(x // y)
print(abs(x))
print(divmod(x, y))
#и так далее

#lists
yu = [1, 3, 5, 7, 9]

yu.append(4)
print(yu)

yu.extend(2, 4)
print(yu)

yu.insert(3, 4)
print(yu)

yu.remove(0)
print(yu)

yu.clear()
print(yu)

#Indexes and slices

i = [1, 2, 3, 4, 5, 6]
print(i[0])
print(i[-1:])
print(i[:])
del i[3]

#Tuples

a = (1, 2, 3, 4, 5, 6, 7, 10)

print(a.__sizeof__())
print(tuple('Welcome Ladies and Gentlemen'))
print(a[3:1])
print(a[7:1])

#Sets (mutable and immutable)

bc = set()
print(bc)
bc = set("I don't have anything to say.")

###

listofvariables = {"a", "B", "c", "D"}
setofset = set(listofvariables)
print(len(listofvariables))
listofvariablesv2 = listofvariables.copy()
listofvariables.pop()
listofvariables.remove("B")
listofvariablesv2.add(77)
print(listofvariablesv2)
print(listofvariables)

###


