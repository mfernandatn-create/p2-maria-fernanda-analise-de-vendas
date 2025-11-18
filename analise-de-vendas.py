import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise de Vendas", layout="wide")

st.title("📊 Dashboard de Análise de Vendas")

uploaded_file = st.file_uploader("Envie sua base de vendas (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Prévia dos dados")
    st.dataframe(df.head())

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Total de vendas")
        total = df["vendas"].sum()
        st.metric("Total vendido", f"R$ {total:,.2f}")

    with col2:
        st.subheader("Quantidade total de itens")
        qtd = df["quantidade"].sum()
        st.metric("Itens vendidos", f"{qtd:,}")

    st.subheader("Gráfico de vendas por produto")
    fig = px.bar(df, x="produto", y="vendas", color="produto")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Envie um arquivo CSV para iniciar a análise.")
