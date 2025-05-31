import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title="Housing Dashboard", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("D:\Desktop\pro\Analysis\Housing.csv")  # replace with your actual CSV filename
    return df

df = load_data()

# Title
st.title("🏠Housing Dataset Dashboard🏠")

st.subheader("🌟Unfiltered Data")
st.dataframe(df, use_container_width= True)
st.sidebar.markdown("Select the option to filter the dataset")


# Sidebar filters
st.sidebar.header("Filter Data")

# Add sliders and selectors
min_price = int(df["price"].min())
max_price = int(df["price"].max())
price_range = st.sidebar.slider("Select Price Range", min_price, max_price, (min_price, max_price))

bedrooms = st.sidebar.multiselect("Select Bedrooms", sorted(df["bedrooms"].unique()), default=sorted(df["bedrooms"].unique()))
bathrooms = st.sidebar.multiselect("Select Bathrooms", sorted(df["bathrooms"].unique()), default=sorted(df["bathrooms"].unique()))

# Filter data
filtered_df = df[
    (df["price"] >= price_range[0]) &
    (df["price"] <= price_range[1]) &
    (df["bedrooms"].isin(bedrooms)) &
    (df["bathrooms"].isin(bathrooms))
]

# Display dataframe
st.subheader("🌟Filtered Dataset")
st.dataframe(filtered_df)

# Area range binning
filtered_df["area range"] = pd.cut(
filtered_df["area"],
bins=[0, 1000, 2000, 3000, float("inf")],
labels=["Small", "Medium", "Large", "Very Large"]
)


# Additional Visualization
st.subheader("💵Price by Furnishing Status")
fig_furnishing = px.box(filtered_df, x="furnishingstatus", y="price", color="furnishingstatus", template="plotly_dark")
st.plotly_chart(fig_furnishing, use_container_width=True)
st.markdown("👉This graph is Streamlit and Plotly to visualize property prices based on furnishing status.")

# pie
st.subheader("📈Area Range Distribution")
fig_area = px.pie(filtered_df, names="area range", title="🌟Distribution of Area Range", template="plotly_dark")
st.plotly_chart(fig_area, use_container_width=True)
st.markdown("👉This graph is  Streamlit and Plotly code snippet for visualizing the distribution of area ranges with a pie chart is well-structured.")

# histogram
st.subheader("💰Price Distribution")
fig_price = px.histogram(filtered_df, x="price", nbins=30, title="🌟Price Histogram", template="plotly_dark")
st.plotly_chart(fig_price, use_container_width=True)
st.markdown("👉this graph is represent diiferent- different rooms prices.")

# Pie Chart
st.subheader("🌟Furnishing Status Distribution")
pie_fig = px.pie(filtered_df, names="furnishingstatus", title="🌟Furnishing Status")
st.plotly_chart(pie_fig)
st.markdown("👉Through this graph it is shown that how many flat furnished, semi-furnished, unfurnised according to the price.")

# bar
st.subheader("🌟Average Price by Number of Bedrooms")
avg_price = filtered_df.groupby("bedrooms")["price"].mean().reset_index()
bar_fig = px.bar(avg_price, x="bedrooms", y="price", title="🌟Average Price by Bedrooms")
st.plotly_chart(bar_fig)
st.markdown("👉This graph shows here how many bedrooms are in this flat according to the price")