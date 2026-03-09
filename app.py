import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

from keyword_engine import generate_keywords
from discovery_engine import discover_products
from scoring_engine import score_product
from profit_engine import profit_simulation

st.set_page_config(page_title="AMAPRO v9 QUANTUM AI", layout="wide")

st.title("🚀 AMAPRO v9 — QUANTUM AMAZON RESEARCH AI")

# Sidebar

st.sidebar.header("Discovery Settings")

keyword_count = st.sidebar.slider("Keywords to Scan",100,1000,300)

min_price = st.sidebar.slider("Minimum Price",40,200,40)

max_reviews = st.sidebar.slider("Maximum Reviews",50,500,200)

if st.sidebar.button("Run Quantum Scan"):

    keywords = generate_keywords(keyword_count)

    df = discover_products(keywords)

    df["Opportunity Score"] = df.apply(score_product,axis=1)

    profits = []
    margins = []

    for p in df["price"]:

        pr,mg = profit_simulation(p)

        profits.append(pr)

        margins.append(mg)

    df["profit"] = profits
    df["margin"] = margins

    # AI niche clustering
    features = df[["price","monthly_sales","reviews"]]

    model = KMeans(n_clusters=6,n_init=10)

    df["niche_cluster"] = model.fit_predict(features)

    filtered = df[
    (df["price"] >= min_price) &
    (df["reviews"] <= max_reviews)
    ]

    filtered = filtered.sort_values("Opportunity Score",ascending=False)

    st.subheader("🏆 Top Opportunities")

    winners = filtered.head(100)

    st.dataframe(winners)

    st.subheader("Opportunity Map")

    fig = px.scatter(
        filtered,
        x="reviews",
        y="revenue",
        size="monthly_sales",
        color="Opportunity Score",
        hover_name="keyword"
    )

    st.plotly_chart(fig)

    st.subheader("Opportunity Distribution")

    fig2 = px.histogram(filtered,x="Opportunity Score")

    st.plotly_chart(fig2)