from django.urls import path
from .views import TareaListCreateView

urlpatterns = [
    path('tareas/', TareaListCreateView.as_view(), name='tareas-list-create'),
]
