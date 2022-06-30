from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'У меня получилось! И даже приходят уведомления в Telegram'
    )


def second_page(request):
    return HttpResponse('А это вторая страница!')
