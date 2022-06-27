# count odd numbers
lists = [1,2,3,4,5,6,7]

odd_count = 0
for num in lists:
    if num % 2 != 0:
        odd_count += 1
print("Odd numbers are: ", odd_count)