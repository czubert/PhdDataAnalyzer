import io

import streamlit
from detect_delimiter import detect

import exceptions
from data_types import bwtek, saved_spectra


def read_files(files, delim):
    try:
        df, bwtek_metadata = bwtek.read_bwtek(files, delim)
    except ValueError:
        print("BWtek spectrometer not found")

        try:
            df = saved_spectra.read_saved_spectra(files, delim)
        except exceptions.WrongSpectrometerReadingError as e:
            print(f'Wrong format of saved data {e}')

    # fix comma separated decimals (stored as strings)
    for col in df.columns:
        try:
            df.loc[:, col] = df[col].str.replace(',', '.').astype(float)
        except (AttributeError, ValueError):
            ...
    
    return df


def files_to_df(files):
    new_files = []
    delim = None

    for file in files:
        file.seek(0)
        lines = file.readlines()

        try:
            lines = [line.decode('utf-8') for line in lines]
        except AttributeError:
            pass

        first_lines = '\n'.join(lines[:20])
        delim = detect(first_lines)
        colnum = lines[-2].count(delim)

        lines = [i for i in lines if i.count(delim) == colnum]
        text = '\n'.join(lines)
        buffer = io.StringIO(text)
        buffer.name = file.name
        new_files.append(buffer)

    return read_files(new_files, delim)

    # try:
    #     df = read_files(new_files, delim)
    #     return df
    #
    # except (TypeError, ValueError) as e:
    #     st.write(f"Try choosing another type of spectra\n Reason:\n{e}")
    #     st.stop()

