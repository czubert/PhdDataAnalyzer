import base64

import plotly.express as px
import plotly.io as pio
import streamlit as st
import pandas as pd
import peakutils


def trim_spectra(df):
    # trim raman shift range
    min_, max_ = int(float(df.index.min())), int(float(df.index.max())) + 1
    min_max = st.slider('Custom range', min_value=min_, max_value=max_, value=[min_, 1800])
    min_rs, max_rs = min_max  # .split('__')
    min_rs, max_rs = float(min_rs), float(max_rs)
    mask = (min_rs <= df.index) & (df.index <= max_rs)
    return df[mask]


def get_plot_description():
    print_widget_labels('Labels')
    xaxis = st.text_input('X axis name', r'Raman Shift [cm <sup>-1</sup>]')
    yaxis = st.text_input('Y axis name', r'Intensity [au]')
    title = st.text_input('Title', r'Raman Spectra')
    chart_titles = {'x': xaxis, 'y': yaxis, 'title': title}
    return chart_titles


def get_plot_description_pca():
    print_widget_labels('Labels')
    xaxis = st.text_input('X axis name', r'PC 1')
    yaxis = st.text_input('Y axis name', r'PC 2')
    title = st.text_input('Title', r'PCA')
    chart_titles = {'x': xaxis, 'y': yaxis, 'title': title}
    return chart_titles


def print_widgets_separator(n=1, sidebar=False):
    """
    Prints customized separation line on sidebar
    """
    html = """<hr style="height:1px;
            border:none;color:#fff;
            background-color:#999;
            margin-top:5px;
            margin-bottom:10px"
            />"""

    for _ in range(n):
        if sidebar:
            st.sidebar.markdown(html, unsafe_allow_html=True)
        else:
            st.markdown(html, unsafe_allow_html=True)


def print_widget_labels(widget_title, margin_top=5, margin_bottom=10):
    """
    Prints Widget label on the sidebar and lets adjust its margins easily
    :param widget_title: Str
    """
    st.markdown(
        f"""<p style="font-weight:500; margin-top:{margin_top}px;margin-bottom:{margin_bottom}px">{widget_title}</p>""",
        unsafe_allow_html=True)


def subtract_baseline_and_smoothen(df, vals, cols_name=False):
    """
    Subtracting baseline from original df, and smoothing the curve using rolling average
    :param df: Original DataFrame
    :param vals: polynomial degree and window for rolling average both Int
    :param cols_name:  Boolean
    :return: DataFrame
    """
    baselines = pd.DataFrame(index=df.index)
    baselined = pd.DataFrame(index=df.index)
    flattened = pd.DataFrame(index=df.index)

    for col in df.columns:
        # for baseline correction in PCA module, as there are some differences in input
        col_name = col
        if cols_name:
            col_name = 'col'

        tmp_spectrum = df[col].dropna()
        tmp_spectrum = pd.Series(peakutils.baseline(tmp_spectrum, vals[col_name][0]), index=tmp_spectrum.index)
        baselines[col] = tmp_spectrum

        baselined[col] = df[col] - baselines[col]
        flattened[col] = baselined[col].rolling(window=vals[col_name][1], min_periods=1, center=True).mean()

    return df, baselines, baselined, flattened
