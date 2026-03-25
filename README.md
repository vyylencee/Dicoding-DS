# Coding Camp 2026 Dashboard

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.11
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```

## Penjelasan 

RMF Analysis digunakan untuk menilai Recency, Frequency, Monetary.
Recency sendiri digunakan untuk menghitung berapa hari sejak customer membeli barang
Frequency adalah jumlah pembelian customer
Monetary adalah jumlah yang dibayarkan oleh customer
Kegunaan RFM Analysis ini ialah perusahaan dapat mengetahui besar frekuensi pelanggan yang berbelanja apakah repeat-order atau tidak, bahkan seberapa banyak yang customer spend dalam perusahaan mereka.

Geospatial ini pada intinya adalah kita dapat melihat visualisasi persebaran data lewat peta. Salah satunya kita gunakan library folium.
Dengan geospatial ini, perusahaan dapat mengetahui lebih detail tempat mana saja yang sering berbelanja.

Clustering manual dimanfaatkan untuk menghitung rentang jumlah pelanggan berdasarkan kota yang ada. Dengan ini perusahaan juga menjadi tahu negara mana yang menjadi salah satu target pasar mereka.

Clustering binning dimanfaatkan untuk pengkategorian dari RMF Analysis yang ada. Sayangnya, frequency pelanggan dalam membeli smeua sama yaitu 1 sehingga tidak ada variasi dari nilai frequencynya.