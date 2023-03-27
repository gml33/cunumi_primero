
from datetime import datetime, timedelta
from .models import turno


def validWeekday(dias):
    # Loop days you want in the next 21 days:
    hoy = datetime.now()
    weekdays = []
    for i in range(0, dias):
        x = hoy + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if turno.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if turno.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def checkEditTime(times, day, id):
    # Only show the time of the day that has not been selected before:
    x = []
    turnoVar = turno.objects.get(pk=id)
    hora = turnoVar.hora
    for k in hora:
        if turno.objects.filter(dia=day, hora=k).count() < 1 or hora == k:
            x.append(k)
    return x


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y
