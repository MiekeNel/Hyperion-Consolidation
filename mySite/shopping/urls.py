from django.urls import path, include, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shopping'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]