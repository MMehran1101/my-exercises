donations = {
    'Mehran': 35,
    'Ali': 100,
    'Kernel': 50,
    'Erfan': 400
}


def donations_calculator(don):
    largest = 0
    total = 0
    count = 0

    for name, value in don.items():
        if value > largest:
            person = (name, value)
        total += value
        count += 1

    avg = int(total / count)
    return person, total, avg


largest_donate_person, total, average = donations_calculator(donations)

print(f"Largest Donate by {largest_donate_person}")
print(f"Total of donates is {total}")
print(f"Average of donates is {average}")
