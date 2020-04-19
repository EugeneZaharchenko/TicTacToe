from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home

urlpatterns = [
    path('home/', home, name='player_home'),
    path('login/', LoginView.as_view(template_engine='player/login_form.html'), name='player_login'),
    path('logout/', LoginView.as_view(), name='player_logout'),
]
