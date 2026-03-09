import requests

def search_amazon_products(keyword, max_results=3):
    """
    Returns top 3 products per niche.
    Each product: {title, asin, price, reviews, rating, link}
    """
    # Placeholder: Replace with real API call
    products=[]
    for i in range(max_results):
        asin=f"B0FAKE{i}{keyword[:2].upper()}"
        products.append({
            "title": f"Demo Product {i+1} for {keyword}",
            "asin": asin,
            "price": round(40 + i*15,2),
            "reviews": 50 + i*70,
            "rating": round(3.5 + 0.3*i,2),
            "link": f"https://www.amazon.com/dp/{asin}"
        })
    return products
