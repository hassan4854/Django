from django.urls import path

from .views import *

urlpatterns = [
    path('sad/<str:name>/', sad_func),
    path('happy/<str:name>/<int:n>/', happy_func),
]
