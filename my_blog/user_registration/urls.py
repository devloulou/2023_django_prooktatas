from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [  
    path('register', register, name='register'),  
    path('login', LoginView.as_view(template_name="user_registration/login.html"), name='login'),  
    path('logout', LogoutView.as_view(template_name="user_registration/logout.html"), name='logout'),  
]
