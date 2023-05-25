age = input("Enter your age:")
int_age = int(age)
if int_age < 21:
    print("You are young!")
else:
    print("Wow, you are old!")


age = input("Enter your age:")
int_age = int(age)
result = "You are young!" if int_age < 21 else "You are old!"
print(result)
