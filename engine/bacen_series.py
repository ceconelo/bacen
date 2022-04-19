import pandas as pd
from time import sleep
from engine.request_api import RequestAPI
from datetime import datetime, timedelta

''' 
    Module responsible for obtaining the last line recorded in the historical series (22707, 22708 e 22709)
    and the provisional data in the external sector statistics worksheet.
'''

GREEN = '\033[92m[+]\033[0m'
RED = '\033[31m[*]\033[0m'


class BacenHistorical:
    def __init__(self):
        self.historical_series = ['22707', '22708', '22709']
        self.data = {
            'Serie': [],
            'Date': [],
            'Value': []
        }

    # Method that parses the historical series data
    def get_last_row_historical_series(self):
        # Scrolling through the series list
        for h_s in self.historical_series:
            print(f'{GREEN} Looking for series: {h_s}')
            response = RequestAPI(h_s).get()
            table = pd.read_html(response.content, match='List of values', header=2, thousands='.', decimal=',')[0]
            table = table[:-2]  # Deleting the last two lines
            self.data['Serie'].append(h_s)
            self.data['Date'].append(table.iloc[-1, 0])
            self.data['Value'].append(table.iloc[-1, 1])
            sleep(5)
        return self.data

    # Method that accesses the worksheet that contains the provisional data of the series
    def get_provisional_data(self):
        print(f'{GREEN} Getting provisional data')
        # Always looking for last month's worksheet
        last_mounth = (datetime.today() - timedelta(days=30)).strftime('%m')
        #last_mounth = '01'  # Test
        url = f'https://www.bcb.gov.br/content/estatisticas/hist_estatisticassetorexterno/2022{last_mounth}_Tabelas_de_estatisticas_do_setor_externo.xlsx'
        try:
            table = pd.read_excel(url, sheet_name='Tabela 1')
        except BaseException as e:
            print(f'{RED} Could not access the file: {url}')
            print(f'Error: {e}')
            exit(0)

        # Month and year of reference of provisional data
        ref = table.iloc[5, 3] + '/' + table.iloc[3, 3]
        ref = str(ref).replace('*', '')

        # The data is located in table 1 of the worksheet, columns D11, D12 and D13.
        balance = round(table.iloc[9, 3], 0)  # Column 3 and row 9
        exports = round(table.iloc[10, 3], 0)  # Column 3 and row 10
        imports = round(table.iloc[11, 3], 0)  # Column 3 and row 11

        self.clear_data(self.data.keys())
        self.set_data_provisional('22707', ref, balance)
        self.set_data_provisional('22708', ref, exports)
        self.set_data_provisional('22709', ref, imports)

        return self.data

    def set_data_provisional(self, ref, num_serie, value):
        self.data['Serie'].append(num_serie)
        self.data['Date'].append(ref)
        self.data['Value'].append(value)

    def clear_data(self, keys):
        for key in keys:
            self.data[key].clear()
