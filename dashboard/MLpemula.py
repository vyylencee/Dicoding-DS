import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

cust = pd.read_csv('data/cust.csv')
geographic = pd.read_csv('data/geographic.csv')
orders = pd.read_csv('data/orders.csv')
order_items = pd.read_csv('data/order_items.csv')
product = pd.read_csv('data/product.csv')
payment = pd.read_csv('data/payment.csv')

st.title('Data Science Project :sparkles:')
st.write('Proyek Analisis Data - Penggunaan E-Commerce')

col1, col2 = st.columns(2)

with col1:
    st.header('Top 5 Kota dengan Penjualan Terbanyak')
    the_most_order_city = pd.merge(
        left=cust,
        right=orders,
        how='left',
        left_on='customer_id',
        right_on='customer_id'
    )

    top_city = the_most_order_city.groupby('customer_city')['order_id'] \
        .nunique() \
        .sort_values(ascending=False) \
        .head(5)

    fig, ax = plt.subplots()
    top_city.plot(kind='bar', ax=ax)

    ax.set_title('Top 5 Kota dengan Jumlah Pesanan Terbanyak')
    ax.set_xlabel('Kota')
    ax.set_ylabel('Jumlah Pesanan')
    plt.xticks(rotation=45)

    st.pyplot(fig)

with col2:
    st.header('Top 3 Kategori Produk dengan Penjualan Terbanyak')
    top_product = pd.merge(
        left=product,
        right=order_items,
        how='left',
        left_on='product_id',
        right_on='product_id'
    )

    top_product.groupby(by='product_category_name').order_id.nunique().sort_values(ascending=False).reset_index().head(10)

    top_category = top_product.groupby('product_category_name')['order_id'] \
        .nunique() \
        .sort_values(ascending=False) \
        .head(3)

    fig, ax = plt.subplots()
    top_category.plot(kind='bar', ax=ax)

    ax.set_title('Top 3 Produk dengan Jumlah Penjualan Terbanyak')
    ax.set_xlabel('Produk')
    ax.set_ylabel('Jumlah Penjualan')
    plt.xticks(rotation=45)

    st.pyplot(fig)