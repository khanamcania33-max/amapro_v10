import random
import pandas as pd

def discover_products(keywords):

    rows=[]

    for k in keywords:

        price=round(random.uniform(40,150),2)

        sales=random.randint(50,1500)

        revenue=price*sales

        reviews=random.randint(10,400)

        rating=round(random.uniform(3.5,4.8),2)

        keyword_volume=random.randint(2000,50000)

        rows.append({

        "Niche":k,
        "Price":price,
        "Monthly Sales":sales,
        "Revenue":revenue,
        "Reviews":reviews,
        "Rating":rating,
        "Keyword Volume":keyword_volume

        })

    return pd.DataFrame(rows)
