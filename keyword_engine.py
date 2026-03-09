import requests
import hashlib
import hmac
import base64
import time
import urllib.parse

# Placeholder: Use official PA API SDK or signed requests
# This is a simplified structure

def search_amazon_products(keyword, max_results=1):
    """
    Return list of product dicts:
    [{'title':..., 'asin':..., 'price':..., 'reviews':..., 'rating':..., 'link':...}]
    """
    # Here you should implement PA API request
    # For demo, we return a fake product
    fake_product = {
        "title": f"Demo Product for {keyword}",
        "asin": "B0FAKE1",
        "price": 49.99,
        "reviews": 120,
        "rating": 4.5,
        "link": f"https://www.amazon.com/dp/B0FAKE1"
    }
    return [fake_product]
