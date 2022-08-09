from django.http import HttpResponse


def sad_func(request, name):
    response = f'Nobody likes you, {name}!'
    return HttpResponse(response)


def happy_func(request, name, n):
    response = ''
    for _ in range(n):
        response += f'You are great, {name} :)\n'
    return HttpResponse(response, content_type='text/plain')
