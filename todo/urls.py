from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('new/', views.task_create, name='task_create'),
    path('edit/<int:task_id>/', views.task_update, name='task_update'),
    path('toggle/<int:task_id>/', views.task_toggle, name='task_toggle'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
    path('signup/', views.signup, name='signup'),
]