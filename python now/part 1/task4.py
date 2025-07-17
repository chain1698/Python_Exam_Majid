numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ").strip()
    if user_input.lower() == "done":
        break
    if not user_input:
        print("Invalid input. Try again.")
        continue
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Try again.")

if numbers:
    total = len(numbers)
    average = round(sum(numbers) / total, 2)
    print(f"Total numbers entered: {total}")
    print(f"Average: {average}")
else:
    print("No valid numbers were entered.")