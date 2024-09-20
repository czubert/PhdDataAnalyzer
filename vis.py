import streamlit as st
from vis import main_page, vis


def main():
    """
    Main is responsible for the visualisation of everything connected with streamlit.
    It is the web application itself.
    """

    # TODO porównanie jednorodności/powtarzalność + błąd (inny dla obu przypadków)
    # TODO porównanie teł/pmba przez RMSE + EF
    # TODO porównanie jak kolejne zmiany wpłynęły na ostatnią modyfikację i na końcu, jak wygląda porównanie
    #  pierwszych do końcowego produktu

    # # Radiobuttons in one row
    # st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    # # Sets sidebar's header and logo
    # sidebar.sidebar_head()
    #
    analysis_type = st.sidebar.radio("Analysis type", ['Strona główna', 'Wizualizacja', 'Jakość widm', 'Powtarzalność'])

    if analysis_type == 'Strona główna':
        main_page.main_page()
    if analysis_type == 'Wizualizacja':
        vis.visualisation()
    # elif analysis_type == 'PCA':
    #     pca.main()
    # elif analysis_type == 'EF':
    #     enhancement_factor.main()
    # elif analysis_type == 'RSD':
    #     rsd.main()
    # authors.show_developers()


if __name__ == '__main__':
    main()

    print("Streamlit finished it's work")
