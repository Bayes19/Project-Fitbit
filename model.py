import pandas as pd
from prep import prep_df, time_split_2, test_train_split
import seaborn as sns
from fbprophet import Prophet
from matplotlib.dates import MonthLocator, num2date
from matplotlib.ticker import FuncFormatter




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
            .groupby(['ds'])['y'].sum().reset_index().set_index('ds'))
           

def prep_steps_data2(df: pd.DataFrame) -> pd.DataFrame:
    return (df.assign(ds=pd.to_datetime(df.Date)).sort_values('ds')
            .assign(y=df.Calories_Burned)
            .groupby(['ds'])['y'].sum().reset_index().set_index('ds'))


def prep_steps_data3(df: pd.DataFrame) -> pd.DataFrame:
    return (df.assign(ds=pd.to_datetime(df.Date)).sort_values('ds')
            .assign(y=df.Activity_Calories)
            .groupby(['ds'])['y'].sum().reset_index().set_index('ds'))


def steps_prophet(df1):
   #steps
    m = Prophet()
    m.fit(df1)
    #Predictions
    future1 = m.make_future_dataframe(periods=365)
    forecast1 = m.predict(future1)
    forecast1[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()
    #Predicting 14 days into the future
    future1 = m.make_future_dataframe(periods=14)
    forecast1 = m.predict(future1)
    df1= forecast1.filter(['ds', 'yhat'])
    df1= df1.rename(columns={'ds':'future date', "yhat": "predicted_steps"}).tail(14)
    df1.predicted_steps=df1.predicted_steps.round()
    df1=df1.tail(14)
    return df1

def Calories_Burned_prophet(df2):
    #Calories Burned
    m = Prophet()
    m.fit(df2)
    #Predictions
    future2 = m.make_future_dataframe(periods=365)
    forecast2 = m.predict(future2)
    forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()
    #Predicting 14 days into the future
    future2 = m.make_future_dataframe(periods=14)
    forecast2 = m.predict(future2)
    df2= forecast2.filter(['ds', 'yhat'])
    df2= df2.rename(columns={'ds':'future date', "yhat": "Calories_Burned"}).tail(14)
    df2.Calories_Burned=df2.Calories_Burned.round()
    df2=df2.tail(14)
    return df2




def Activity_Calories_prophet(df3):
    #Activity Calories
    m = Prophet()
    m.fit(df3)
    #Predictions
    future3 = m.make_future_dataframe(periods=365)
    forecast3 = m.predict(future3)
    forecast3[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head()
    #Predicting 14 days into the future
    future3 = m.make_future_dataframe(periods=14)
    forecast3 = m.predict(future3)
    df3= forecast3.filter(['ds', 'yhat'])
    df3= df3.rename(columns={'ds':'future date', "yhat": "Activity_Calories"}).tail(14)
    df3.Activity_Calories=df3.Activity_Calories.round()
    df3=df3.tail(14)
    return df3