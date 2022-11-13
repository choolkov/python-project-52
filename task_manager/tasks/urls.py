from django.urls import path

from task_manager.tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('create/', views.CreateTaskView.as_view(), name='create'),
    path('<int:pk>/', views.TaskView.as_view(), name='preview'),  # TODO
    path('<int:pk>/update/', views.UpdateTaskView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete'),
]
