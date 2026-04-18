def total_calc(bill , tip):
    tip_per = bill * tip // 100
    total = bill + tip_per
    print(total)

total_calc(1000 , 10)