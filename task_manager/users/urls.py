from django.urls import path

from task_manager.users import views

app_name = "users"

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='list'),
    path('users/create/', views.RegistrationView.as_view(), name='create'),
]
