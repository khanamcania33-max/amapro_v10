def score_product(row):

    demand = 25 if row["Revenue"]>50000 else 18 if row["Revenue"]>25000 else 10

    competition = 20 if row["Reviews"]<120 else 12

    trend = 15 if row["Monthly Sales"]>800 else 10

    keyword = 15 if row["Keyword Volume"]>20000 else 8

    improvement = 10 if row["Rating"]<4.3 else 5

    return demand+competition+trend+keyword+improvement
