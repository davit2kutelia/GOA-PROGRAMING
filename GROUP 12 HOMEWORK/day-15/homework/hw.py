
# score = float(input("შეიტანეთ ტესტში მიღებული ქულა: "))

# if 90 < score < 100:
#     print("თქვენ დაგიფინანსდებათ სწავლა სრულიად.")
# elif 70 < score < 80:
#     print("თქვენ დაგიფინანსდებათ სწავლა 1500 ლარით.")
# elif 40 < score < 70:
#     print("თქვენ დაგიფინანსდებათ სწავლა 500 ლარით.")
# else:
#     print("თქვენ არ დაგიფინანსდებათ სწავლის პროცესი.")


grade = float(input("Enter your grade in the test: "))

if grade == 10:
    print("Excellent!")
elif grade == 9 or 8:
    print("Well done!")
elif grade == 5:
    print("Bad.")
elif grade < 5:
    print("Kick from school.")
else:
    print("Grade not recognized.")
