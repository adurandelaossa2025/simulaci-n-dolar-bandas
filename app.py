import streamlit as st

st.title("Simulador de Trading con Bandas Cambiarias por Adrián A. Durán")

# Entradas del usuario
piso = st.number_input("Precio piso del dólar ($)", value=1050.0, step=10.0)
techo = st.number_input("Precio techo del dólar ($)", value=1300.0, step=10.0)
capital_inicial = st.number_input("Capital inicial (ARS)", value=500000.0, step=1000.0)
num_ciclos = st.slider("Cantidad de ciclos al año", min_value=1, max_value=12, value=1)

# Cálculo de ganancia por ciclo
ganancia_por_ciclo = techo / piso
capital_final = capital_inicial * (ganancia_por_ciclo ** num_ciclos)
rendimiento_total = (capital_final - capital_inicial) / capital_inicial * 100

# Resultados
st.markdown("---")
st.subheader("Resultados")
st.write(f"🔁 Rentabilidad por ciclo: **{(ganancia_por_ciclo - 1) * 100:.2f}%**")
st.write(f"📈 Capital final estimado después de {num_ciclos} ciclos: **${capital_final:,.2f}**")
st.write(f"💰 Rentabilidad total acumulada: **{rendimiento_total:.2f}%**")

# Advertencia
st.markdown("---")
st.warning("Este simulador es solo educativo. El éxito de la estrategia depende de que el esquema de bandas se mantenga sin cambios inesperados.")
