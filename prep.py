import pandas as pd
from acquire import get_df

def prep_df():
    df = get_df()
    df["Date"] = pd.to_datetime(df.Date)
    df = df.set_index(["Date"])
    col_int = ["Floors", "Distance", "Minutes Fairly Active", "Minutes Lightly Active", "Minutes Very Active"]
    for n in col_int:
        df[n] = df[n].astype(float)
    col = ["Calories Burned","Activity Calories","Minutes Sedentary", "Steps"]
    for n in col:
        df[n] = df[n].str.replace(",", "").astype(float)
    return df




def test_train_split(df, train_amount):
    train_size = int(len(df) * train_amount)
    train, test = df[0:train_size].reset_index(), df[train_size:len(df)].reset_index()
    train.set_index(["Date"])
    test.set_index(["Date"])
    return train, test



def cluster_split_train_and_test(train, test, target):
    X_train = train.drop(columns=[target])
    y_train = train[target]
    X_test = test.drop(columns=[target])
    y_test = test[target]
    return X_train, y_train, X_test, y_test

def time_split(train, test, target):
    X_train = train.index 
    y_train = trian[target]
    X_test = test.index
    y_test = test[target]
    return X_train, y_train, X_test, y_test