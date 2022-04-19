import pandas as pd
from engine.bacen_series import BacenHistorical

'''
    Main module that makes the necessary calls to obtain the historical series and provisional data and later stores 
    the data in CSV files. 
'''


def main():
    print('Initializing')
    bacen = BacenHistorical()

    histotical_data = bacen.get_last_row_historical_series()
    df_historical = pd.DataFrame(histotical_data)
    df_historical.to_csv('dataset/historical_series.csv')

    provisional_data = bacen.get_provisional_data()
    df_provisional = pd.DataFrame(provisional_data)
    df_provisional.to_csv('dataset/provisional_data.csv')


if __name__ == '__main__':
    main()
