import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

from keyword_engine import generate_keywords
from discovery_engine import discover_products
from scoring_engine import score_product
from profit_engine import profit_sim

st.set_page_config(page_title="AMAPRO v13 ULTIMATE AUTOPILOT", layout="wide")
st.title("🚀 AMAPRO v13 — ULTIMATE AUTOPILOT PRO (Top 3 Products per Niche)")

# Sidebar
st.sidebar.header("Discovery Settings")
keyword_count = st.sidebar.slider("Number of Niches", 100, 500, 200)
min_price = st.sidebar.slider("Minimum Price", 40, 200, 40)
max_reviews = st.sidebar.slider("Maximum Reviews", 50, 500, 200)
run = st.sidebar.button("Run Quantum Scan")

if run:
    keywords = generate_keywords(keyword_count)
    df = discover_products(keywords)
    
    # Scoring and profit
    df["Opportunity Score"] = df.apply(score_product, axis=1)
    profits=[]
    margins=[]
    for p in df["Price"]:
        pr, mg = profit_sim(p)
        profits.append(pr)
        margins.append(mg)
    df["Profit $"] = profits
    df["Margin %"] = margins
    
    # Niche clustering
    features = df[["Price","Reviews"]]
    model = KMeans(n_clusters=6, n_init=10)
    df["Cluster"] = model.fit_predict(features)
    
    # Filter by user
    filtered = df[(df["Price"]>=min_price)&(df["Reviews"]<=max_reviews)]
    filtered = filtered.sort_values("Opportunity Score", ascending=False)
    
    st.subheader("🏆 Top Opportunities with Top 3 Products per Niche")
    st.dataframe(
        filtered.head(100),
        column_config={"Amazon Link": st.column_config.LinkColumn("Amazon Link", display_text="Open Product")},
        use_container_width=True
    )
    
    # Opportunity Map
    st.subheader("Opportunity Map")
    fig = px.scatter(filtered, x="Reviews", y="Price", size="Profit $", color="Opportunity Score", hover_name="Product")
    st.plotly_chart(fig)
    
    # CSV Export
    csv = filtered.to_csv(index=False).encode()
    st.download_button("📥 Download Google Sheets CSV", csv, "amapro_v13_opportunities.csv", "text/csv")
