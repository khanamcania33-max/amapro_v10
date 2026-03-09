import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

from keyword_engine import generate_keywords
from discovery_engine import discover_products
from scoring_engine import score_product
from profit_engine import profit_sim

st.set_page_config(page_title="AMAPRO v10 AI ENGINE",layout="wide")

st.title("🚀 AMAPRO v10 — FULL AI AMAZON BUSINESS ENGINE")

# sidebar

st.sidebar.header("Discovery Settings")

keyword_count = st.sidebar.slider("Niches to Scan",100,1000,300)

min_price = st.sidebar.slider("Minimum Price",40,200,40)

max_reviews = st.sidebar.slider("Maximum Reviews",50,500,200)

run = st.sidebar.button("Run AI Scan")

if run:

    keywords = generate_keywords(keyword_count)

    df = discover_products(keywords)

    df["Opportunity Score"] = df.apply(score_product,axis=1)

    profits=[]
    margins=[]

    for p in df["Price"]:

        pr,mg = profit_sim(p)

        profits.append(pr)
        margins.append(mg)

    df["Profit $"] = profits
    df["Margin %"] = margins

    # Amazon search link

    df["Amazon Link"] = "https://www.amazon.com/s?k=" + df["Niche"].str.replace(" ","+")

    # niche clustering

    features = df[["Price","Monthly Sales","Reviews"]]

    model = KMeans(n_clusters=6,n_init=10)

    df["Cluster"] = model.fit_predict(features)

    filtered = df[
    (df["Price"]>=min_price)&
    (df["Reviews"]<=max_reviews)
    ]

    filtered = filtered.sort_values("Opportunity Score",ascending=False)

    st.subheader("🏆 Top Opportunities")

    winners = filtered.head(100)

    st.dataframe(
        winners,
        column_config={
        "Amazon Link":st.column_config.LinkColumn("Amazon",display_text="Search")
        },
        use_container_width=True
    )

    # charts

    st.subheader("Opportunity Map")

    fig = px.scatter(
        filtered,
        x="Reviews",
        y="Revenue",
        size="Monthly Sales",
        color="Opportunity Score",
        hover_name="Niche"
    )

    st.plotly_chart(fig)

    st.subheader("Opportunity Score Distribution")

    fig2 = px.histogram(filtered,x="Opportunity Score")

    st.plotly_chart(fig2)

    # CSV DOWNLOAD (GOOGLE SHEETS READY)

    csv = winners.to_csv(index=False).encode()

    st.download_button(
    "📥 Download Google Sheets CSV",
    csv,
    "amapro_v10_opportunities.csv",
    "text/csv"
    )
