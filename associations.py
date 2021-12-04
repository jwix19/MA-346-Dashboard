"""
Name: Andrew D'Annolfo & Joey Wix
Section: MA 346
"""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import kruskal
from scipy.stats import chi2_contingency
import streamlit as st
from scipy import stats


def associations(df):
    global association
    st.write()
    vars = df.columns.tolist()
    vars.pop(0)
    variables = st.sidebar.multiselect("Please select two variables to test: ", vars)
    if len(variables) == 0:
        var1 = vars[1]
        var2 = vars[2]
    elif len(variables) == 1:
        var1 = variables[0]
        var2 = vars[2]
    elif len(variables) == 2:
        var1 = variables[0]
        var2 = variables[1]
    price = vars.pop(1)
    cts_vars = [price, vars.pop(1), vars.pop(4)]
    if var1 in cts_vars and var2 in cts_vars:
        test = "Pearson Correlation because both variables are continuous"
        a = pearsonr(df[var1], df[var2])
        association = f"For the variables {var1} and {var2}, we will use the {test}. This will " \
                      f"yield a coefficient of {a[0]:.3f}."

    elif var1 in cts_vars and var2 not in cts_vars:
        test = "One-Way Anova because we have one categorical " \
               "and one continuous variable"
        grouped = df.loc[:, [var1, var2]].groupby(var2).agg(['mean', 'std'])
        grouped = grouped.dropna()

        i = 0
        d = {}
        while i < len(grouped):
            d[grouped.index[i]] = [grouped.iloc[i, 0], grouped.iloc[i, 1]]
            i += 1

        var_holder = {}
        df_holder = {}
        final_df = pd.DataFrame()

        for a in d.keys():
            var_holder[a] = np.random.normal(loc=d[a][0], scale=d[a][1], size=100)
            df_holder[a] = pd.DataFrame(var_holder[a])
            df_holder[a]['Group'] = a
            for df in df_holder.values():
                final_df = final_df.append(df)
        final_df[var1] = final_df[0]
        final_df = final_df.drop(0, axis=1)

        F, p = stats.f_oneway(*[final_df[final_df['Group'] == b][var1] for b in d.keys()])
        a = [F, p]
        association = f"For the variables {var1} and {var2}, we will use the {test}. This test " \
                      f"yields an F-statistic of {a[0]:.3f} that has a p-value of {a[1]:.3f}."

    elif var1 not in cts_vars and var2 in cts_vars:
        test = "One-Way Anova because we have one categorical " \
               "and one continuous variable"
        grouped = df.loc[:, [var2, var1]].groupby(var1).agg(['mean', 'std'])
        grouped = grouped.dropna()

        i = 0
        d = {}
        while i < len(grouped):
            d[grouped.index[i]] = [grouped.iloc[i, 0], grouped.iloc[i, 1]]
            i += 1

        var_holder = {}
        df_holder = {}
        final_df = pd.DataFrame()

        for a in d.keys():
            var_holder[a] = np.random.normal(loc=d[a][0], scale=d[a][1], size=100)
            df_holder[a] = pd.DataFrame(var_holder[a])
            df_holder[a]['Group'] = a
            for df in df_holder.values():
                final_df = final_df.append(df)
        final_df[var2] = final_df[0]
        final_df = final_df.drop(0, axis=1)

        F, p = stats.f_oneway(*[final_df[final_df['Group'] == b][var2] for b in d.keys()])
        a = [F, p]
        association = f"For the variables {var1} and {var2}, we will use the {test}. This test " \
                      f"yields an F-statistic of {a[0]:.3f} that has a p-value of {a[1]:.3f}."

    elif var1 not in cts_vars and var2 not in cts_vars:
        test = "Chi-Squared Test for Independence because both variables are categorical"
        ct = pd.crosstab(df[var1], df[var2], margins=True)
        obs = np.array(ct.iloc[:-1, :-1])
        a = chi2_contingency(obs)[0:3]
        association = f"For the variables {var1} and {var2}, we will use the {test}. This test " \
                      f"yields a Chi-Squared-statistic of {a[0]:.3f}, a p-value of {a[1]:.3f}, and " \
                      f"degrees of freedom of {a[2]:.3f}."

    return association


def app():
    st.title("Testing Associations Between Variables")
    df = pd.read_csv("cl_used_car_clean.csv")
    st.write("This page examines the relationship between variables. We have both numeric and "
             "categorical data, which poses a problem for calculating correlations unless "
             "dummy variables are created.")
    st.write("To combat this issue, we will use three tests for analyzing relationships "
             "between variables. We will use the Pearson Correlation Coefficient, One-Way ANOVA,"
             "and the Chi-Squared Test of Independence.")

    st.write(associations(df))
