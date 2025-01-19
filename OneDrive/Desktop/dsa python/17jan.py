def chocolates_from_wrappers(wrappers, wrapper_offer):
    if wrappers < wrapper_offer:
        return 0
    new_chocolates = wrappers // wrapper_offer
    remaining_wrappers = wrappers % wrapper_offer
    return new_chocolates + chocolates_from_wrappers(new_chocolates + remaining_wrappers, wrapper_offer)

def chocolates_in_a_day(money, chocolate_price, wrapper_offer):
    chocolates = money // chocolate_price
    return chocolates + chocolates_from_wrappers(chocolates, wrapper_offer)

def chocolates_in_a_month(days_in_month, money, chocolate_price, wrapper_offer):
    total_chocolates = 0
    for day in range(1, days_in_month + 1):
        if day % 7 == 0 or day % 7 == 6:
            continue
        total_chocolates += chocolates_in_a_day(money, chocolate_price, wrapper_offer)
    return total_chocolates

money_per_day = 16
chocolate_price = 2
wrapper_offer = 2
days_in_month = 30

total_chocolates = chocolates_in_a_month(days_in_month, money_per_day, chocolate_price, wrapper_offer)
print("Total chocolates Raman can buy in a month:", total_chocolates)
