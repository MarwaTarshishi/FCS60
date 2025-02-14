age = int(input("Enter your age: "))

if age < 5:
    print("You're too young! Enjoy the movie for free!")
    price = 0
elif age <= 12:
    print("You're a kid! Your ticket price is just $5.")
    price = 5
elif age <= 60:
    print("You're an adult! Standard ticket price applies: $10.")
    price = 10
print(f"The ticket price is ${price}.")
