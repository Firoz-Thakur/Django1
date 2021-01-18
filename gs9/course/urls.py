from django.urls import path

from . import views
from django.urls import path


urlpatterns = [
    path('learnd/',views.learn_django),
    path('learnp/',views.learn_python),
]
