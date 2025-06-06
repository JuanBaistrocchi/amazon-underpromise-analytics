# 📦 AMZ Underpromise Analytics

Este repositorio contiene un análisis simulado (¡no real!) del comportamiento de under-promising en las órdenes de AMZ México.  
El objetivo es identificar patrones en los tiempos de entrega prometidos vs. los reales, y entender cómo varían por región, distancia y seller.

---

## 🧠 Scripts Principales

- `scripts/app.py`: Dashboard interactivo en Streamlit.
- `scripts/generar_reporte_pptx.py`: Exporta gráficos y métricas a PowerPoint automáticamente.
- `notebooks/Terminal Mexico.ipynb`: Exploración, limpieza, enriquecimiento de datos y análisis de correlación.

---

## ⚙️ Cómo ejecutar

```bash
# Crear entorno y activar dependencias si hiciera falta
pip install -r requirements.txt

# Ejecutar dashboard interactivo
streamlit run scripts/app.py

📊 Visualizaciones
Barras por región de origen y destino

Top sellers con mejor under-promise

Heatmap por rutas Origen → Destino

Diagrama de Sankey

Correlación entre distancia (km) y delta_days

🛠️ Herramientas Usadas
Python, Pandas, Plotly, Seaborn, Streamlit

JupyterLab en SageMaker Studio

GitHub para control de versiones

GitHub Actions (próximamente para automatización)
