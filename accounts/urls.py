from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('todos/', views.todo_list_view, name='todo_list'),
    path('todos/create/', views.create_todo, name='create_todo'),
    path('todos/<int:todo_id>/edit/', views.edit_todo, name='edit_todo'),
    path('todos/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('todos/<int:todo_id>/toggle/', views.toggle_todo, name='toggle_todo'),
]