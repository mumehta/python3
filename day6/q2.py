# Write a program to accept marks of 6 students and display them in a sorted manner.
marks = input("Enter student marks(separated by comma): ")
marks = list(marks.split(","))
# converting to ints
for i in range(0, len(marks)):
    marks[i] = int(marks[i])
# list in sorted manner
marks.sort()
print("The marks in sorted manner are: ", marks)
