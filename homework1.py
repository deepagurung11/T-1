age = int(input("Enter your age:"))
y = input("Are you a student? (yes/no): ")
if age < 5:
    print("You are too young to watch a movie.")
elif age >= 5 and age <= 12:
    print("You are eligible for a child discount.")
elif age >= 60:
    print("You are eligible for a senior discount.")
elif y == "yes":
    print("You are eligible for a student discount.")
else:
    print("You are not eligible for any discounts.")