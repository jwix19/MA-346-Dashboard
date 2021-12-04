"""
Name: Andrew D'Annolfo & Joey Wix
Section: MA 346
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def cts_scatter(df):
    st.write()
    vars = df.columns.tolist()
    vars.pop(0)
    price = vars.pop(1)
    cts_vars = [vars.pop(1), vars.pop(4)]
    cts_variables = st.sidebar.multiselect("Please select one continuous predictor variable: ", cts_vars)
    if len(cts_variables) == 0:
        var1 = cts_vars[0]
    else:
        var1 = cts_variables[0]
    var_format1 = "".join(var1).capitalize()
    var_format2 = "".join(price).capitalize()
    x = df[var1]
    y = df[price]
    plt.scatter(x, y, color='k', marker='D', s=15)
    plt.title(f"{var_format1} vs. {var_format2} Scatter Plot")
    plt.xticks(rotation=45)


def cat_scatter(df):
    st.write()
    vars = df.columns.tolist()
    vars.pop(0)
    price = vars.pop(1)
    vars.pop(1)
    vars.pop(4)
    cat_vars = vars
    cat_variables = st.sidebar.multiselect("Please select one categorical predictor variable: ", cat_vars)
    if len(cat_variables) == 0:
        var1_cat = cat_vars[1]
    else:
        var1_cat = cat_variables[0]
    var_cat_format1 = "".join(var1_cat).capitalize()
    var_cat_format2 = "".join(price).capitalize()
    x = df[var1_cat]
    y = df[price]
    sns.stripplot(x, y)
    plt.xticks(rotation=45)
    plt.title(f"{var_cat_format1} vs. {var_cat_format2} Strip Plot")


def app():
    st.title("Plotting Response against Predictor Variables")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    df = pd.read_csv("cl_used_car_clean.csv")
    st.pyplot(cts_scatter(df))
    st.pyplot(cat_scatter(df))


