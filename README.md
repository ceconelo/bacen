
# Data scraping on Time Series Management System of Bank Central of Brasil (SGS)


SGS System aims at consolidating and providing economical and financial information, as well as keeping the uniformity of documents generated out of the time series stored within it.




## About project

This project scrapes data from the 22707, 22708 and 22709 series into two information sources.

1. https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries
2. https://www.bcb.gov.br/estatisticas/historicosetorexterno

Bacen maintains an updated calendar with the schedule for the publication of data from these series.
We created a module in this project that requests this calendar and creates the schedules in crontab.



## Roadmap

- Put the project into your virtual environment

- In the engine/schedules.py file set the path to your virtual environment and path to the main.py file.
  (eg. job = user_cron.new(command='~/it/projetos/bacen/venv/bin/python3 ~/it/projetos/bacen/main.py')

- Install the necessary libraries (requirements.txt)
  


## How to Use
In project folder.

- Schedule modulo.
```bash
  python3 engine/schedules.py 
```

- Series scraping
```bash
  python3 main.py
```

