"""
Name: Andrew D'Annolfo & Joey Wix
Section: MA 346
"""
import home
import plots
import associations
import streamlit as st


pages = {
    "Home Page": home,
    "Plots": plots,
    "Associations": associations}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Tabs", list(pages.keys()))
    page = pages[selection]
    page.app()


main()
