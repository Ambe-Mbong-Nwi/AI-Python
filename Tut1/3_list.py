ages = [2, 6, 8, 12, 14, 16]
#the above is a list
print(ages[0], ages[1:5], ages[-1])
# u can create a list of strings and of different data types as follows
names = ["abong", "abii", "miya", "solange", "afa"]
values = ["tokyo", 3, 4.45]
print(names)
print(values)
# we can have a list of lists as follows
tot = [names, ages]
print(tot)
# lists are mutable eg adding other values etc
names.append("blessing")
print(names)
names.insert(5,"melvis")
print(names)
names.remove("abii")# removes the element you want
print(names)
names.pop(1)# removes the element using the index value
print(names)#pop() removes last element bcos its a stack
del names[0:2]# deletion of multiple values
print(names)
names.extend(["moi", "toi", "wow"])# addition of many names
print(names)
ages.sort()
print(ages)
print(min(ages))# finding minimum value
print(max(ages))
print(sum(ages))


# tuple is similar to lists but diff bcos its immutable ie values cannot be changed
# tuple(), list[], but in fetching values use [].
# tuple has only two methods which are count and index
ages = (2, 4, 6, 8, 10, 12, 14, 16, 18)
print(ages)
print(ages[1:4])
