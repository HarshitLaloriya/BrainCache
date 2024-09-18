from django.urls import path
from . import views

# declaration of url patterns

urlpatterns = [
    path(route='', view=views.index)
]
