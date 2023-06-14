import streamlit as st
import pandas as pd
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def fivenum(data):
    """Five-number summary."""
    return np.percentile(data, [0, 25, 50, 75, 100], method="midpoint")

uploaded_file = st.file_uploader("Upload your data file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write("Number of columns:", len(dataframe.columns))
    st.write("Number of rows:", len(dataframe.index))
    st.write(dataframe.dtypes)
    column = st.selectbox("column:", dataframe.columns)
    dataframe[column]
    if is_numeric_dtype(dataframe[column]):
        fivenum_stats = fivenum(dataframe[column])
        st.write(fivenum_stats)
        fig = plt.figure(figsize = (3,5))
        sns.kdeplot(dataframe[column])
        st.pyplot(fig)
    else:
        st.write(dataframe[column].value_counts())
        st.bar_chart(dataframe[column].value_counts())