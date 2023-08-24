change = {10: 4, 20: 3, 50: 5, 100: 2, 200: 3, 500: 6, 1000: 1, 0: 0}


while True:
    user_input = int(input("Enter Change You want to get:\n"))

    remaining = user_input
    change_given = {}

    for currency in sorted(change.keys(), reverse=True):
        if currency == 0:
            break
        while remaining >= currency and change[currency] > 0:
            remaining -= currency
            change_given[currency] = change_given.get(currency, 0) + 1
            change[currency] -= 1

            if change[currency] == 0:
                change[0] += 1

    if remaining == 0:
        print("Your change:", user_input)
        print("Your wallet:", change)
    else:
        print("Sorry, unable to provide exact change. Remaining:", remaining)

    if change[0] == 7:
        print("Sorry the change basket has finished")
        break
    else:
        continue
