
#1)

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b


#2)


# def form():
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))
#     return length * width

# print(form())

#3)
# def func():
#     result = []
#     for i in range(10):
#         result.append("goa best")
#     return result
# output = func()
# print(output)


#4)

# def func(length,width,):
#     perimeter = []
#     perimeter.append(2*(length + width))
#     print(perimeter)

# func(2,5)

# 5)

# number = int(input("შეიყვანეთ რიცხვი: "))

# if number > 10:
#     print("რიცხვი მეტია 10-ზე")
# else:
#     print("რიცხვი არ არის 10-ზე მეტი")


#6)

# number = int(input("შეიყვანეთ რიცხვი: "))

# if number >= 1:
#     print("დადებიითი")
# elif number == 0:
#     print("its 0")
# else:
#     print("its negative")

#7)

# age = int(input("what is ur age:"))
# if age >= 18:
#     print("u can vote")
# else:
#     print("u cant vote")

#8)

# number = int(input("write a number:"))
# if number >=0:
#     print("its positive")
# else:
#     print("its negative")



#9)

age = int(input("what is ur age:"))

if 0 <= age <= 13:
    print("ur baby")

elif 14<= age <=18:
    print("ur teen")

else:
    print("ur adult")