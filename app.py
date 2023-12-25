import streamlit as st
import modules.cyk as cyk
import pandas as pd

st.header("Parsing Kalimat Indonesia Kelompok D3")
kalimat = st.text_input("Masukkan kalimat yang ingin diperiksa")
result = cyk.is_accepted(kalimat)
table = cyk.get_table_element(kalimat)
chart = pd.DataFrame(table)
chart = chart.style.highlight_null(props="color: transparent;").hide()

if kalimat:
    if result:
        st.success("Kalimat diterima")
        st.table(chart)
    else:
        st.error("Kalimat tidak diterima")
        st.table(chart)