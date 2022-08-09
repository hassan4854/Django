from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Task


@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        added_task = request.POST.get('task')
        new_task = Task(name=added_task)
        new_task.save()
        return HttpResponse(f"Task Created: '{added_task}'")

    elif request.method == 'GET':
        return HttpResponse(f"it works")
