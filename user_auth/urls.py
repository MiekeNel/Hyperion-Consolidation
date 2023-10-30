from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'user_auth'
urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('authenticate/', views.authenticate_user, name='authenticate_user'),
    #path('show_user/', views.show_user, name='show_user'),
    path('register/', views.user_registration, name='register')
]
