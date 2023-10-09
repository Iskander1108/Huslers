from django.urls import path
from .views import register_view, index, login_view, logoutUser



urlpatterns = [
    path('register/', register_view, name='register'),
    path('', index, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logoutUser, name='logout'),
]