import pandas as pd
from acquire import get_df

def prep_df():
    df = get_df()
    df["Date"] = pd.to_datetime(df.Date)
    df = df.set_index(["Date"])
    return df