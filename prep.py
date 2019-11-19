import pandas as pd
from acquire import get_df

def prep_df():
    df = get_df()
    df["Date"] = pd.to_datetime(df.Date)
    df = df.set_index(["Date"])
    col_int = ["Floors", "Distance", "Minutes Fairly Active", "Minutes Lightly Active", "Minutes Very Active"]
    for n in col_int:
        df[n] = df[n].astype(float)
        print([n])
    col = ["Calories Burned","Activity Calories","Minutes Sedentary", "Steps"]
    for n in col:
        df[n] = df[n].str.replace(",", "").astype(float)
    return df