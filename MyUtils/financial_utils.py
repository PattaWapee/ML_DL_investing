def CalReturn(data,frequencies= 'D'):
    """
    Calculate the return of the stock price
    :param data: the stock price data
    :param frequencies: the frequency of the data, 
        default is D (daily) other params are W (weekly, M (monthly), Y (yearly)
    :return: the return of the stock price
    """
    if frequencies == 'D':
        data_return = data["Adj Close"].pct_change() * 100
    else:
        data_return = data['Adj Close'].resample(frequencies).ffill().pct_change().plot()
    
    return data_return
    
def ResampleAggreg(data, frequencies = 'W', ret=True):
    """
    Resample the data and aggregate the data
    :param data: the stock price data
    :param frequencies: the frequency of the data, 
        default is D (daily) other params are W (weekly, M (monthly), Y (yearly)
    :return: the aggregated data
    """
    if frequencies == 'W':
        df_aggreg = data.resample('W-FRI').agg({'Open':'first',
                                    'High':'max',
                                    'Low':'min',
                                    'Close':'last',
                                    'Volume':'sum'})
        df_aggreg['weekly_return'] = df_aggreg['Close'].pct_change(-1)
    elif frequencies == 'M':
        df_aggreg = data.resample('BM').agg({'Open':'first',
                                             'High':'max',
                                             'Low':'min',
                                             'Close':'last',
                                             'Volume':'sum'})
        df_aggreg['monthly_return'] = df_aggreg['Close'].pct_change(-1)
    
    return df_aggreg