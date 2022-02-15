# Write a program to sum a list with 4 numbers
list_1 = input("Enter four numbers (separated by comma): ")
numb = list(list_1.split(","))
total = 0
# converting to ints
for i in range(0, len(numb)):
    total += int(numb[i])
print("sum is: ", total)
