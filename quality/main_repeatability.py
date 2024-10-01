import streamlit as st


def repeatability():
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

                    "3. **Metody porównawcze** - (Uśredniamy widma dla pojedynczych podłoży z danej modyfikacji"
                    " i porónujemy (poniższymi metodami) między podłożami, tak aby móc ocenić powtarzalność podłoży)\n"
                    "   - Porównanie widm dla obu grup z wykorzystaniem:\n"
                    "       * Miar statystycznych: RMSE or R<sup>2</sup>\n"
                    "       * Testów statystycznych, żeby zweryfikować, czy różnice są istotne statystycznie:\n"
                    "           + ANOVA\n"
                    "           + t-studenta\n"
                    "           + chi-kwadrat\n"

                    "4. **Prezentacja wyników**\n"
                    "   - Pokazać przykładowy odcięty baseline, żeby było widać, "
                    "na czym polega baseline correction (?)\n"
                    "   - Wykres przedstawiający metodykę liczenia powtarzalności - wykres uśrednionych widm "
                    "z wielu podłoży (1 krzywa to 1 podłoże) dla danej modyfikacji "
                    "i opis jak liczymy o ile się od siebie różnią. Następnie porównanie końcowego wyniku dla podłoży"
                    "przed i po danej modyfikacji.\n"
                    "       * podana miara statystyczna (RMSE lub inna)\n"
                    "       * podane czy różnice są istotne statystycznie (wynik testu statystycznego)\n"
                    "       * dla widm PMBA - EF\n",
                    unsafe_allow_html=True
                    )


if __name__ == '__main__':
    repeatability()
