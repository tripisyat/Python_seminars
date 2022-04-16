from datetime import datetime as dt

def temperature_logger(data): #описываем логирование в файл температуры
    time = dt.now().strftime('%H:%M')# получаем время начала логирования
    with open('log.cvs', 'a') as file: #открываем файл log.cvs
        file.write('{} - temperature = {}\n'
                    .format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('{} - pressure = {}\n'
                    .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('{} - wind_speed = {}\n'
                    .format(time, data))