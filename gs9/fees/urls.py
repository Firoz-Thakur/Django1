from django.urls import path

from . import views
from django.urls import path


urlpatterns = [
    path('feesdj/',views.fees_django),
]
