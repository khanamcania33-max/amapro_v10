import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from keyword_engine import generate_keywords
from discovery_engine import discover_products
from scoring_engine import score_product
from profit_engine import profit_sim

st.set_page_config(page_title="AMAPRO v12 AUTOPILOT PRO", layout="wide")
st.title("🚀 AMAPRO v12 — AUTOPILOT PRO (Real Amazon Products)")

# Sidebar
st.sidebar.header("Discovery Settings")
keyword_count = st.sidebar.slider("Number of Niches",100,500,200)
min_price = st.sidebar.slider("Minimum Price",40,200,40)
max_reviews = st.sidebar.slider("Maximum Reviews",50,500,200)
run = st.sidebar.button("Run Quantum Scan")

if run:
    keywords = generate_keywords(keyword_count)
    df = discover_products(keywords)
    
    # Opportunity Score
    df["Opportunity Score"] = df.apply(score_product, axis=1)
    
    profits=[]
    margins=[]
    for p in df["Price"]:
        pr, mg = profit_sim(p)
        profits.append(pr)
        margins.append(mg)
    df["Profit $"] = profits
    df["Margin %"] = margins
    
    # Clustering
    features = df[["Price","Reviews"]]
    model = KMeans(n_clusters=5,n_init=10)
    df["Cluster"] = model.fit_predict(features)
    
    # Filter
    filtered = df[(df["Price"]>=min_price)&(df["Reviews"]<=max_reviews)]
    filtered = filtered.sort_values("Opportunity Score",ascending=False)
    
    st.subheader("🏆 Top Opportunities with Amazon Product")
    st.dataframe(
        filtered.head(100),
        column_config={"Amazon Link": st.column_config.LinkColumn("Amazon Link", display_text="Open Product")},
        use_container_width=True
    )
    
    # Charts
    st.subheader("Opportunity Map")
    fig = px.scatter(filtered, x="Reviews", y="Price", size="Profit $", color="Opportunity Score",
                     hover_name="Product")
    st.plotly_chart(fig)
    
    st.subheader("Download Google Sheets CSV")
    csv = filtered.to_csv(index=False).encode()
    st.download_button("📥 Download CSV", csv, "amapro_v12_opportunities.csv", "text/csv")
