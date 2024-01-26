import streamlit as st
import pandas as pd

view = [100, 200, 300]

view

st.write('# Youtube view')
st.bar_chart(view)

sview = pd.Series(view)
sview

