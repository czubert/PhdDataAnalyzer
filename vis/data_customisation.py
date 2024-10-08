import streamlit as st

from constants import LABELS
from data_processing import utils


def get_deg_win(chart_type, spectra_conversion_type, df_columns):
    """
    Fills in right side of webside with sliders for polynomial degree and smoothening window

    Args:
        chart_type (str): type of plot
        spectra_conversion_type (str): type of data preprocessing
        df_columns (list): df column names

    Returns:
        dict: polynomial degree and smoothening window tuple for each data series
    """
    if spectra_conversion_type == 'RAW':
        vals = None

    elif chart_type == 'SINGLE':
        vals = {}
        for col in df_columns:
            vals[col] = (utils.choosing_regression_degree(col), utils.choosing_smoothening_window(col))

    elif chart_type in {'GS', 'P3D', 'MS'}:
        deg = utils.choosing_regression_degree()
        window = utils.choosing_smoothening_window()
        vals = {col: (deg, window) for col in df_columns}

    else:
        raise ValueError('Unknown chart type')
    
    return vals


def separate_spectra(normalized):
    """
    Shift spectra between each other.
    Depending on the conversion type it takes different values
    :param normalized:
    :return: Int or Float
    """
    # depending on conversion type we have to adjust the scale
    if normalized:
        shift = st.slider(LABELS['SHIFT'], 0.0, 1.0, 0.0, 0.1)
        shift = float(shift)
    else:
        shift = st.slider(LABELS['SHIFT'], 0, 30000, 0, 250)
        shift = int(shift)
    return shift
