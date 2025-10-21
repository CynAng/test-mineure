import streamlit as st
import pandas as pd
st.header("mon application")

nombres = [1,2,3,4]
carré = [1**2,2**2,3**2,4**2]

d = {"nombres": nombres, "carré": carré}
df=pd.DataFrame(d)

st.write(df)

