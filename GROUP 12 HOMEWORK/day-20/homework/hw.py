# for i in range(1, 101):
#     if i % 5 == 0:
#         print(i)
#     elif i % 3 ==0:
#         print(i)



# username = []
# adding = input("Please enter your name: ")
# username.append(adding)
# print(username)



number = int(input("Enter a number: "))
total = 0

for i in range(1, number):
    print(i)
    total += i

average = total / number

print(total)
print(average)