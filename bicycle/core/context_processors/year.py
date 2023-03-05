import datetime


# функция, возвращающая текущий год. Будет в футере вместе с копирайтом
# показывать всем, что мы - серьезный сайт.
def year(request):
    current_year = int(datetime.datetime.now().year)
    return {'year': current_year}
