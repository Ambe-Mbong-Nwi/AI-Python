x = 3
y = 4
print(x+y)
# in some cases _ gives output of the previous equation so _+2 gives 9
name = "tokyoisfine"
print(name + "toi")
print(name[0])
#prints first letter of name which is t
print(name[-1])
# starts from ending hence prints e
print(name[0:3])
#prints 0 to 2(tok) hence excluding 3
print(name[1:], name[:5])
#prints from 1 till end and begining to 4th letter respectively
# NB strings here are immutable meaning value of any letter cannot be changed as with integers
#hence to modify strings, do the following
print(name[0:5] + " is my dream place")
print(len(name))
#len prints length of string