import pandas as pd
from prep import prep_df, time_split_2, test_train_split
import seaborn as sns
df = prep_df()
X_train, y_train, X_test, y_test = time_split_2(df)
train, test = test_train_split(df, .66)

def evaluate(target_var, train = train, test = test, output=True):
    mse = metrics.mean_squared_error(test[target_var], yhat[target_var])
    rmse = math.sqrt(mse)

    if output:
        print('MSE:  {}'.format(mse))
        print('RMSE: {}'.format(rmse))
    else:
        return mse, rmse

def plot_and_eval(target_vars, train = train, test = test, metric_fmt = '{:.2f}', linewidth = 4):
    if type(target_vars) is not list:
        target_vars = [target_vars]

    plt.figure(figsize=(16, 8))
    plt.plot(train[target_vars],label='Train', linewidth=1)
    plt.plot(test[target_vars], label='Test', linewidth=1)

    for var in target_vars:
        mse, rmse = evaluate(target_var = var, train = train, test = test, output=False)
        plt.plot(yhat[var], linewidth=linewidth)
        print(f'{var} -- MSE: {metric_fmt} RMSE: {metric_fmt}'.format(mse, rmse))

    plt.show()

    yhat[var] = pd.DataFrame(model.forecast(test[var].shape[0]), columns=[var])

def next_two_weeks_Holt(df):
    import matplotlib.pyplot as plt
    from statsmodels.tsa.api import Holt
    df = df.set_index('Date')
    final = pd.DataFrame()
    for var in df.columns:
            model = Holt(df[var]).fit(smoothing_level=.3, smoothing_slope=.1, optimized=False)
            final[var] = pd.Series(model.forecast(14))
    return final


<<<<<<< HEAD
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
>>>>>>> 8b998b1bfea4b5611b6d35a8d1d3f3d6ce1f2103

def all_decompose(df):
    df = df.set_index(["Date"])
    for var in df.columns:
        import statsmodels.api as sm
        decomposition = sm.tsa.seasonal_decompose(df[var])
        fig = decomposition.plot()
        plt.title(str(var))
        plt.show()

