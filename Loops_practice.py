# average height of student

student_heights = [158, 176, 192, 135, 164, 171]

counter = 0 # keeps track of index count
sum_of_heights = 0 #tracks sum of all heights

for height in student_heights:
    counter += 1
    sum_of_heights += height

average_height = sum_of_heights / counter
print(int(average_height))

print(counter)

# adding even numbers
print("\n")
final_number = 0

for number in range(1, 101):
    if number % 2 == 0:
        final_number += number

print(final_number)

# FIZZ BUZZ
print("\n")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FIZZBUZZ")
    elif number % 5 == 0:
        print("BUZZ")
    elif number % 3 == 0:
        print("FIZZ")
    else:
        print(number)