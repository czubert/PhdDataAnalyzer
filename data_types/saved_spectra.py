import pandas as pd

from data_processing import utils
from constants import LABELS


def read_saved_spectra(uploaded_files, delim):
    """
    Reads numeric data from file and creates DataFrame
    :param uploaded_files: Streamlit uploader file
    :return: Dict of DataFrames
    """
    reni_data = {}
    spectra_params_uploaded = {'sep': delim, 'decimal': '.', 'skipinitialspace': True,
                               'header': 0}

    # Iterates through each file, converts it to DataFrame and adds to temporary dictionary
    for uploaded_file in uploaded_files:
        data = utils.read_spec(uploaded_file, spectra_params_uploaded)
        import streamlit as st
        st.write(data)
        data.dropna(inplace=True, how='any', axis=0)
        data[LABELS["RS"]] = data[LABELS["RS"]].round(decimals=0)
        data.set_index(LABELS["RS"], inplace=True)

        reni_data[uploaded_file.name[:-4]] = data

    df = pd.concat([reni_data[data_df] for data_df in reni_data], axis=1)
    df.dropna(inplace=True, how='any', axis=0)

    return df
