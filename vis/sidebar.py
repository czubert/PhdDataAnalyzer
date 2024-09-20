import streamlit as st

# from vis_helpers import vis_utils
from constants import LABELS


def sidebar_head():
    """
    Sets Page title, page icon, layout, initial_sidebar_state
    Sets position of radiobuttons (in a row or one beneath another)
    Shows logo in the sidebar
    """
    st.set_page_config(
        page_title="PhD Data Analyzer",
        layout="wide",
        initial_sidebar_state="auto"
    )

    st.set_option('deprecation.showfileUploaderEncoding', False)


def print_widget_labels(widget_title, margin_top=5, margin_bottom=10):
    """
    Prints Widget label on the sidebar and lets adjust its margins easily
    :param widget_title: Str
    """
    st.sidebar.markdown(
        f"""<p style="font-weight:500; margin-top:{margin_top}px;margin-bottom:{margin_bottom}px">{widget_title}</p>""",
        unsafe_allow_html=True)


def choose_spectra_type():
    spectra_types = ['EMPTY', 'BWTEK', 'RENI', 'WITEC', 'WASATCH', 'TELEDYNE', 'JOBIN']
    spectrometer = st.sidebar.selectbox(
        "Spectra type",
        spectra_types,
        format_func=LABELS.get,
        index=0)
    return spectrometer
