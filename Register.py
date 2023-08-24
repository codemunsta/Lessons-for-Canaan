basket = [10, 20, 50, 100, 200, 500, 1000, 20, 20, 50, 200, 200, 500, 200, 10, 100, 100, 100]
basket_dic = {
    "10": 2,
    "20": 5,
    "50": 1,
    "100": 4,
    "200": 3,
    "500": 2,
    "1000": 1
}


def check_change_dic(change):
    print("checking from dict")
    change_string = str(change)
    if basket_dic[change_string] != 0:
        print(f"Your change is {change}")
        basket_dic[change_string] = basket_dic[change_string] - 1
        return
    else:
        print("We do not have your change")
        return


def check_change(change):
    print("checking from array")
    for currency in basket:
        if change == currency:
            print(f"Your change is {change}")
            basket.remove(currency)
            return
    print("We do not have your change")
    return


while True:
    change = int(input("How much is your change \n"))
    check_change_dic(change)
    if len(basket) == 0:
        print("we have run out of chash")
        break
