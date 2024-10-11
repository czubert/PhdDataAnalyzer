import streamlit as st

from quality import main_repeatability, main_enhancement, main_homogeneity, main_summation
from vis import main_page, vis

st.set_page_config(
    initial_sidebar_state="auto",
    layout="wide",
    page_title="PhD thesis"
)


def main():
    """
    Main is responsible for the visualisation of everything connected with streamlit.
    It is the web application itself.
    """
    analysis_type = st.sidebar.radio("Analysis type",
                                     ['Strona główna', 'Wizualizacja', 'Wzmocnienie i tło', 'Powtarzalność',
                                      'Jednorodność', 'Podsumowanie'])

    if analysis_type == 'Strona główna':
        main_page.main_page()
    if analysis_type == 'Wizualizacja':
        vis.visualisation()
    elif analysis_type == 'Wzmocnienie i tło':
        main_enhancement.quality()
    elif analysis_type == 'Powtarzalność':
        main_repeatability.repeatability()
    elif analysis_type == 'Jednorodność':
        main_homogeneity.homogeneity()
    elif analysis_type == 'Podsumowanie':
        main_summation.summation()


if __name__ == '__main__':
    main()

    print("Streamlit finished it's work")
