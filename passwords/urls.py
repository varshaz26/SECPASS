from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login_view, name='index'),
    path('register/', views.register_page, name='register'),  # Registration page
    path('home/', views.home_page, name='home'),  # Home page
    path('logout/', views.logout_view, name='logout'),  # Logout

    path('add_password/', views.add_new_password, name='add_password'),
    path('manage_passwords/', views.manage_passwords, name='manage_passwords'),
    path('edit_password/<str:pk>/', views.edit_password, name='edit_password'),
    path('search/', views.search, name='search'),

]
