import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import os

# -----------------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------------
st.set_page_config(page_title="Underpromise Dashboard", layout="wide")
st.title("📦 Dashboard de Underpromise - Amazon México")

# -----------------------------------
# CARGA DE DATOS
# -----------------------------------
df_sellers = pd.read_csv("datos/Top10Sellers.csv")
df_dest = pd.read_csv("datos/PorRegionDestino.csv")
df_origin = pd.read_csv("datos/PorRegionOrigen.csv")
df_routes = pd.read_csv("datos/Top10Rutas.csv")

# -----------------------------------
# MÉTRICAS GLOBALES
# -----------------------------------
st.subheader("📊 Métricas Generales")
df_summary = pd.read_csv("datos/ResumenGlobal.csv")
cols = st.columns(3)
cols[0].metric(label="Total de órdenes", value=int(df_summary.iloc[0, 1]))
cols[1].metric(label="% Under-Promise", value=df_summary.iloc[2, 1])
cols[2].metric(label="Promedio Delta Days", value=df_summary.iloc[5, 1])

# -----------------------------------
# GRÁFICOS
# -----------------------------------
st.subheader("🏬 Under-Promise por Región")
c1, c2 = st.columns(2)

with c1:
    fig1 = px.bar(df_dest, x='destination_region', y='under_rate_pct',
                  title="Región de Destino", labels={'under_rate_pct': '% Under-Promise'},
                  color='under_rate_pct', template='plotly_white')
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    fig2 = px.bar(df_origin, x='origin_region', y='under_rate_pct',
                  title="Región de Origen", labels={'under_rate_pct': '% Under-Promise'},
                  color='under_rate_pct', template='plotly_white')
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------------
# SELLERS
# -----------------------------------
st.subheader("🏅 Top 10 Sellers por Under-Promise Rate")
fig3 = px.bar(df_sellers.sort_values('under_rate_pct'),
              x='under_rate_pct', y='seller_id', orientation='h',
              labels={'under_rate_pct': '% Under-Promise', 'seller_id': 'Seller ID'},
              title="Sellers con mejor desempeño (>= 20 órdenes)",
              template='plotly_white')
st.plotly_chart(fig3, use_container_width=True)

# -----------------------------------
# HEATMAP DE RUTAS
# -----------------------------------
st.subheader("🗺️ Heatmap de Under-Promise por Ruta Origen → Destino")
pivot = df_routes.pivot(index='origin_region', columns='destination_region', values='under_rate_pct')
fig4, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="Blues", ax=ax)
st.pyplot(fig4)

# -----------------------------------
# SANKEY DIAGRAM
# -----------------------------------
st.subheader("🔀 Sankey: Flujo de Rutas con Mayor Under-Promise")
labels = list(pd.unique(df_routes[['origin_region', 'destination_region']].values.ravel()))
label_map = {label: i for i, label in enumerate(labels)}

sources = df_routes['origin_region'].map(label_map)
targets = df_routes['destination_region'].map(label_map)
values = df_routes['under_rate_pct'].round(1)

fig5 = go.Figure(data=[go.Sankey(
    node=dict(pad=15, thickness=20, line=dict(color="gray", width=0.5), label=labels, color="lightblue"),
    link=dict(source=sources, target=targets, value=values, label=[f"{v:.1f}%" for v in values], color="lightgray")
)])

fig5.update_layout(title_text="Top Rutas con Mayor Under-Promise", font_size=12)
st.plotly_chart(fig5, use_container_width=True)

# -----------------------------------
# NOTA FINAL
# -----------------------------------
st.markdown("---")
st.markdown("App construida con 💡 por un PM obsesionado con delivery accuracy.")
