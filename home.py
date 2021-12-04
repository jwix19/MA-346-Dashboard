"""
Name: Andrew D'Annolfo & Joey Wix
Section: MA 346
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

image = Image.open("used car.jfif")

def app():
    st.title("Craigslist Used Car Exploratory Data Analysis")
    st.write("By Andrew D'Annolfo & Joey Wix")

    st.title("Purpose")
    st.write("This dashboard is used to perform Exploratory Data Analysis on used car data"
             "from Craigslist. Please use the corresponding tabs on the navigation bar to "
             "explore plots of predictor variables vs. response variable and associations "
             "between variables.")
    st.image(image)
