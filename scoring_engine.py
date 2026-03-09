def score_product(row):

    demand = 25 if row["revenue"] > 50000 else 18 if row["revenue"] > 25000 else 10

    competition = 20 if row["reviews"] < 120 else 12

    trend = 15 if row["monthly_sales"] > 800 else 10

    keyword = 15 if row["keyword_volume"] > 20000 else 8

    rating_gap = 10 if row["rating"] < 4.3 else 5

    return demand + competition + trend + keyword + rating_gap