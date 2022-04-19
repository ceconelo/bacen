from bacen_calendar import *
from crontab import CronTab

'''
    This module is responsible for scheduling in crontab
'''

GREEN = '\033[92m[+]\033[0m'
RED = '\033[31m[*]\033[0m'


def set_schedules():
    # Getting and iterating over calendar data
    for month, day in get_calendar().items():
        user_cron = CronTab(user=True)
        # command = ~/path to virtual environment ~/path to the module to be executed by crontab
        job = user_cron.new(command='~/it/projetos/bacen/venv/bin/python3 ~/it/projetos/bacen/main.py')
        job.hour.on(10)  # 10 hours
        job.day.on(int(day))
        job.month.on(int(month))
        user_cron.write()
    print(f'{GREEN} Scheduling done.')


if __name__ == '__main__':
    set_schedules()
