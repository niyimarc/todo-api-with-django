from todolist import views 
from django.urls import path

urlpatterns = [
    path('', views.TodosAPIView.as_view(), name='todos'),
]
