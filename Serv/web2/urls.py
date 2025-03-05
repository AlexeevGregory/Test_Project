from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('generate_code/', views.generate_code_view, name='generate_code'),
    path('logout/', views.logout_view, name='logout'),  # Путь к функции logout
]