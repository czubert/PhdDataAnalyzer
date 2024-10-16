import streamlit as st


def homogeneity():
    """

    :return:
    """

    st.markdown('**Powtarzalność i Jednorodność podłoży SERS**')
    # TODO zrobić opcję inputu całych folderów. Następnie skrypt ma czytać info ze ścieżki: brak modyfikacji/modyfikacja
    #  tło/PMBA oraz numer podłoża, dzięki temu mam 3 dodatkowe featury, po których będę liczył sobie std. dev.

    # TODO odległość euklidesowa?
    # TODO normalizacja, żeby porównywać widma o różnych intensywnościach
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
                    "   - wykres z kilkoma pomiarami z pojedynczego podłoża (po usunięciu dwóch skrajnych) "
                    "z podaną metodą jak liczyliśmy jednorodność dla tego pojedynczego podłoża."
                    " jako przykład co liczyliśmy. A pod spodem wyliczenia (zgodnie z opisanym wyżej sposobem)"
                    "dla wszystkich podłoży z danej modyfikacji i przed nią. Porównanie wyniku między nimi.\n"
                    "       * podana miara statystyczna (RMSE lub inna)\n"
                    "       * podane czy różnice są istotne statystycznie (wynik testu statystycznego)\n"
                    "       * dla widm PMBA - EF\n"
                    ,
                    unsafe_allow_html=True
                    )


if __name__ == '__main__':
    homogeneity()
