import datetime


def year(request):
    ''' функция, возвращающая текущий год. Будет в футере вместе с копирайтом
    показывать всем, что мы - серьезный сайт. '''
    current_year = int(datetime.datetime.now().year)
    return {'year': current_year}
