from django.http import HttpResponse
from .models import Task
from django.db.models.functions import Lower


def list_create_tasks(request):
    if request.method == 'GET':
        to_do_list = Task.objects.order_by(Lower('name'))
    tasks = '<br>'.join(map(str, to_do_list))
    return HttpResponse(tasks)


def count_tasks(request):
    if request.method == 'GET':
        count = Task.objects.all().count()
    return HttpResponse(f'you have \'{count}\' tasks to do')
