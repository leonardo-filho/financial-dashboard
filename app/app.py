import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Análise de Vendas - 2024")

# === Carregar dados ===
@st.cache_data
@st.cache_data
def load_data():
    df = pd.read_csv("data/sales_data_2024.csv", parse_dates=["Date of Sale"])
    df["Month"] = df["Date of Sale"].dt.strftime("%Y-%m")
    df["Day"] = df["Date of Sale"].dt.date
    return df


df = load_data()

# === Filtros ===
st.sidebar.header("Filtros")
product = st.sidebar.multiselect("Produto", df["Product Name"].unique())
channel = st.sidebar.multiselect("Canal de Venda", df["Sales Channel"].unique())
region = st.sidebar.multiselect("Região", df["Region"].unique())

df_filtered = df.copy()
if product:
    df_filtered = df_filtered[df_filtered["Product Name"].isin(product)]
if channel:
    df_filtered = df_filtered[df_filtered["Sales Channel"].isin(channel)]
if region:
    df_filtered = df_filtered[df_filtered["Region"].isin(region)]

# === Gráfico de vendas mensais ===
monthly_sales = df_filtered.groupby("Month")["Total Sales Value"].sum().reset_index()
fig_month = px.bar(monthly_sales, x="Month", y="Total Sales Value", title="Vendas Totais por Mês")
st.plotly_chart(fig_month, use_container_width=True)

# === Gráfico por categoria ===
category_sales = df_filtered.groupby("Category")["Total Sales Value"].sum().reset_index()
fig_cat = px.pie(category_sales, values="Total Sales Value", names="Category", title="Distribuição por Categoria")
st.plotly_chart(fig_cat, use_container_width=True)

# === Dias sem vendas ===
sales_by_day = df_filtered.groupby("Day")["Total Sales Value"].sum()
zero_sales_days = sales_by_day[sales_by_day == 0].index

st.subheader("📅 Dias sem vendas:")
if zero_sales_days.empty:
    st.success("Sem dias com vendas zeradas!")
else:
    st.warning(f"{len(zero_sales_days)} dias com venda total = 0")
    st.dataframe(zero_sales_days)

# === Tabela detalhada ===
st.subheader("📋 Tabela de dados filtrados")
st.dataframe(df_filtered)
