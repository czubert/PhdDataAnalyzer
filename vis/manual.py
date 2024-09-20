import re

import streamlit as st
import streamlit.components.v1 as components

from constants import LABELS
from data_processing import utils

def example_data_html(spectrometer):
    """
    Prepares string to show in manual, i.e. *.csv
    :param spectrometer: Str, name of the chosen spectrometer
    :return: Str
    """
    files = utils.load_example_files()
    text = files[0].read()
    files[0].seek(0)
    html = f'<div style="font-family: monospace"><p>{text}</p></div>'
    html = re.sub(r'\n', r'<br>', html)
    return html


def show_manual():
    """
    Shows manual on front page if data is not uploaded
    """

    with st.expander('BWTEK'):
        # warnings with tips how to work with this program
        st.header('Data visualisation')
        st.subheader('Short manual on how to import data')
        st.warning("First choose spectra type from left sidebar (if it doesn't work try different one)")
        st.warning('Then upload file or files for visualisation (or load example data) from left sidebar')
        st.write('')

        st.write('Upload raw data in *.txt format')
        st.write('Original data consists of metadata and data')
        html = example_data_html('BWTEK')
        components.html(html, height=200, scrolling=True)
