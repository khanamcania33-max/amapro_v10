def profit_simulation(price):

    cost = price * 0.25

    shipping = 4

    fba_fee = price * 0.15

    ppc = price * 0.10

    profit = price - (cost + shipping + fba_fee + ppc)

    margin = profit / price

    return round(profit,2), round(margin*100,1)