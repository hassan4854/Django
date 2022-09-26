from django.shortcuts import render, HttpResponse
from .models import Musician, Album
from django.views.generic.list import ListView


class Musician_list(ListView):
    def get(self, request):
        musician_name = Musician.objects.order_by("name").values_list("name", flat=True)
        return HttpResponse(musician_name)


