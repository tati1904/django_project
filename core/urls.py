from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inbox/', views.inbox, name="inbox"),
    path('send_message/', views.send_message, name="send_message"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
]
