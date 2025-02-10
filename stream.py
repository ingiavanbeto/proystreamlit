import streamlit as st
#import pymysql
import pandas as pd
#import plotly.express as px
import time
import numpy as np
import altair as alt
#import matplotlib.pyplot as plt

# Configuración de la conexión a MySQL
def obtener_datos():
    try:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="x",
            database="pruebas"
        )
        consulta = "SELECT id_monitoreo, valor,(select nombre FROM sensor WHERE id_sensor = tipo_sensor) as Nombre FROM monitoreo where tipo_sensor = 1 Order by id_monitoreo DESC limit 1000;"
        df = pd.read_sql_query(consulta, conexion)

        consulta2 = "SELECT valor FROM monitoreo where tipo_sensor = 1 Order by id_monitoreo DESC limit 1;"
        d2 = pd.read_sql(consulta2, conexion)
        conexion.close()

        return df,d2
    except Exception as e:
        st.error(f"Error al conectar con la base de datos: {e}")
        return None
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.header("_Streamlit_ is :blue[cool] :sunglasses:")
st.header("This is a header with a divider", divider="gray")
st.header("These headers have rotating dividers", divider=True)
st.header("One", divider=True)
st.header("Two", divider=True)
st.header("Three", divider=True)
st.header("Four", divider=True)
with st.spinner("Wait for it..."):
    time.sleep(5)
st.success("Done!")
st.button("Rerun")
# Configuración de la aplicación Streamlit
st.title("📊 Dashboard de Monitoreo")
st.write("Esta aplicación muestra los datos de la tabla **monitoreo** en una gráfica interactiva.")
# Obtener datos de la base de datos
_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig

st.write("This is some text.")

st.slider("This is a slider", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))
