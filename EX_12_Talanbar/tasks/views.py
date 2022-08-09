from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Task


@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        if task_id in Task.objects.values_list("id", flat=True):
            record = Task.objects.get(id=task_id)
            record.delete()
            return HttpResponse(f"Task Done :' {record}'")
        else:
            return HttpResponse(f"There isn't any task with id 'task_id'")