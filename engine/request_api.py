import requests
from datetime import datetime

'''
    This module is responsible for requesting the historical series through the POST method.
    We build the header and body to follow the pattern of the request made by the server
'''


class RequestAPI:
    def __init__(self, num_serie):
        self.url = 'https://www3.bcb.gov.br/sgspub/consultarvalores/consultarValoresSeries.do?method=consultarValores'
        end = datetime.today().strftime('%d-%m-%Y').replace('-', '%2F')
        self.payload = f'optSelecionaSerie={num_serie}&' \
                       'dataInicio=01%2F01%2F1995&' \
                       f'dataFim={end}' \
                       'selTipoArqDownload=1&' \
                       f'hdOidSeriesSelecionadas={num_serie}&' \
                       'hdPaginar=false'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www3.bcb.gov.br',
            'Pragma': 'no-cache',
            'Referer': 'https://www3.bcb.gov.br/sgspub/consultarvalores/telaCvsSelecionarSeries.paint',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        }

    def get(self):
        return requests.request("POST", self.url, headers=self.headers, data=self.payload)
