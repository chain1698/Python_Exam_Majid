purchases = [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)]

totals = {}

for name, amount in purchases:
    if name in totals:
        totals[name] += amount
    else:
        totals[name] = amount

for name, total in totals.items():
    print(f"{name} spent ${total}")