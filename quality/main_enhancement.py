import streamlit as st


def quality():
    """
    Package responsible for counting the reproducibilty and hogeneity of SERS substrates.
    :return:
    """

    st.markdown('**Jakość podłoży SERS**')
    with st.expander('TODO'):
        st.markdown("1. **Dane wejściowe** \n"
                    "   - Pierwsza grupa - widma PMBA\n"
                    "       - uśrednione widmo z widm PMBA dla ostatniej modyfikacji podłoża\n"
                    "       - uśrednione widmo z widm PMBA dla nowej modyfikacji podłoża\n"
                    "   - Druga grupa - widma teł\n"
                    "       - uśrednione widmo z widm teł dla ostatniej modyfikacji podłoża\n"
                    "       - uśrednione widmo z widm teł dla nowej modyfikacji podłoża\n"
    
                    "2. **Przygotowanie widm**\n"
                    "   - normalizacja (?)\n"
                    "   - baseline correction (?)\n"
                    "   - średnia z widm (?)\n"
                    "   - jeżeli wszystkie z powyższych, to czy wpierw normalizujemy i usuwamy "
                    "baselina a potem liczymy średnią, czy odwrotnie?\n"
    
                    "3. **Metody porównawcze**\n"
                    "(Porównujemy ze sobą uśrednione widma, żeby pokaząc globalnie poprawę wzmocnienia i jakości tła)\n"
                    "   - Porównanie widm dla obu grup z wykorzystaniem:\n"
                    "       * Miar statystycznych: RMSE or R<sup>2</sup>\n"
                    "       * Testów statystycznych, żeby zweryfikować, czy różnice są istotne statystycznie:\n"
                    "           + ANOVA\n"
                    "           + t-studenta\n"
                    "           + chi-kwadrat\n"
                    "   - Porównanie widm pierwszej grupy (PMBA) z wykorzystaniem\n"
                    "       * Enhancement Factor (EF)\n"
    
                    "4. **Prezentacja wyników**\n"
                    "   - Pokazać przykładowy odcięty baseline, żeby było widać, na czym polega baseline correction (?)\n"
                    "   - wykres z uśrednionymi widmami przed i po modyfikacji z podanymi parametrami, "
                    "które oceniają jak bardzo się różnią:\n"
                    "       * podana miara statystyczna (RMSE lub inna)\n"
                    "       * podane czy różnice są istotne statystycznie (wynik testu statystycznego)\n"
                    "       * dla widm PMBA - EF\n"
                    ,
                    unsafe_allow_html=True
                    )


if __name__ == '__main__':
    quality()
