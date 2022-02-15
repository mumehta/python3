# Write a program to store seven fruits in a list entered by the user.
fruits = input("Enter seven fruits(separated by comma): ")
fruits = list(fruits.split(","))
print("The fruits are: ")
for i in fruits:
    print(i.strip())
