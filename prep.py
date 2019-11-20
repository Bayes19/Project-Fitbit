import pandas as pd
from acquire import get_df
import numpy as np

def prep_df():
    df = get_df()
    df["Date"] = pd.to_datetime(df.Date)
    col_int = ["Floors", "Distance", "Minutes Fairly Active", "Minutes Lightly Active", "Minutes Very Active"]
    for n in col_int:
        df[n] = df[n].astype(float)
    col = ["Calories Burned","Activity Calories", "Steps", "Minutes Sedentary"]
    for n in col:
        df[n] = df[n].astype("str").str.replace(",", "").astype(float)
    median = df['Floors'].median()
    median
    df["Floors"] = np.where(df["Floors"] > df["Floors"].mean()*2, median,df['Floors'])
    return df

def test_train_split(df, train_amount):
    train_size = int(len(df) * train_amount)
    train, test = df[0:train_size].reset_index(), df[train_size:len(df)].reset_index()
    train = train.set_index(["Date"])
    test = test.set_index(["Date"]) 
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


def time_split_2(df):
    import numpy as np
    X = df.Date
    y = df.Steps

    X = np.array(X)
    y = np.array(y)

    from sklearn.model_selection import TimeSeriesSplit
    tss = TimeSeriesSplit(n_splits=4, max_train_size=None)

    for train_index, test_index in tss.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

    X_train = pd.Series(X_train)
    y_train = pd.Series(y_train)
    X_test = pd.Series(X_test)
    y_test = pd.Series(y_test)

    return X_train, y_train, X_test, y_test