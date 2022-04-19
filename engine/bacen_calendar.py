import pandas as pd
import requests
from html_table_parser import HTMLTableParser

'''
    Module responsible for obtaining the schedule of economic and financial disclosures from the central bank
'''

GREEN = '\033[92m[+]\033[0m'
RED = '\033[31m[*]\033[0m'


# Request for the page that contains the data
def request_content():
    url = "https://www.bcb.gov.br/api/servico/sitebcb/accordiondados?tronco=estatisticas&guidLista=6317bfdc-16b2-42f6-a7c9-89e419ed6cb6"
    payload = {}
    headers = {
        'authority': 'www.bcb.gov.br',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.bcb.gov.br/estatisticas/notas_calendario',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/100.0.4896.88 Safari/537.36 '
    }
    return requests.request("GET", url, headers=headers, data=payload).text


# Parser on the table that contains the calendar
def get_calendar():
    parser_tables = HTMLTableParser()
    print(f'{GREEN} Getting a release calendar.')
    parser_tables.feed(request_content())
    calendar_table = pd.DataFrame(parser_tables.tables[0])
    calendar_table = calendar_table.iloc[2:14, [0, 1]]  # Rows 2:14 and Columns 0 e 1 of dataframe
    return to_dict(calendar_table[1].values)


# Returns dictionary containing numeric month (1-12) and days
def to_dict(days):
    return {i: days[i - 1] for i in range(1, 13)}
