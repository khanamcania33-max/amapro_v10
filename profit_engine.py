def profit_sim(price):

    cost = price*0.25

    shipping = 4

    fba = price*0.15

    ppc = price*0.10

    profit = price-(cost+shipping+fba+ppc)

    margin = profit/price

    return round(profit,2), round(margin*100,1)
