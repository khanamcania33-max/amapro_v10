def score_product(row):
    demand = 25 if row["Price"]*row["Reviews"]>50000 else 18 if row["Price"]*row["Reviews"]>25000 else 10
    competition = 20 if row["Reviews"]<120 else 12
    trend = 15 if row["Reviews"]>50 else 10
    improvement = 10 if row["Rating"]<4.5 else 5
    return demand + competition + trend + improvement
