man = input("Please enter your name: ")
result = []
for i in range(len(man)):
    if man[i].isdigit():
        result.append(i)
if result:
    print("Error at positions:", result)
else:
    print("Thanks, your name is valid.")


