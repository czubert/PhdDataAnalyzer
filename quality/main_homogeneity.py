import streamlit as st


def homogeneity():
    """

    :return:
    """

    st.markdown('**Powtarzalność i Jednorodność podłoży SERS**')

    with st.expander('TODO'):
        st.markdown("1. **Dane wejściowe** \n"
                    "   - Pierwsza grupa - widma PMBA\n"
                    "       - widma PMBA dla ostatniej modyfikacji podłoża\n"
                    "       - widma PMBA dla nowej modyfikacji podłoża\n"
                    "   - Druga grupa - widma teł\n"
                    "       - widma teł dla ostatniej modyfikacji podłoża\n"
                    "       - widma teł dla nowej modyfikacji podłoża\n"

                    "2. **Przygotowanie widm**\n"
                    "   - normalizacja (?)\n"
                    "   - baseline correction (?)\n"

                    "3. **Metody porównawcze** - (liczymy odchylenie między widmami pojedynczego "
                    "podłoża (poniższymi metodami), uśredniamy wynik dla wszystkich podłoży z danej modyfikacji, "
                    "i porównujemy jednorodność przed i po modyfikacji)\n"
                    "   - Porównanie widm dla obu grup z wykorzystaniem:\n"
                    "       * Miar statystycznych: RMSE or R<sup>2</sup>\n"
                    "       * Testów statystycznych, żeby zweryfikować, czy różnice są istotne statystycznie:\n"
                    "           + ANOVA\n"
                    "           + t-studenta\n"
                    "           + chi-kwadrat\n"

                    "4. **Prezentacja wyników**\n"
                    "   - Pokazać przykładowy odcięty baseline, żeby było widać, "
                    "na czym polega baseline correction (?)\n"
                    "   - wykres z uśrednionymi widmami przed i po modyfikacji z podanymi parametrami, "
                    "które oceniają jak bardzo się różnią:\n"
                    "       * podana miara statystyczna (RMSE lub inna)\n"
                    "       * podane czy różnice są istotne statystycznie (wynik testu statystycznego)\n"
                    "       * dla widm PMBA - EF\n",
                    unsafe_allow_html=True
                    )


if __name__ == '__main__':
    homogeneity()
