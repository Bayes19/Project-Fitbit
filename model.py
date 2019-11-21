import pandas as pd
from prep import prep_df, time_split_2, test_train_split
import seaborn as sns




def next_two_weeks_Holt(df):
    import matplotlib.pyplot as plt
    from statsmodels.tsa.api import Holt
    df = df.set_index('Date')
    final = pd.DataFrame()
    for var in df.columns:
            model = Holt(df[var]).fit(smoothing_level=.3, smoothing_slope=.1, optimized=False)
            final[var] = pd.Series(model.forecast(14))
    return final


'''<<<<<<< HEAD
=======
def lineplot(df):
    from sklearn.preprocessing import MinMaxScaler
    import seaborn as sns
    scaler = MinMaxScaler()
    scaler.fit(df)
    df2 = pd.DataFrame(scaler.transform(df))
    df2 = df2.rename(columns={0:"Calories Burned", 1:"Steps",2:"Distance",3:"Floors",4:"Minutes Sedentarty",5:"Minutes Lightly Active"\
        ,6:"Minutes Fairly Active",7:"Minutes Very Active", 8:"Activity Calories", 9:"BMR"})
    df2 = df2.set_index(df.index)
    return df2
>>>>>>> 8b998b1bfea4b5611b6d35a8d1d3f3d6ce1f2103'''

def all_decompose(df):
    df = df.set_index(["Date"])
    for var in df.columns:
        import statsmodels.api as sm
        decomposition = sm.tsa.seasonal_decompose(df[var])
        fig = decomposition.plot()
        plt.title(str(var))
        plt.show()


def prep_prophet_data1(df: pd.DataFrame) -> pd.DataFrame:
    return (df.assign(ds=pd.to_datetime(df.Date)).sort_values('ds')
            .assign(y=df.Steps)
            .groupby(['ds'])['Steps'].sum().reset_index().set_index('ds'))

def prep_steps_data2(df: pd.DataFrame) -> pd.DataFrame:
    return (df.assign(ds=pd.to_datetime(df.Date)).sort_values('ds')
            .assign(y=df.Calories_Burned)
            .groupby(['ds'])['Calories_Burned'].sum().reset_index().set_index('ds'))


def prep_steps_data3(df: pd.DataFrame) -> pd.DataFrame:
    return (df.assign(ds=pd.to_datetime(df.Date)).sort_values('ds')
            .assign(y=df.Activity_Calories)
            .groupby(['ds'])['Activity_Calories'].sum().reset_index().set_index('ds'))


