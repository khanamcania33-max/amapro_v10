import random
import pandas as pd
from faker import Faker

fake = Faker()

def discover_products(keywords):

    rows = []

    for k in keywords:

        price = round(random.uniform(40,150),2)

        sales = random.randint(50,1500)

        revenue = price * sales

        reviews = random.randint(10,400)

        rating = round(random.uniform(3.5,4.8),2)

        keyword_volume = random.randint(2000,50000)

        rows.append({

        "keyword":k,
        "price":price,
        "monthly_sales":sales,
        "revenue":revenue,
        "reviews":reviews,
        "rating":rating,
        "keyword_volume":keyword_volume,
        "asin":fake.bothify(text='B0#####')

        })

    return pd.DataFrame(rows)