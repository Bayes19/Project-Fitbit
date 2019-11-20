import pandas as pd
def get_df():
    csv1 = pd.read_csv("april-may.csv")
    csv2 = pd.read_csv("may-june.csv")
    csv3 = pd.read_csv("june-july.csv")
    csv4 = pd.read_csv("july-aug.csv")
    csv5 = pd.read_csv("aug-sep.csv")
    csv6 = pd.read_csv("sep-oct.csv")
    csv7 = pd.read_csv("oct-nov.csv")
    csv8 = pd.read_csv("nov-dec.csv")
    frames = [csv1, csv2, csv3, csv4, csv5, csv6, csv7, csv8]
    df = pd.concat(frames)
    df = df.reset_index()
    return df.drop(columns=["index"])


