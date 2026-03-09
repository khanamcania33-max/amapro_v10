from amazon_api import search_amazon_products
import pandas as pd

def discover_products(keywords):
    rows=[]
    for k in keywords:
        products = search_amazon_products(k, max_results=1)
        for p in products:
            rows.append({
                "Niche": k,
                "Product": p["title"],
                "ASIN": p["asin"],
                "Amazon Link": p["link"],
                "Price": p["price"],
                "Reviews": p["reviews"],
                "Rating": p["rating"]
            })
    return pd.DataFrame(rows)
