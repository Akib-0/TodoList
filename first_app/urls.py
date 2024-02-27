from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeTemplate.as_view(),name='homepage'),
    path('task_add/',views.TodoForm.as_view(),name='taskaddpage'),
    path('show_tasks/',views.TaskListView.as_view(),name='show_tasks'),
    path('edit_task<str:pk>/',views.TaskUpdate.as_view(),name='edit_task'),
    path('delete_task<str:pk>/',views.DeleteTask.as_view(),name='delete_task'),
    path('move_to_completed/<str:pk>/', views.MoveToCompletedView.as_view(),name='move_to_completed'),
    path('completed_task/', views.CompletedTask.as_view(), name='completed'),
]